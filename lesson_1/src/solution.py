class Library:
    def __init__(self) -> None:
        self.books: list[tuple[str, str]] = []
            

    def add_book(self, name: str, author: str):
        self.books.append((name, author))
        return self


    def remove_book(self, name: str):
        for book in self.books:
            if book[0] == name:
                self.books.remove(book)
        return self


    def __getitem__(self, index: int) -> tuple[str, str]:
        return self.books[index]

        
    def __contains__(self, name_book) -> bool:
        return bool([book for book in self.books if book[0] == name_book])


library = Library()

library.add_book('Мёртвые души', 'Н.В. Гоголь').remove_book('Мёртвые души').add_book(
    'Евгений Онегин', 'А.С. Пушкин').add_book('Война и мир', 'Л.Н. Толстой')

print(library[-1])
print('Евгений Онегин' in library)
print('Преступление и наказание' in library)