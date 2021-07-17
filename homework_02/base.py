from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):

        started = False
        self.weight = 1380
        self.fuel = 45
        self.fuel_consumption = 11

    def start(self):
        try:
            if self.fuel <= 0:
                raise LowFuelError
            else:
                started = True
                print(f'started = {started}')
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
