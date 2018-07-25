import unittest

from PyCode.FileInfoCollection import FileInfoCollection
from PyCode.FileInfoContainer import FileInfoContainer


class TesterUnittest(unittest.TestCase):
    def test_container(self):
        container = FileInfoContainer('D:\Download\installed\calc.py')

        self.assertEqual(container.num_of_line, 26)
        self.assertEqual(container.num_of_method, 4)
        self.assertEqual(container.num_of_class, 2)

        container_info = container.get_info()
        self.assertEqual(container_info,
                         'file name: D:\Download\installed\calc.py\n\tline: 26\n\tmethod: 4\n\tclass: 2')

    def test_collection(self):
        collection = FileInfoCollection('D:\Download\installed')

        container = collection.get(-1)
        self.assertEqual(container, None)

        container = collection.get(0)
        self.assertEqual(container.num_of_line, 26)
        self.assertEqual(container.num_of_method, 4)
        self.assertEqual(container.num_of_class, 2)

        container = collection.get(1)
        self.assertEqual(container.num_of_line, 7)
        self.assertEqual(container.num_of_method, 0)
        self.assertEqual(container.num_of_class, 0)

        container = collection.get(2)
        self.assertEqual(container.num_of_line, 10)
        self.assertEqual(container.num_of_method, 1)
        self.assertEqual(container.num_of_class, 1)

        container = collection.get(3)
        self.assertEqual(container, None)
