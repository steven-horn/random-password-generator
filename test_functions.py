import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_length(self):
        self.assertEqual(length(8),8)
        self.assertEqual(length('a'), False)
        self.assertEqual(length(0), False)
        self.assertEqual(length(589), False)



if __name__ == '__main__':
    unittest.main()
