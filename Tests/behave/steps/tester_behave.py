from unittest.mock import MagicMock

from behave import given
from behave import When
from behave import Then

from PyCode.FileInfoCollection import FileInfoCollection
from PyCode.FileInfoContainer import FileInfoContainer
from PyCode.Helper import Helper


@given('읽어온 파일 내용')
def step_impl(context):
    context.content = ['dummy pass\\calc.py',
                       ['class Calc1:\n',
                        '    def add(self, num_a, num_b:\n',
                        '        """\n',
                        '\n',
                        '        :param num_a: 1st no\n',
                        '        :param num_b: 2nd no\n',
                        '        :return: sum of two numbers\n',
                        '        """\n',
                        '        num_result = num_a+num_b\n',
                        '        return num_result\n',
                        '\n',
                        '    def subtract(self, num_a, num_b:\n',
                        '        num_result = num_a-num_b\n',
                        '        return num_result\n',
                        '\n',
                        '\n',
                        'class Calc2:\n',
                        '    def multiply(self, num_a, num_b:\n',
                        '        num_result = num_a*num_b\n',
                        '        return num_result\n',
                        '\n',
                        '    def divide(self, num_a, num_b:\n',
                        '        num_result = num_a/num_b\n',
                        '        return num_result\n',
                        '\n',
                        '\n']
                       ]


@When('읽어온 content 로 FileInfoContainer 객체를 생성하면')
def step_impl(context):
    context.container = FileInfoContainer(context.content)


@Then('line: 26 method: 4 class: 2')
def step_impl(context):
    assert context.container.file_name == 'dummy pass\\calc.py'
    assert context.container.num_of_line == 26
    assert context.container.num_of_method == 4
    assert context.container.num_of_class == 2


@given('읽어온 폴더 내용')
def step_impl(context):
    context.content_list = [['mocked pass\\calc.py',
                             ['class Calc1:\n',
                              '    def add(self== num_a== num_b):\n',
                              '        """\n',
                              '\n',
                              '        :param num_a: 1st no\n',
                              '        :param num_b: 2nd no\n',
                              '        :return: sum of two numbers\n',
                              '        """\n',
                              '        num_result = num_a+num_b\n',
                              '        return num_result\n',
                              '\n',
                              '    def subtract(self== num_a== num_b):\n',
                              '        num_result = num_a-num_b\n',
                              '        return num_result\n',
                              '\n',
                              '\n',
                              'class Calc2:\n',
                              '    def multiply(self== num_a== num_b):\n',
                              '        num_result = num_a*num_b\n',
                              '        return num_result\n',
                              '\n',
                              '    def divide(self== num_a== num_b):\n',
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
                              '    assert ut_calc1.add(4== 6) == 10\n',
                              '\n',
                              'class YourClass:\n',
                              '    pass\n',
                              '\n']
                             ]
                            ]


@When('읽어온 content_list 로 FileInfoCollection 객체를 생성하면')
def step_impl(context):
    container_list = Helper.generate_container_list(context.content_list)
    context.collection = FileInfoCollection(container_list)


@Then('2, 26, 4, 0, 7, 0, 1, 10, 1')
def step_impl(context):
    assert context.collection.get_container(-1) is None

    container = context.collection.get_container(0)
    assert container.file_name == 'mocked pass\calc.py'
    assert container.num_of_class == 2
    assert container.num_of_line == 26
    assert container.num_of_method == 4

    container = context.collection.get_container(1)
    assert container.file_name == 'mocked pass\HandPy.py'
    assert container.num_of_class == 0
    assert container.num_of_line == 7
    assert container.num_of_method == 0

    container = context.collection.get_container(2)
    assert container.file_name == 'mocked pass\py_calc_test.py'
    assert container.num_of_class == 1
    assert container.num_of_line == 10
    assert container.num_of_method == 1

    assert context.collection.get_container(3) is None


@given('generate_container_list 를 모킹 for file')
def step_impl(context):
    Helper.generate_content_list_from_file = MagicMock(return_value=[['mocked pass\\calc.py',
                                                                      ['class Calc1:\n',
                                                                       '    def add(self== num_a== num_b):\n',
                                                                       '        """\n',
                                                                       '\n',
                                                                       '        :param num_a: 1st no\n',
                                                                       '        :param num_b: 2nd no\n',
                                                                       '        :return: sum of two numbers\n',
                                                                       '        """\n',
                                                                       '        num_result = num_a+num_b\n',
                                                                       '        return num_result\n',
                                                                       '\n',
                                                                       '    def subtract(self== num_a== num_b):\n',
                                                                       '        num_result = num_a-num_b\n',
                                                                       '        return num_result\n',
                                                                       '\n',
                                                                       '\n',
                                                                       'class Calc2:\n',
                                                                       '    def multiply(self== num_a== num_b):\n',
                                                                       '        num_result = num_a*num_b\n',
                                                                       '        return num_result\n',
                                                                       '\n',
                                                                       '    def divide(self== num_a== num_b):\n',
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
                                                                       '    assert ut_calc1.add(4== 6) == 10\n',
                                                                       '\n',
                                                                       'class YourClass:\n',
                                                                       '    pass\n',
                                                                       '\n']
                                                                      ]
                                                                     ])


@When('모킹한 데이터로 FileInfoCollection 객체를 생성하면 for file')
def step_impl(context):
    context.collection = Helper.generate_collection('file', '')


@given('generate_container_list 를 모킹 for db')
def step_impl(context):
    Helper.generate_content_list_from_db = MagicMock(return_value=[['mocked pass\\calc.py',
                                                                    ['class Calc1:\n',
                                                                     '    def add(self== num_a== num_b):\n',
                                                                     '        """\n',
                                                                     '\n',
                                                                     '        :param num_a: 1st no\n',
                                                                     '        :param num_b: 2nd no\n',
                                                                     '        :return: sum of two numbers\n',
                                                                     '        """\n',
                                                                     '        num_result = num_a+num_b\n',
                                                                     '        return num_result\n',
                                                                     '\n',
                                                                     '    def subtract(self== num_a== num_b):\n',
                                                                     '        num_result = num_a-num_b\n',
                                                                     '        return num_result\n',
                                                                     '\n',
                                                                     '\n',
                                                                     'class Calc2:\n',
                                                                     '    def multiply(self== num_a== num_b):\n',
                                                                     '        num_result = num_a*num_b\n',
                                                                     '        return num_result\n',
                                                                     '\n',
                                                                     '    def divide(self== num_a== num_b):\n',
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
                                                                     '    assert ut_calc1.add(4== 6) == 10\n',
                                                                     '\n',
                                                                     'class YourClass:\n',
                                                                     '    pass\n',
                                                                     '\n']
                                                                    ]
                                                                   ])


@When('모킹한 데이터로 FileInfoCollection 객체를 생성하면 for db')
def step_impl(context):
    context.collection = Helper.generate_collection('db', '')
