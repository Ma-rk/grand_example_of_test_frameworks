class FileInfoContainer:
    def __init__(self, content_pair):
        self.file_name = content_pair[0]

        num_of_method = 0
        num_of_class = 0

        for line in content_pair[1]:
            if 'def ' in line:
                num_of_method = num_of_method + 1
            if 'class ' in line:
                num_of_class = num_of_class + 1

        self.num_of_line = len(content_pair[1])
        self.num_of_method = num_of_method
        self.num_of_class = num_of_class

    def get_info(self):
        info = 'file name: %s\n\tline: %s\n\tmethod: %s\n\tclass: %s' \
               % (self.file_name, self.num_of_line, self.num_of_method, self.num_of_class)
        return info
