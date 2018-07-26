import sys
from PyCode.Helper import Helper


def execute(command_line_arg: str):
    collection = Helper.generate_collection(command_line_arg)
    collection.display_collection_info()


if __name__ == '__main__':
    if sys.argv.__len__() is 1:
        print('no argument. quit.')
    if 2 < sys.argv.__len__():
        print('too many argument. quit.')
    else:
        print('... LAUNCH')
        execute(sys.argv[1])
