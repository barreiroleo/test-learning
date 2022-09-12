import unittest
from world.countries import NewZealand

class TestVisa(unittest.TestCase):
    def setUp(self) -> None:
        self.destiny = NewZealand()
        # return super().setUp()

    def test_destiny(self):
        country = self.destiny.name
        self.assertEqual(country, "New Zealand")

    def test_visa_str(self):
        msg = self.destiny.get_visa("name")
        self.assertIsInstance(msg, str)

if __name__ == "__main__":
    unittest.main()
