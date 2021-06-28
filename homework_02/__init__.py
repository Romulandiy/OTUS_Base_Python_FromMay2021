"""
Домашнее задание №2
Классы и модули
"""
# from . import base, car, engine, exceptions, plane
# from . Vehicle import Vehicle
from homework_02.base.Vehicle import Vehicle

# __all__ = [
#     "base",
#     "car",
#     "engine",
#     "exceptions",
#     "plane",
# ]


# Example # 1 ----------------------------------------
vehicle_1 = Vehicle(weight=1380,
                    started=False,
                    fuel=50,
                    fuel_consumption=12.7)

if __name__ == '__main__':
    start()
