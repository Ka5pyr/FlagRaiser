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

def clean_up(db_file_no_ext, output_full_path):
    directories = ["./dist", "./build"]
    files = [f"{db_file_no_ext}.spec", f"./out/{db_file_no_ext}.py"]
    move_file(f"./dist/{db_file_no_ext}", output_full_path)

    
    [remove_dir(directory) for directory in directories]
    [remove_file(file) for file in files]
    wipe_file("./py-modules/db.py")
    

def test_db():
    check_processor.process_checks()

def create_dir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created successfully")
    except Exception as e:
        print(f"Error creating directory '{directory}': {e}")
        sys.exit(0)
        
def remove_dir(directory):
    try:
        shutil.rmtree(directory)
    except Exception as e:
        print(f"Error removing directory '{directory}': {e}")
        sys.exit(0)

def move_file(source, destination):
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"Error moving file '{source}': {e}")

def remove_file(file):
    try:
        os.remove(file)
    except Exception as e:
        print(f"Error removing file '{file}': {e}")
        sys.exit(0)
        
def copy_file(source, destination):    
    try:
        shutil.copy(source, destination)
    except Exception as e:
        print(f"Error copying file '{source}': {e}")
    
def create_py_file(py_full_path):
    file_content = [
        "import sys",
        "",
        "sys.path.append('./py-modules/')",
        "import check_processor",
        "",
        "def main():",
        "    check_processor.process_checks()",
        "",
        "if __name__ == '__main__':",
        "    main()",
        ""
    ]
    try:
        with open(py_full_path, 'w') as f:
            f.write('\n'.join(file_content))
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(0)

def wipe_file(file):
    try:
        with open(file, 'w'):
            pass
    except Exception as e:
        print(f"Error: Couldn't wipe file {file} - {e}")

def main():
    args = parse_arguments()
    db_file = args.db_file
    db_file_no_ext = db_file.split(".")[0]
    if not db_file.endswith('.py'):
        print(f"Error: The Database File '{db_file}' needs to be a py file")
        sys.exit(0)
    db_path = args.db_file_path
    db_full_path = os.path.join(db_path, db_file)
    if not os.path.exists(db_full_path):
        print(f"Error: Database file '{db_file}' does not exist.")
        

    if args.output_file is None:
        output_file = db_file_no_ext
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
    
    py_full_path = output_full_path + ".py"
    wipe_file("./py-modules/db.py")
    copy_file(db_full_path, "./py-modules/db.py") 
    if args.test:
        test_db()
        sys.exit(0)
    create_py_file(py_full_path)
    py_compiler.compile(py_full_path)
    clean_up(db_file_no_ext, output_full_path)
    

if __name__ == "__main__":
    main()