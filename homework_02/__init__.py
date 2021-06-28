"""
Домашнее задание №2
Классы и модули
"""
# from . import base, car, engine, exceptions, plane
from homework_02.base import Vehicle

# __all__ = [
#     "base",
#     "car",
#     "engine",
#     "exceptions",
#     "plane",
# ]


# Example # 1 ----------------------------------------
vehicle_1 = Vehicle(fuel=0)

if __name__ == '__main__':
    vehicle_1.start()
