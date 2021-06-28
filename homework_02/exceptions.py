"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print('Not enough fuel for going!')

class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass