"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if number + self.cargo > self.max_cargo:
            raise CargoOverload('Error: cargo overload!')
        else:
            self.cargo += number
            print(f'Plane.cargo after plus with number = {self.cargo}')

    def remove_all_cargo(self):
        if self.cargo == 0:
            return self.cargo
        else:
            tmp = self.cargo
            self.cargo = 0
        return tmp
