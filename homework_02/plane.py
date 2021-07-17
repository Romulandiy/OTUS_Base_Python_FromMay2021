"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 250
    # max_cargo = 7900

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo
        super().__init__()

    def load_cargo(self, number):
        try:
            if number + Plane.cargo > self.max_cargo:
                raise CargoOverload
            else:
                Plane.cargo += number
                print(f'Plane.cargo after plus with number = {Plane.cargo}')
        except CargoOverload:
            print('Raised an exception from def load_cargo')
            CargoOverload.car_go_overload()

    def remove_all_cargo(self):
        if Plane.cargo == 0:
            return Plane.cargo
        else:
            tmp = Plane.cargo
            Plane.cargo = 0
        return tmp
