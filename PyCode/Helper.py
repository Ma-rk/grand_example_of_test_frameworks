import os

import pymysql

from PyCode.FileInfoCollection import FileInfoCollection
from PyCode.FileInfoContainer import FileInfoContainer


class Helper:
    @staticmethod
    def generate_collection(data_source: str, dir_path: str):
        """ FileInfoCollection 객체를 생성하여 리턴

        1. 파일명 list -> 경로+파일명 list -> 파일내용 list
        2. container list
        3. collection

        :param data_source:
        :param dir_path:
        :return: collection
        """

        content_list = ''
        if data_source == 'file':
            content_list = Helper.generate_content_list_from_file(dir_path)
        elif data_source == 'db':
            content_list = Helper.generate_content_list_from_db()
        container_list = Helper.generate_container_list(content_list)
        collection = FileInfoCollection(container_list)

        return collection

    @staticmethod
    def generate_content_list_from_file(dir_path):
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

    @staticmethod
    def generate_content_list_from_db():
        """파일명 list -> 경로+파일명 list -> 파일내용 list

        :param dir_path:
        :return: 파일내용 list
        """

        content_pair_list = []

        conn = pymysql.connect(host='', user='', password='', db='', charset='utf8')
        curs = conn.cursor()
        curs.execute('this is not a qry')
        rows = curs.fetchall()
        print()
        print(rows)
        conn.close()

        return content_pair_list

    @staticmethod
    def generate_container_list(content_list):
        """container list

        :param content_list:
        :return:
        """
        container_list = []
        for content_pair in content_list:
            container = FileInfoContainer(content_pair)
            container_list.append(container)

        return container_list
