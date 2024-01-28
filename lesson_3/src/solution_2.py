class Greenhouse:
    def __init__(self, temp: int, humidity: int, light_level: int) -> None:
        self.__temp = temp
        self.__humidity = humidity
        self.__light_level = light_level

    def get_temp(self) -> int:
        return self.__temp
    
    def get_humidity(self) -> int:
        return self.__humidity
    
    def get_light_level(self) -> int:
        return self.__light_level
    
    def set_temp(self, temp: int) -> None:
        if 15 <= temp <= 30:
            self.__temp = temp
        else:
            raise ValueError('Температура должна быть от 15 до 30 градусов')
    
    def set_humidity(self, humidity: int) -> None:
        if 0 <= humidity <= 100:
            self.__humidity = humidity
        else:
            raise ValueError('Влажность не может быть ниже 0 или выше 100 %')
            
    def set_light_level(self, light_level: int) -> None:
        if light_level > 0:
            self.__light_level = light_level
        else:
            raise ValueError('Освещенность не может быть отрицательной')
        
greenhouse = Greenhouse(20, 80, 200)
greenhouse.set_temp(25)
greenhouse.set_humidity(100)
greenhouse.set_light_level(350)

print(f'температура: {greenhouse.get_temp()} градусов\
      \nвлажность: {greenhouse.get_humidity()} %\
      \nосвещенность: {greenhouse.get_light_level()} Лк\
      ')
