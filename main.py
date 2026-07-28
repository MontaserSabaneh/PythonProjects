from utils import load_test_data
from inventory import Inventory


def main():
    """
    Main program.
    """
    objects = load_test_data()

    inventory = Inventory(objects)

    inventory.classify_all()

    inventory.display()


if __name__ == "__main__":
    main()