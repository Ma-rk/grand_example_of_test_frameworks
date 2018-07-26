import unittest
from unittest.mock import MagicMock

from PyCode.Helper import Helper


class TesterUnittest(unittest.TestCase):
    def setUp(self):
        self.org_generate_content_list_from_file = Helper.generate_content_list_from_file
        self.org_generate_content_list_from_db = Helper.generate_content_list_from_db

        self.mock_content_list = [['mocked pass\\calc.py',
                                   ['class Calc1:\n',
                                    '    def add(self, num_a, num_b):\n',
                                    '        """\n',
                                    '\n',
                                    '        :param num_a: 1st no\n',
                                    '        :param num_b: 2nd no\n',
                                    '        :return: sum of two numbers\n',
                                    '        """\n',
                                    '        num_result = num_a+num_b\n',
                                    '        return num_result\n',
                                    '\n',
                                    '    def subtract(self, num_a, num_b):\n',
                                    '        num_result = num_a-num_b\n',
                                    '        return num_result\n',
                                    '\n',
                                    '\n',
                                    'class Calc2:\n',
                                    '    def multiply(self, num_a, num_b):\n',
                                    '        num_result = num_a*num_b\n',
                                    '        return num_result\n',
                                    '\n',
                                    '    def divide(self, num_a, num_b):\n',
                                    '        num_result = num_a/num_b\n',
                                    '        return num_result\n',
                                    '\n',
                                    '\n']],
                                  ['mocked pass\\HandPy.py',
                                   ['import sys\n',
                                    '\n',
                                    'print(sys.executable)\n',
                                    '\n',
                                    'x = 1000\n',
                                    'y = 1000\n',
                                    'print(x is y)\n']],
                                  ['mocked pass\\py_calc_test.py',
                                   ['from calc import Calc1\n',
                                    '\n',
                                    '\n',
                                    'def test_add():\n',
                                    '    ut_calc1 = Calc1()\n',
                                    '    assert ut_calc1.add(4, 6) == 10\n',
                                    '\n',
                                    'class YourClass:\n',
                                    '    pass\n',
                                    '\n']
                                   ]
                                  ]

    def tearDown(self):
        Helper.generate_content_list_from_file = self.org_generate_content_list_from_file
        Helper.generate_content_list_from_db = self.org_generate_content_list_from_db

    def test_generate_content_list(self):
        content_pair_list = Helper.generate_content_list_from_file('D:\Download\installed')
        for content_pair in content_pair_list:
            self.assertEqual(len(content_pair), 2)
            self.assertEqual(type(content_pair), list)
            self.assertEqual(type(content_pair[0]), str)
            self.assertEqual(type(content_pair[1]), list)

    def test_generate_container_list(self):
        content_pair_list = Helper.generate_content_list_from_file('D:\Download\installed')

        container_list = Helper.generate_container_list(content_pair_list)

        self.assertEqual(len(container_list), 3)

        container = container_list[0]
        self.assertEqual(container.file_name, 'D:\Download\installed\calc.py')
        self.assertEqual(container.num_of_class, 2)
        self.assertEqual(container.num_of_line, 26)
        self.assertEqual(container.num_of_method, 4)

        container = container_list[1]
        self.assertEqual(container.file_name, 'D:\Download\installed\HandPy.py')
        self.assertEqual(container.num_of_class, 0)
        self.assertEqual(container.num_of_line, 7)
        self.assertEqual(container.num_of_method, 0)

        container = container_list[2]
        self.assertEqual(container.file_name, 'D:\Download\installed\py_calc_test.py')
        self.assertEqual(container.num_of_class, 1)
        self.assertEqual(container.num_of_line, 10)
        self.assertEqual(container.num_of_method, 1)

    def test_generate_collection_from_file(self):
        self.help_generate_collection('file')

    def test_generate_collection_from_db(self):
        self.help_generate_collection('db')

    def help_generate_collection(self, data_source: str):
        collection = Helper.generate_collection(data_source, 'D:\Download\installed')

        self.assertEqual(collection.get_container(-1), None)

        container = collection.get_container(0)
        self.assertEqual(container.file_name, 'D:\Download\installed\calc.py')
        self.assertEqual(container.num_of_class, 2)
        self.assertEqual(container.num_of_line, 26)
        self.assertEqual(container.num_of_method, 4)

        container = collection.get_container(1)
        self.assertEqual(container.file_name, 'D:\Download\installed\HandPy.py')
        self.assertEqual(container.num_of_class, 0)
        self.assertEqual(container.num_of_line, 7)
        self.assertEqual(container.num_of_method, 0)

        container = collection.get_container(2)
        self.assertEqual(container.file_name, 'D:\Download\installed\py_calc_test.py')
        self.assertEqual(container.num_of_class, 1)
        self.assertEqual(container.num_of_line, 10)
        self.assertEqual(container.num_of_method, 1)

        self.assertEqual(collection.get_container(3), None)

    def test_generate_collection_from_file_with_mock(self):
        self.help_generate_collection_with_mock('file')

    def test_generate_collection_from_db_with_mock(self):
        self.help_generate_collection_with_mock('db')

    def help_generate_collection_with_mock(self, data_source: str):
        if data_source == 'file':
            Helper.generate_content_list_from_file = MagicMock(return_value=self.mock_content_list)
        elif data_source == 'db':
            Helper.generate_content_list_from_db = MagicMock(return_value=self.mock_content_list)

        collection = Helper.generate_collection(data_source, 'mocked pass')

        self.assertEqual(collection.get_container(-1), None)

        container = collection.get_container(0)
        self.assertEqual(container.file_name, 'mocked pass\calc.py')
        self.assertEqual(container.num_of_class, 2)
        self.assertEqual(container.num_of_line, 26)
        self.assertEqual(container.num_of_method, 4)

        container = collection.get_container(1)
        self.assertEqual(container.file_name, 'mocked pass\HandPy.py')
        self.assertEqual(container.num_of_class, 0)
        self.assertEqual(container.num_of_line, 7)
        self.assertEqual(container.num_of_method, 0)

        container = collection.get_container(2)
        self.assertEqual(container.file_name, 'mocked pass\py_calc_test.py')
        self.assertEqual(container.num_of_class, 1)
        self.assertEqual(container.num_of_line, 10)
        self.assertEqual(container.num_of_method, 1)

        self.assertEqual(collection.get_container(3), None)
