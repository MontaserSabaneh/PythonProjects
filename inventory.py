import os

from utils import classify_object


class Inventory:
    """
    Inventory class for managing objects.
    """

    def __init__(self, objects):
        self.objects = objects

    def classify_all(self):
        """
        Add a category to every object.
        """
        for obj in self.objects:
            obj["category"] = classify_object(obj)

    def display(self):
        """
        Display all objects and save the output to a file.
        """

        # Create output folder if it does not exist
        os.makedirs("output", exist_ok=True)

        # Output file
        output_path = "output/classified_inventory.txt"

        # Save classified objects
        with open(output_path, "w") as file:
            for obj in self.objects:
                print(obj)
                file.write(str(obj) + "\n")

    def get_objects(self):
        """
        Return all objects.
        """
        return self.objects