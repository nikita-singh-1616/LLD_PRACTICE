# follows a tree like structure
# consists of two types of nodes leaf node or composite node
# Example File System

class FileSystemInterface:
    def ls(self):
        pass


class File(FileSystemInterface):
    def __init__(self, name):
        self.file_name = name

    def ls(self):
        print(f'filename -{self.file_name}')


class Directory(FileSystemInterface):
    def __init__(self, name):
        self.folder_name = name
        self.folder_contents = []

    def set_folder_content(self, content):
        self.folder_contents.append(content)
        print('content added successfully')

    def ls(self):
        print(f'Folder Name- {self.folder_name}')
        for i in self.folder_contents:
            i.ls()


class FileSystemImplementation:
    def __init__(self):
        main = Directory('Main ')
        file_A = File('file_A')
        folder_A = Directory('FOLDER_A')
        main.set_folder_content(file_A)
        main.set_folder_content(folder_A)
        file_B = File('file_B')
        file_C = File('file_c')
        folder_A.set_folder_content(file_B)
        folder_A.set_folder_content(file_C)
        main.ls()


FileSystemImplementation()
