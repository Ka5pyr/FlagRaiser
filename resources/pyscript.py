import sys

sys.path.append('./py-modules/')
import check_processor


def main():
    check_processor.process_checks(db_full_path, db_path, db_file)


if __name__ == "__main__":
    main()