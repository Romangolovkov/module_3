from datetime import datetime

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, datetime.now().year - birth_year)
    

    def __str__(self) -> str:
        return f'{self.name}, {self.age} лет'


person = Person.from_birth_year('Роман', 1991)
print(person)