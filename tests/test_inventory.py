import unittest
from utils import classify_object, filter_by_shape


class TestInventory(unittest.TestCase):

    def test_classify_medium(self):
        obj = {
            "id": 1,
            "color": "red",
            "shape": "sphere",
            "weight_g": 125
        }
        self.assertEqual(classify_object(obj), "Medium")

    def test_classify_light(self):
        obj = {
            "id": 2,
            "color": "white",
            "shape": "cylinder",
            "weight_g": 95
        }
        self.assertEqual(classify_object(obj), "Light")

    def test_classify_heavy(self):
        obj = {
            "id": 3,
            "color": "green",
            "shape": "cube",
            "weight_g": 190
        }
        self.assertEqual(classify_object(obj), "Heavy")

    def test_filter_by_shape(self):
        objects = [
            {
                "id": 1,
                "color": "red",
                "shape": "sphere",
                "weight_g": 123
            },
            {
                "id": 2,
                "color": "white",
                "shape": "cylinder",
                "weight_g": 95
            },
            {
                "id": 3,
                "color": "green",
                "shape": "cube",
                "weight_g": 190
            },
            {
                "id": 4,
                "color": "yellow",
                "shape": "cylinder",
                "weight_g": 173
            },
            {
                "id": 5,
                "color": "black",
                "shape": "sphere",
                "weight_g": 80
            }
        ]

        result = filter_by_shape(objects, "sphere")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()