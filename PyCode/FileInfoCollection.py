class FileInfoCollection:
    def __init__(self, file_info_container_list):
        self.file_info_container_list = file_info_container_list

    def get_container(self, idx):
        if idx < 0:
            return None  # todo: 익셉션 IndexError 를 처리하도록 변경
        if len(self.file_info_container_list) <= idx:
            return None  # todo: 익셉션 IndexError 를 처리하도록 변경

        return self.file_info_container_list[idx]

    def display_collection_info(self):
        for file_info_container in self.file_info_container_list:
            print(file_info_container.get_info())
