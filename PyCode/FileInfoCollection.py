import os

from PyCode.FileInfoContainer import FileInfoContainer


class FileInfoCollection:
    def __init__(self, dir_path):

        full_file_name_list = self._get_file_full_name_list(dir_path)
        self.file_info_container_list = self._get_file_container_collection(full_file_name_list)

    def _get_file_full_name_list(self, dir_path):
        file_name_list = os.listdir(dir_path)
        full_file_name_list = []

        for file_name in file_name_list:
            if not file_name.endswith('.py'):
                continue

            full_file_name = os.path.join(dir_path, file_name)
            full_file_name_list.append(full_file_name)

        return full_file_name_list

    def _get_file_container_collection(self, full_file_name_list):
        file_info_container_list = []

        for full_file_name in full_file_name_list:
            container = FileInfoContainer(full_file_name)
            file_info_container_list.append(container)

        return file_info_container_list

    def get(self, idx):
        if idx < 0:
            return None  # todo: 익셉션 IndexError 를 처리하도록 변경
        if len(self.file_info_container_list) <= idx:
            return None  # todo: 익셉션 IndexError 를 처리하도록 변경

        return self.file_info_container_list[idx]

    def display_collection_info(self):
        for file_info_container in self.file_info_container_list:
            print(file_info_container.get_info())
