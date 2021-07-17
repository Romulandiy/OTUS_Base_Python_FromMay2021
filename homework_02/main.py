from homework_02.base import Vehicle
from homework_02.car import Car
from homework_02.engine import Engine
from homework_02.plane import Plane

# ---- Task # 1_1 ----:
vehicle_1_1 = Vehicle(fuel=0, fuel_consumption=17, started=False, weight=1500)

# ---- Task # 1_2 ----:
vehicle_1_2 = Vehicle(fuel=20, fuel_consumption=17, started=False, weight=1500)

# ---- Task # 1_3 ----:
vehicle_1_3 = Vehicle(fuel=30, fuel_consumption=15, started=False, weight=2100)

# ---- Task # 1_4 ----:
vehicle_1_4 = Vehicle(fuel=50, fuel_consumption=11, started=False, weight=2450)

# ---- Task # 2_1 ----:'
engine_example_1 = Engine(volume=2.5, pistons=6)
car_2_1 = Car(engine=engine_example_1)

# ---- Task # 3_1, 3_2, 3_3 ----:'
plane_1 = Plane(cargo=12000, max_cargo=17000)

# ---- Task # 3_4 ----:'
plane_2 = Plane(cargo=0, max_cargo=17000)


if __name__ == '__main__':
    print('---- Task # 1_1 ----:')
    vehicle_1_1.start()

    print('\n---- Task # 1_2 ----:')
    vehicle_1_2.start()

    print('\n---- Task # 1_3 ----:')
    vehicle_1_3.move(dist=400)

    print('\n---- Task # 1_4 ----:')
    vehicle_1_4.move(dist=250)

    print('\n---- Task # 2_1 ----:')
    print(car_2_1.set_engine(engine=engine_example_1))

    print('\n---- Task # 3_1 ----:')
    print(plane_1.load_cargo(number=7700))

    print('\n---- Task # 3_2 ----:')
    print(plane_1.load_cargo(number=800))

    print('\n---- Task # 3_3 ----:')
    print(plane_1.remove_all_cargo())

    print('\n---- Task # 3_4 ----:')
    print(plane_2.remove_all_cargo())
