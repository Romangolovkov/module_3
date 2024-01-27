class Temperature:
    def __init__(self) -> None:
        pass


    @staticmethod
    def celsius_to_fahrenheit(temp_celsius: float) -> float:
        return temp_celsius * 9 / 5 + 32
    

    @staticmethod
    def fahrenheit_to_celsius(temp_fahrenheit: float) -> float:
        return (temp_fahrenheit - 32) * 5 / 9
    

print(f'16 градусов Цельсия равно {Temperature.celsius_to_fahrenheit(16):.1f} градусов Фаренгейта')
print(f'0 градусов Цельсия равно {Temperature.fahrenheit_to_celsius(0):.1f} градусов Фаренгейта')