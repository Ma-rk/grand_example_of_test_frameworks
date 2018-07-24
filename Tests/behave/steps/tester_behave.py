from behave import given
from behave import When
from behave import Then

from PyCode.FileInfoCollection import FileInfoCollection
from PyCode.FileInfoContainer import FileInfoContainer


@given('파일명 D Download installed calc.py')
def step_impl(context):
    context.full_file_path = 'D:\Download\installed\calc.py'


@When('D Download installed calc.py 로 FileInfoContainer 객체를 생성하면')
def step_impl(context):
    context.container = FileInfoContainer(context.full_file_path)


@Then('line: 26 method: 4 class: 2')
def step_impl(context):
    assert context.container.num_of_line == 26
    assert context.container.num_of_method == 4
    assert context.container.num_of_class == 2


@given('경로 D Download installed')
def step_impl(context):
    context.dir_path = 'D:\Download\installed'


@When('D Download installed 로 FileInfoCollection 객체를 생성하면')
def step_impl(context):
    context.collection = FileInfoCollection(context.dir_path)


@Then('26/4/2 7/0/0 10/1/1')
def step_impl(context):
    container = context.collection.get(0)
    assert container.num_of_line == 26
    assert container.num_of_method == 4
    assert container.num_of_class == 2

    container = context.collection.get(1)
    assert container.num_of_line == 7
    assert container.num_of_method == 0
    assert container.num_of_class == 0

    container = context.collection.get(2)
    assert container.num_of_line == 10
    assert container.num_of_method == 1
    assert container.num_of_class == 1
