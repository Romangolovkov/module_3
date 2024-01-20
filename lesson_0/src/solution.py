class Animal:
    def __init__(self, name_animal: str, sound: str) -> None:
        self.name_animal = name_animal
        self.sound = sound
    

    def speak(self) -> str:
        return f'{self.name_animal} говорит {self.sound}'
    

    def eat(self) -> str:
        return f'{self.name_animal} покушала'


dog = Animal('Собака', 'гав-гав')
cat = Animal('Кошка', 'мяу-мяу')
mouse = Animal('Мышь', 'пи-пи')

print(dog.speak())
print(cat.eat())
print(mouse.eat(), mouse.speak())
