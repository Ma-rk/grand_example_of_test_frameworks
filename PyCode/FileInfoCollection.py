import os


class FileInfoCollection:
    def get_file_full_name_list(self, dir_path):
        file_name_list = os.listdir(dir_path)
        full_file_name_list = []

        for file_name in file_name_list:
            if not file_name.endswith('.py'):
                continue

            full_file_name = os.path.join(dir_path, file_name)
            full_file_name_list.append(full_file_name)

        return full_file_name_list
