class Book:
    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author
    

    def __str__(self) -> str:
        return f'"{self.name}", {self.author}'
    

class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []


    def library_list(self) -> list[str]:
        return [book.__str__() for book in self.books]

    
    def add_book(self, book) -> 'Library':
        self.books.append(book)
        return self


    def remove_book(self, name_book: str) -> 'Library':
        for book in self.books:
            if book.name == name_book:
                self.books.remove(book)
        return self


    def __getitem__(self, index: int) -> str:
        return self.books[index].__str__()

        
    def __contains__(self, name_book) -> bool:
        return bool([book for book in self.books if book.name == name_book])


library: Library = Library()

book1 = Book('Мёртвые души', 'Н.В. Гоголь')
book2 = Book('Евгений Онегин', 'А.С. Пушкин')
book3 = Book('Война и мир', 'Л.Н. Толстой')

library.add_book(book1).remove_book(book1).add_book(
    book2).add_book(book3)

print(library[-1])
print('Евгений Онегин' in library)
print('Преступление и наказание' in library)
print(library.library_list())