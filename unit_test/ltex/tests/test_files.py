import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest, logging
from files import Dictionary
# logging.basicConfig(level=logging.DEBUG)


class TestDictionary(unittest.TestCase):
    # def setUp(self) -> None:

    def testCreateDict(self):
        Dictionary().create_dictionary()
        cwd, filename = os.getcwd(), Dictionary().filename
        path = "{}/{}".format(cwd, filename)
        file_exist = os.path.exists(path)
        logging.debug("Creating {}".format(path))
        self.assertTrue(file_exist, "File doesn't created")

    def testReadDict(self):
        content = Dictionary().read_dictionary()
        logging.debug("Dictionary content: {}".format(content))
        self.assertEqual(Dictionary().body, content, "Body corrupted")


