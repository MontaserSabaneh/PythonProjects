import json

DEFAULT_DATA = "data.json"


def load_test_data(filename=DEFAULT_DATA):
    """
    Load objects from a JSON file.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Data file not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []


def classify_object(obj):
    """
    Classify an object based on its weight.
    """
    if obj["weight_g"] >= 150:
        return "Heavy"
    elif obj["weight_g"] >= 100:
        return "Medium"
    else:
        return "Light"


def filter_by_shape(objects, shape):
    """
    Return all objects with the given shape.
    """
    return [obj for obj in objects if obj["shape"].lower() == shape.lower()]