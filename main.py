import argparse
import os
from platform import python_compiler
import shutil
import sys

sys.path.append('./py-modules/')
import check_processor
import py_compiler

def parse_arguments():
    parser = argparse.ArgumentParser(description='Flag Raiser Program')

    # Create Groups for the seperate checks
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-B", "--build", action="store_true",
                        help=("Build the Python File with the " 
                              "specified database file."))
    group.add_argument("-T", "--test", action="store_true",
                        help=("Test the DB File in Test Mode. "
                        "This will NOT create an executable."))
    
    parser.add_argument("-dF", "--db-file", type=str,
                        required=True,
                        help="")
    parser.add_argument("-dB", "--db-file-path", type=str,
                        required=True,
                        help="")
    parser.add_argument("-oF", "--output-file", type=str,
                        help="")
    parser.add_argument("-oP", "--output-path", type=str,
                        default="./out",
                        help="")
    
    return parser.parse_args()


def test_db(db_full_path, db_path, db_file):
    check_processor.process_checks(db_full_path, db_path, db_file)

def create_dir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created successfully")
    except Exception as e:
        print(f"Error creating directory '{directory}': {e}")
        sys.exit(0)

def remove_file(file):
    try:
        os.remove(file)
    except Exception as e:
        print(f"Error removing file '{file}': {e}")
        sys.exit(0)
    
def create_py_file(py_full_path):
    try:
        shutil.copyfile("./resources/pyscript.py",
                py_full_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(0)

def main():
    args = parse_arguments()
    db_file = args.db_file
    if not db_file.endswith('.py'):
        print(f"Error: The Database File '{db_file}' needs to be a py file")
        sys.exit(0)
    db_path = args.db_file_path
    db_full_path = os.path.join(db_path, db_file)
    if not os.path.exists(db_full_path):
        print(f"Error: Database file '{db_file}' does not exist.")

    if args.output_file is None:
        output_file = db_file.split(".")[0]
    else:
        output_file = args.output_file
    output_path = args.output_path
    if output_path == "./out":
        create_dir(output_path)
        
    output_full_path = os.path.join(output_path, output_file)
    if not os.path.exists(output_path):
        print(f"Error: Output Path '{output_path}' does not exist.")
        choice = input("Would you like to create the output path? (y/n): ")
        if choice.lower() in ["y","yes"]:
            create_dir(output_path)
        else:
            sys.exit(0)
    if os.path.exists(output_full_path):
        print(f"Error: Output File '{output_full_path}' already exists.")
        choice = input("Would you like to overwrite the file? (y/n): ")
        if choice.lower() in ["y","yes"]:
            remove_file(output_full_path)
        else:
            sys.exit(0)
    
    if args.test:
        test_db(db_full_path, db_path, db_file)
    elif args.build:
        py_full_path = output_full_path + ".py"
        create_py_file(py_full_path)
        py_compiler.compile(py_full_path)


if __name__ == "__main__":
    main()