from abc import ABC
from dataclasses import dataclass
from homework_02.exceptions import LowFuelError, NotEnoughFuel


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
            print('Raised an exception from def start')
            LowFuelError.low_fuel_error()

    def move(self, dist):
        try:
            if self.fuel - dist / 100 * self.fuel_consumption < 0:
                raise NotEnoughFuel
            else:
                self.fuel = self.fuel - dist / 100 * self.fuel_consumption
                print(f'fuel after changed = {self.fuel}')
        except NotEnoughFuel:
            print('Raised an exception from def move')
            NotEnoughFuel.not_enough_fuel()
