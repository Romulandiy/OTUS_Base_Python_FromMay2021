"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo, max_cargo):
        # super().__init__()

        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        try:
            if number + self.cargo > self.max_cargo:
                raise CargoOverload
            else:
                self.cargo += number
                print(f'cargo after plus with number = {self.cargo}')
        except CargoOverload:
            print('Raised an exception from def load_cargo')
            CargoOverload.car_go_overload()

    def remove_all_cargo(self):
        if self.cargo == 0:
            return self.cargo
        else:
            tmp = self.cargo
            self.cargo = 0
        return tmp
