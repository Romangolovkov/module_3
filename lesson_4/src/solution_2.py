import pickle

class FileHandler:
    def read(self) -> None:
        pass

    def write(self) -> None:
        pass

class TextFileHandler(FileHandler):
    def __init__(self, file_name: str) -> None:
        if file_name[-4:] == '.txt':
            self.file_name = file_name
        else:
            print('Разрешение файла должно быть ".txt"')

    def read(self) -> None:
        file = open('src/' + self.file_name)
        text = file.read()
        file.close()    
        return text

    def write(self, data: str):
        file = open('src/' + self.file_name, 'w+')
        file.write(data)
        file.close()
        print(f"Текстовый файл {self.file_name} был записан! \nТекст файла: '{self.read()}'")
        
class BinaryFileHandler(FileHandler):
    def __init__(self, file_name: str) -> None:
        if file_name[-4:] == '.bin':
            self.file_name = file_name
        else:
            print('Разрешение файла должно быть ".bin"')

    def read(self) -> None:
        file = open('src/' + self.file_name, 'rb')
        bin = file.read()
        file.close()
        return bin

    def write(self, data: str):
        file = open('src/' + self.file_name, 'wb+')
        pickle.dump(data, file)
        file.close()
        print(f"Бинарный файл {self.file_name} был записан! \nСодержимое файла: '{self.read()}'")

print()
text_file = TextFileHandler('Text_file.txt')
text_file.write('Hello, World!')

print()
binary_file_handler = BinaryFileHandler('Binary_file.bin')
binary_file_handler.write('Привет, Мир!')
print()
