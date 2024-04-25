import sys

sys.path.append('./py-modules/')
import check_processor


def main():
    # Process through the checks
    check_processor.process_checks()


if __name__ == "__main__":
    main()