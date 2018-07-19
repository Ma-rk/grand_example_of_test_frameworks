from behave import *

from PyCode.Executor import Executor


@given('argument is "D Download installed" 인수는 "D Download installed"')
def step_impl(context):
    context.dir_path = 'D:\Download\installed'


@When('pass "D Download installed"')
def step_impl(context):
    context.executor = Executor(context.dir_path)


@Then('executor.dir_path is "D Download installed"')
def step_impl(context):
    assert context.executor.dir_path == context.dir_path
