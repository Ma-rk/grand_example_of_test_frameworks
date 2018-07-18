import sys


def execute(command_line_arg: str):
    print(command_line_arg)


if __name__ == '__main__':
    if sys.argv.__len__() is 1:
        print('no argument. quit.')
    if 2 < sys.argv.__len__():
        print('too many argument. quit.')
    else:
        execute(sys.argv[1])
