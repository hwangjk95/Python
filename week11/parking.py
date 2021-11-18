#parking.py

import car
import time

MAX = 10
car_list = []

if len(car_list)<MAX:
    car1 = car.Car("111가1111")
    car_list.append(car1)
    print(car1.intime, car1.outtime)
    time.sleep(5)
    number = "111가1111"
    for c in car_list:
        if c.number == number:
            car1.out()
            print(car1.intime, car1.outtime)
            print(car1.gettime(),car1.calprice())
            car_list.remove(c)
            break