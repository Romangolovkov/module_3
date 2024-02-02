class Fountain:
    def spray_water(self) -> None:
        pass

class SimpleFountain:
    def spray_water(self) -> None:
        print('Это обычный фонтан')

class MusicalFountain:
    def spray_water(self) -> None:
        print('Это музыкальный фонтан')

class LightedFountain:
    def spray_water(self) -> None:
        print('Это освещённый фонтан', self.__class__.__name__)

fountains: list[Fountain] = [SimpleFountain(), MusicalFountain(), LightedFountain()]

for fountain in fountains:
    fountain.spray_water()