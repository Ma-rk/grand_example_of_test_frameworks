import sys

from PyCode.Executor import Executor


def execute(command_line_arg: str):
    executor = Executor(command_line_arg)
    executor.get_file_full_name_list()
    executor.display_all_file_name()


if __name__ == '__main__':
    if sys.argv.__len__() is 1:
        print('no argument. quit.')
    if 2 < sys.argv.__len__():
        print('too many argument. quit.')
    else:
        print('... LAUNCH')
        execute(sys.argv[1])
