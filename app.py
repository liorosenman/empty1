from definitions import Car, Menu
# from functions import *
from json_methods import *

cars = []

def display_actions():
            print("1 - Print the garage")
            print("2 - Add a car")
            print("3 - Update a car")
            print("4 - Delete a car")
            print("5 - How many cars")
            print("6 - Clear data")

def print_the_cars(cars):
        if len(cars) == 0:
            print("The garage is lazy")
        else:
            for car in cars:
                print(car)

def add_car(cars):
    new_car = Car(input("color: "), input("model: "), input("kind: "))
    new_car_dict = new_car.to_dict()
    cars.append(new_car_dict)
#    cars_to_json(cars)
    print_the_cars(cars)

def upd_car(cars):
      index_to_change = int(input("Index to change: "))
      updated_car = Car(input("color: "), input("model: "), input("kind: "))
      cars[index_to_change -1] = updated_car.to_dict()
      print_the_cars(cars)

def del_car(cars):
       index_to_del = int(input("Index to delete: "))
       cars.pop(index_to_del - 1)
       print_the_cars(cars)

if __name__ == "__main__":
        cars = json_to_cars()
        while True:
            display_actions()
            choise = input("What do you want to do? ")
            choise_int = int(choise)
            choise_action = Menu(choise_int)
            if (choise_action == Menu.PRINT):
                print_the_cars(cars)
            if (choise_action == Menu.ADD):
                add_car(cars)
            if (choise_action == Menu.UPDATE):
                upd_car(cars)
            if (choise_action == Menu.DELETE):
                del_car(cars)
            cars_to_json(cars)
            

# if __name__ == "__main__":
#       car1 = Car("Jeru", 1989, "zaza")
#       car2 = Car("ysaof", 1970, "pizzA")
#       cars.append(car1)
#       cars.append(car2)
#       car_dict_list = []
#       for car in cars:
#             car_dict = car.to_dict()
#             car_dict_list.append(car_dict)
#       with open('cars.json', 'w') as json_file:
#         json.dump(car_dict_list,json_file,indent=4)
            

