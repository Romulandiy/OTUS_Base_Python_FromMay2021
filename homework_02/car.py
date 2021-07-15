"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, engine):
        # super().__init__(self)
        self.engine = engine

    def set_engine(self, engine):
        return self.engine
