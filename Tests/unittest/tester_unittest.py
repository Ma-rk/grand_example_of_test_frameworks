import unittest

from PyCode.Executor import Executor
from PyCode.FileInfoContainer import FileInfoContainer


class TesterUnittest(unittest.TestCase):
    def setUp(self):
        self.executor = Executor('D:\Download\installed')
        self.file_full_name_list = ['D:\Download\installed\Anaconda3-5.2.0-Windows-x86_64.exe'
            , 'D:\Download\installed\BANDIZIP-SETUP-KR.EXE'
            , 'D:\Download\installed\calc.feature'
            , 'D:\Download\installed\calc.py'
            , 'D:\Download\installed\cmder_mini.zip'
            , 'D:\Download\installed\DropboxInstaller.exe'
            , 'D:\Download\installed\Git-2.18.0-64-bit.exe'
            , 'D:\Download\installed\GitKrakenSetup.exe'
            , 'D:\Download\installed\HandPy.py'
            , 'D:\Download\installed\KakaoTalk_Setup.exe'
            , 'D:\Download\installed\Monoid-Regular.ttf'
            , 'D:\Download\installed\Monoid-Retina.ttf'
            , 'D:\Download\installed\mRemoteNG-Portable-1.75.7012.16846.zip'
            , 'D:\Download\installed\py_calc_test.py'
            , 'D:\Download\installed\Readme_License.html'
            , 'D:\Download\installed\VSCodeSetup-x64-1.25.0.exe']
        self.trimmed_list = ['D:\Download\installed\calc.py'
            , 'D:\Download\installed\HandPy.py'
            , 'D:\Download\installed\py_calc_test.py']

    def test_get_file_full_name_list(self):
        self.executor.get_file_full_name_list()
        self.assertEqual(len(self.file_full_name_list), len(self.executor.file_full_name_list))

        for i in range(len(self.file_full_name_list)):
            self.assertEqual(self.file_full_name_list[i], self.executor.file_full_name_list[i])

    def test_remove_not_py_from_list(self):
        self.executor.file_full_name_list = self.file_full_name_list
        self.executor.remove_not_py_from_list()

        self.assertEqual(len(self.trimmed_list), len(self.executor.file_full_name_list))

        for i in range(len(self.trimmed_list)):
            self.assertEqual(self.trimmed_list[i], self.executor.file_full_name_list[i])

    def test_initialize_file_info_container_instance(self):
        container = FileInfoContainer('D:\Download\installed\py_calc_test.py')
        assert container.num_of_line == 9
        assert container.num_of_method == 1
        assert container.num_of_class == 0
