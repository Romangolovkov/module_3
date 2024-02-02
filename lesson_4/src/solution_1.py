from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class Guitar(Instrument):
    def play(self) -> None:
        print('Звук гитары')

class Piano(Instrument):
    def play(self) -> None:
        print('Звук пианино')

class Flute(Instrument):
    def play(self) -> None:
        print('Звук флейты')

instruments: list[Instrument] = [Guitar(), Piano(), Flute()]

for instrument in instruments:
    instrument.play()