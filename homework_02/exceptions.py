"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):

    @staticmethod
    def low_fuel_error():
        print('Low fuel error!')


class NotEnoughFuel(Exception):

    @staticmethod
    def not_enough_fuel():
        print('Not enough fuel!')


class CargoOverload(Exception):

    @staticmethod
    def car_go_overload():
        print('Car go overload!')
