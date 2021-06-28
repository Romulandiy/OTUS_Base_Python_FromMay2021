from abc import ABC
from dataclasses import dataclass

from homework_02.exceptions import LowFuelError


@dataclass
class Vehicle(ABC):
    weight: int = 1380
    started: bool = False
    fuel: int = 50
    fuel_consumption: float = 12.7

    # @staticmethod
    def start(self):
        try:
            if self.fuel > 0:
                self.started = True

        except Exception:
            print("Raised an exception", "\n")


