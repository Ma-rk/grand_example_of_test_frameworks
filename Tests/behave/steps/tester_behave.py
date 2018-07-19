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


@given('Executor 객체, 파일 목록 instance of Executor, list of files')
def step_impl(context):
    context.executor = Executor('D:\Download\installed')
    context.file_full_name_list = ['D:\Download\installed\Anaconda3-5.2.0-Windows-x86_64.exe'
        , 'D:\Download\installed\BANDIZIP-SETUP-KR.EXE'
        , 'D:\Download\installed\calc.feature'
        , 'D:\Download\installed\calc.py'
        , 'D:\Download\installed\cmder_mini.zip'
        , 'D:\Download\installed\DropboxInstaller.exe'
        , 'D:\Download\installed\Git-2.18.0-64-bit.exe'
        , 'D:\Download\installed\GitKrakenSetup.exe'
        , 'D:\Download\installed\HandPy.py'
        , 'D:\Download\installed\KakaoTalk_Setup.exe'
        , 'D:\Download\installed\Monoid-Regular.ttf'
        , 'D:\Download\installed\Monoid-Retina.ttf'
        , 'D:\Download\installed\mRemoteNG-Portable-1.75.7012.16846.zip'
        , 'D:\Download\installed\py_calc_test.py'
        , 'D:\Download\installed\Readme_License.html'
        , 'D:\Download\installed\VSCodeSetup-x64-1.25.0.exe']


@When('파일목록 조회 read the list of files')
def step_impl(context):
    context.executor.get_file_full_name_list()


@Then('주어진 목록과 조회한 목록이 일치 both of given list and actual list are equal')
def step_impl(context):
    given_list = context.file_full_name_list
    actual_list = context.executor.file_full_name_list
    assert given_list == actual_list


@given('1. 파일목록, 2. .py가 아닌 항목 제거한 목록')
def step_impl(context):
    context.executor = Executor('D:\Download\installed')
    context.executor.file_full_name_list = ['D:\Download\installed\Anaconda3-5.2.0-Windows-x86_64.exe'
        , 'D:\Download\installed\BANDIZIP-SETUP-KR.EXE'
        , 'D:\Download\installed\calc.feature'
        , 'D:\Download\installed\calc.py'
        , 'D:\Download\installed\cmder_mini.zip'
        , 'D:\Download\installed\DropboxInstaller.exe'
        , 'D:\Download\installed\Git-2.18.0-64-bit.exe'
        , 'D:\Download\installed\GitKrakenSetup.exe'
        , 'D:\Download\installed\HandPy.py'
        , 'D:\Download\installed\KakaoTalk_Setup.exe'
        , 'D:\Download\installed\Monoid-Regular.ttf'
        , 'D:\Download\installed\Monoid-Retina.ttf'
        , 'D:\Download\installed\mRemoteNG-Portable-1.75.7012.16846.zip'
        , 'D:\Download\installed\py_calc_test.py'
        , 'D:\Download\installed\Readme_License.html'
        , 'D:\Download\installed\VSCodeSetup-x64-1.25.0.exe']
    context.trimmed_list = ['D:\Download\installed\calc.py'
        , 'D:\Download\installed\HandPy.py'
        , 'D:\Download\installed\py_calc_test.py']


@When('파일목록에서 .py가 아닌 항목을 제거했을 때')
def step_impl(context):
    context.executor.remove_not_py_from_list()


@Then('작업한 목록과 주어진 목록이 일치')
def step_impl(context):
    given_list = context.trimmed_list
    trimmed_list = context.executor.file_full_name_list
    assert given_list == trimmed_list
