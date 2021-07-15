from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=1380, started=False, fuel=45, fuel_consumption=11):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

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
