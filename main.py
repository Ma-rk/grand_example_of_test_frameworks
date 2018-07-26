import sys
from PyCode.Helper import Helper


def execute(data_source: str, dir_path: str):
    collection = Helper.generate_collection(data_source, dir_path)
    collection.display_collection_info()


if __name__ == '__main__':
    if sys.argv.__len__() < 3:
        print('no argument. quit.')
    if 3 < sys.argv.__len__():
        print('too many argument. quit.')
    else:
        print('... LAUNCH')
        execute(sys.argv[1], sys.argv[2])
