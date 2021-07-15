"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):

    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        super().__init__(max_cargo)

    def load_cargo(self, number):
        try:
            if number + self.cargo > max_cargo:
                raise NotEnoughFuel
            else:
                self.fuel = self.fuel - dist / 100 * self.fuel_consumption
                print(f'fuel after changed = {self.fuel}')
        except NotEnoughFuel:
            print('Raised an exception from def move')
            NotEnoughFuel.not_enough_fuel()

