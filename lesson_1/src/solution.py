class Car:
    def __init__(self, color: str, brand: str, hp: int):
        self.color = color
        self.brand = brand
        self.hp = hp
    

    
    

car1 = Car('', '', 200)
car2 = Car('', '', 200)
car3 = Car('', '', 250)


print(car1.hp == car2.hp)
print(car1.hp == car3.hp)