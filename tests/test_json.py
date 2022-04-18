import unittest
import json


class ValidateJson(unittest.TestCase):

    def setUp(self):
        with open("data/dummy.json", "r") as f:
            self.data = json.load(f)

    def test1(self):
        self.assertGreaterEqual(len(self.data["data"]), 1)

    def test2(self):
        for d in self.data["data"]:
            self.assertIn("name", d)

if __name__ == '__main__':
    unittest.main()
