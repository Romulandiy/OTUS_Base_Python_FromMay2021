from homework_02.base import Vehicle
from homework_02.car import Car
from homework_02.engine import Engine
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload
from homework_02.plane import Plane

# ---- Task # 1_1 ----:
vehicle_1_1 = Vehicle(fuel=0, fuel_consumption=17, weight=1500)

# ---- Task # 1_2 ----:
vehicle_1_2 = Vehicle(fuel=20, fuel_consumption=17, weight=1500)

# ---- Task # 1_3 ----:
vehicle_1_3 = Vehicle(fuel=50, fuel_consumption=15, weight=2100)

# ---- Task # 1_4 ----:
vehicle_1_4 = Vehicle(fuel=50, fuel_consumption=11, weight=2450)

# ---- Task # 2_1 ----:'
engine_example_1 = Engine(volume=2.5, pistons=6)
car_2_1 = Car()

# ---- Task # 3_1, 3_2, 3_3 ----:'
plane_1 = Plane(weight=1100, fuel=20, fuel_consumption=13, max_cargo=3000)

if __name__ == '__main__':
    print('---- Task # 1_1 ----:')
    try:
        vehicle_1_1.start()
    except LowFuelError as e:
        print(e)


    print('\n---- Task # 1_2 ----:')
    vehicle_1_2.start()

    print('\n---- Task # 1_3 ----:')
    try:
        vehicle_1_3.move(dist=300)
    except NotEnoughFuel as e:
        print(e)

    print('\n---- Task # 1_4 ----:')
    try:
        vehicle_1_4.move(dist=750)
    except NotEnoughFuel as e:
        print(e)

    print('\n---- Task # 2_1 ----:')
    print(car_2_1.set_engine(engine=engine_example_1))

    print('\n---- Task # 3_1 ----:')
    try:
        print(plane_1.load_cargo(number=3100))
    except CargoOverload as e:
        print(e)

    print('\n---- Task # 3_2 ----:')
    print(plane_1.load_cargo(number=800))

    print('\n---- Task # 3_3 ----:')
    print(plane_1.remove_all_cargo())

