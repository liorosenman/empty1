import json
file_path = 'cars.json'

def json_to_cars():
    try:
        with open(file_path, 'r') as file:
            cars = json.load(file)
        return cars
    except:
         return []

# def cars_to_json(cars):
#     cars_dict_list = []
#     # car_dict = {}
#     for car in cars:
#         car_dict = car.to_dict()
#         cars_dict_list.append(car_dict)
#     with open('cars.json', 'w') as json_file:
#         json.dump(cars_dict_list,json_file,indent=4)


# def cars_to_json(cars):
#     cars_dict_list = dict(cars)
#     with open(filename, 'w') as json_file:
#         json.dump(cars_dict_list, json_file, indent=4)

# def cars_to_json(cars):
#          cars_list = [car.to_dict(car) for car in cars]
#          with open(file_path, 'w') as json_file:
#             json.dump(cars_list, json_file, indent=4)

def cars_to_json(cars):
    with open('cars.json', 'w') as json_file:
        json.dump(cars, json_file, indent=4)

