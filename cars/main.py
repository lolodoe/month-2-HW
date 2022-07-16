from cars.get_car_info import get_car_info
volvo = get_car_info("volvo","v80","black")
print(volvo.car_info())
print(volvo.start_engine())
print(volvo.stop_engine())