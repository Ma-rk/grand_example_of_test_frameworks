from behave import given
from behave import When
from behave import Then

from PyCode.FileInfoContainer import FileInfoContainer


@given('읽어온 파일 내용')
def step_impl(context):
    context.content = ['mocked pass\\calc.py',
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
    assert context.container.num_of_line == 26
    assert context.container.num_of_method == 4
    assert context.container.num_of_class == 2
