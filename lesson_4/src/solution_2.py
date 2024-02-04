import pickle

class FileHandler:
    def read(self) -> None:
        pass

    def write(self) -> None:
        pass

class TextFileHandler(FileHandler):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        
    def read(self) -> str:
        file = open('src/' + self.file_name)
        text = file.read()
        file.close()    
        return text

    def write(self, data: str) -> None:
        file = open('src/' + self.file_name, 'w+')
        file.write(data)
        file.close()
        print(f"Текстовый файл {self.file_name} был записан! \nТекст файла: '{self.read()}'")
        
class BinaryFileHandler(FileHandler):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        
    def read(self) -> str:
        file = open('src/' + self.file_name, 'rb')
        bin = file.read()
        file.close()
        return bin

    def write(self, data: str) -> None:
        file = open('src/' + self.file_name, 'wb+')
        pickle.dump(data, file)
        file.close()
        print(f"Бинарный файл {self.file_name} был записан! \nСодержимое файла: '{self.read()}'")

def save_data(handler: FileHandler, data: str) -> None:
    handler.write(data)

text_file = TextFileHandler('Text_file.txt')
binary_file = BinaryFileHandler('Binary_file.bin')

print()
save_data(text_file, 'Hello, World!')
print()
save_data(binary_file, 'Привет, Мир!')
print()
