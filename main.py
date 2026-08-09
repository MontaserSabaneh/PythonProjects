import argparse
from utils import load_test_data
from inventory import Inventory


def main():
    """
    Main program.
    """

    parser = argparse.ArgumentParser(
        description="Inventory Classification System"
    )

    parser.add_argument(
        "--file_path",
        type=str,
        required=True,
        help="The target file path to process."
    )

    args = parser.parse_args()

    objects = load_test_data(args.file_path)

    inventory = Inventory(objects)

    inventory.classify_all()

    inventory.display()


if __name__ == "__main__":
    main()