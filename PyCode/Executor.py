import os


class Executor:
    def __init__(self, dir_path: str):
        self.file_full_name_list = []

        self.dir_path = dir_path

    def get_file_full_name_list(self):
        print('... get_file_full_name_list')
        file_name_list = os.listdir(self.dir_path)

        for file_name in file_name_list:
            full_file_name = os.path.join(self.dir_path, file_name)
            self.file_full_name_list.append(full_file_name)

    def display_all_file_name(self):
        print('... display_all_file_name')
        for file_name in self.file_full_name_list:
            print(file_name)
