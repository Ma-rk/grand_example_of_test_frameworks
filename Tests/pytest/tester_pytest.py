from PyCode.Executor import Executor


class TestClass:
    def setup_method(self):
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
