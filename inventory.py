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
        Print all objects.
        """
        for obj in self.objects:
            print(obj)

    def get_objects(self):
        """
        Return all objects.
        """
        return self.objects