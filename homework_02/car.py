"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle


class Car(Vehicle):

    # def __init__(self, engine):
    #     engine

        # super().__init__()
        # self.engine = engine

    def set_engine(self, engine):
        self.engine = engine
        # print(self.engine)
