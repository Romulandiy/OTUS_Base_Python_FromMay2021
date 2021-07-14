"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, engine):
        self.engine = engine

    def __add__(self, other):
        return self.fuel + self.started + self.fuel_consumption + self.weight + other.volume + other.pistons

    def set_engine(self, engine):
        return self + engine
