from PyCode.FileInfoContainer import FileInfoContainer
from PyCode.FileInfoCollection import FileInfoCollection


class TestClass:
    def test_container(self):
        container = FileInfoContainer('D:\Download\installed\calc.py')

        assert container.num_of_line == 26
        assert container.num_of_method == 4
        assert container.num_of_class == 2

        container_info = container.get_info()
        assert container_info == 'file name: D:\Download\installed\calc.py\n\tline: 26\n\tmethod: 4\n\tclass: 2'

    def test_collection(self):
        collection = FileInfoCollection('D:\Download\installed')

        container = collection.get(-1)
        assert container is None

        container = collection.get(0)
        assert container.num_of_line == 26
        assert container.num_of_method == 4
        assert container.num_of_class == 2

        container = collection.get(1)
        assert container.num_of_line == 7
        assert container.num_of_method == 0
        assert container.num_of_class == 0

        container = collection.get(2)
        assert container.num_of_line == 10
        assert container.num_of_method == 1
        assert container.num_of_class == 1

        container = collection.get(3)
        assert container is None
