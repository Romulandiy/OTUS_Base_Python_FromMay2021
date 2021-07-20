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
        if number + Plane.cargo > self.max_cargo:
            raise CargoOverload('error car')
        else:
            Plane.cargo += number
            print(f'Plane.cargo after plus with number = {Plane.cargo}')

    def remove_all_cargo(self):
        if Plane.cargo == 0:
            return Plane.cargo
        else:
            tmp = Plane.cargo
            Plane.cargo = 0
        return tmp
