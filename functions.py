# import json
# from definitions import *
# from json_methods import cars_to_json

# cars = []

# def display_actions():
#             print("1 - Print the garage")
#             print("2 - Add a car")
#             print("3 - Update a car")
#             print("4 - Delete a car")
#             print("5 - How many cars")
#             print("6 - Clear data")

# def print_the_cars(cars):
#         car_list_json = json.dumps(cars, indent=4)
#         print(car_list_json)
    

# def add_car(cars):
#     new_car = Car(input("color: "), input("model: "), input("kind: "))
#     cars.append(new_car)
#     cars_to_json(cars)
#     print_the_cars(cars)

