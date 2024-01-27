class Person:
    population: int = 0


    def __str__(self) -> str:
        return f'{self.name}, {self.age} лет'


    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.population += 1


    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, 2023 - birth_year)
    

    @classmethod
    def display_population(cls) -> None:
        print(f'Текущая популяция: {Person.population} человек(а)')


person1 = Person.from_birth_year('Роман', 1991)
person2 = Person('Дмитрий', 20)
person3 = Person('Анна', 25)
person4 = Person.from_birth_year('Алина', 1995)

Person.display_population()
        
    

