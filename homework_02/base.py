from abc import ABC
from dataclasses import dataclass
from homework_02.exceptions import LowFuelError


@dataclass
class Vehicle(ABC):
    weight: int = 1380
    started: bool = False
    fuel: int = 45
    fuel_consumption: float = 12.7

    def start(self):
        try:
            if self.fuel <= 0:
                raise LowFuelError
            else:
                self.started = True
                print(f'started = {self.started}')
        except LowFuelError:
            print('Raised an exception')
            LowFuelError.low_fuel_error()
