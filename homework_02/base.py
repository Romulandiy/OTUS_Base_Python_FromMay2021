from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=900, fuel=23, fuel_consumption=14):

        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        try:
            if self.fuel > 0:
                self.started = True
                print(f'self.started = {self.started}')
        except LowFuelError:
            raise LowFuelError.low_fuel_error()

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
