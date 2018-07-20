class FileInfoContainer:
    def __init__(self, file_name):
        self.file_name = file_name

        f = open(file_name, 'r')
        content = f.readlines()

        num_of_method = 0
        num_of_class = 0

        for line in content:
            if 'def ' in line:
                num_of_method = num_of_method + 1
            if 'class ' in line:
                num_of_class = num_of_class + 1

        self.num_of_line = len(content)
        self.num_of_method = num_of_method
        self.num_of_class = num_of_class
