class Library:
    books = []
    def __init__(self, name: str, author: str):
        
        
        self.book = (name, author)    

    def add_book(self):
        self.books.append(self.book)
        
    




        
        
    
        
    

book1 = Library('red', 'toyota')


book1.add_book()
print(Library.books)
