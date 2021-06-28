from abc import ABC
# from abc import ABC, abstractmethod
from dataclasses import dataclass

from homework_02.exceptions.LowFuelError import LowFuelError
from LowFuelError import LowFuelError


@dataclass
class Vehicle(ABC):
    weight: int = 1380
    started: bool = False
    fuel: int = 50
    fuel_consumption: int = 12.7

    @staticmethod
    def start(fuel, started):
        try:
            if fuel <= 0:
                raise Exception(exceptions.LowFuelError())
        except Exception:
            print("Raised an exception", "\n")
        else:
            started = True
