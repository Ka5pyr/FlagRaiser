import argparse
import os
import sys

sys.path.append('./py-modules/')
import check_processor

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
                        default="./out/",
                        help="")
    
    return parser.parse_args()


def test_db(db_full_path, db_path, db_file):
    check_processor.process_checks(db_full_path, db_path, db_file)


def main(args):
    print(args)
    db_file = args.db_file
    if not db_file.endswith('.py'):
        print(f"Error: The Database File '{db_file}' needs to be a py file")
        sys.exit(0)
    db_path = args.db_file_path
    db_full_path = os.path.join(db_path, db_file)
    if not os.path.exists(db_full_path):
        print(f"Error: Database file '{db_file}' does not exist.")
        sys.exit(0)

    if args.output_file is None:
        output_file = db_file.split(".")[0]
    else:
        output_file = args.output_file
        
    
    if args.test:
        test_db(db_full_path, db_path, db_file)
    elif args.build:
        pass


if __name__ == "__main__":
    args = parse_arguments()
    main(args)