import os


class Helper:
    @staticmethod
    def generate_content_list(dir_path):
        """파일명 list -> 경로+파일명 list -> 파일내용 list

        :param dir_path:
        :return: 파일내용 list
        """
        file_name_list = os.listdir(dir_path)

        full_file_name_list = []
        for file_name in file_name_list:
            if not file_name.endswith('.py'):
                continue

            full_file_name = os.path.join(dir_path, file_name)
            full_file_name_list.append(full_file_name)

        content_pair_list = []
        for full_file_name in full_file_name_list:
            with open(full_file_name, 'r') as f:
                content = f.readlines()
                content_pair_list.append([full_file_name, content])

        return content_pair_list
