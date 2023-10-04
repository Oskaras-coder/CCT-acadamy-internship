import json
from locomotive import Locomotive
from wagon import Wagon
from train import Train
import pandas


def weight_of_the_structure(train_structures: list):
    """Calculates the total weight of the combined train components masses"""
    weight = train_structures[0]
    for structure in range(1, len(train_structures)):
        weight += train_structures[structure]
    return weight


def check_wagon(given_wagon):
    """Checking if locomotive has sufficient information"""
    if not (type(given_wagon["mass"]) is not int or
            type(given_wagon["load_mass"]) is not int or
            type(given_wagon["max_load_mass"]) is not int or
            given_wagon["wagon_number"] is None):
        return True


def check_locomotive(given_locomotive):
    """Checking if locomotive has sufficient information"""
    if not (type(given_locomotive.locomotive_mass) is not int or
            type(given_locomotive.max_towable_mass) is not int):
        return True


# def add_wagon(overweight, wagon: Wagon, wagons: list):
#     overweight -= wagon.max_mass_of_the_load
#     wagon.mass_of_the_load = overweight
#     wagons.append(wagon)
#     return overweight, wagons


with open("train_original_data.json") as train_original_data:
    train_data = json.load(train_original_data)

data = pandas.read_csv("train_operations.csv")

wagon_S = Wagon(mass=10000,
                mass_of_the_load=0,
                max_mass_of_the_load=10000,
                unique_wagon_number="ADD001"
                )
wagon_M = Wagon(mass=12000,
                mass_of_the_load=0,
                max_mass_of_the_load=20000,
                unique_wagon_number="ADD002"
                )
wagon_L = Wagon(mass=14000,
                mass_of_the_load=0,
                max_mass_of_the_load=30000,
                unique_wagon_number="ADD003"
                )
trains = []
for train in train_data["trains"]:
    locomotive = Locomotive(locomotive_mass=train["locomotive"]["mass"],
                            max_towable_mass=train["locomotive"]["max_towable_mass"]
                            )
    is_train_info_sufficient = check_locomotive(locomotive)
    if not is_train_info_sufficient:
        print(f"Train {train['train_number']} has insufficient/incorrect data about 'locomotive' to form a train")
        continue
    wagons = []
    wagon_overweight = 0
    for wagon in train["wagons"]:
        wagon["load_mass"] += wagon_overweight
        wagon_overweight = 0
        if check_wagon(wagon):
            train_wagon = Wagon(mass=wagon["mass"],
                                mass_of_the_load=wagon["load_mass"],
                                max_mass_of_the_load=wagon["max_load_mass"],
                                unique_wagon_number=wagon["wagon_number"]
                                )
            wagon_overweight += train_wagon.check_mass()
            wagons.append(train_wagon)
        else:
            is_train_info_sufficient = False
            break
    if wagon_overweight > 0:
        print("Wagons are overloaded, need more wagons to carry.")
        # while wagon_overweight > 0:
        #     wagon_overweight, wagons = add_wagon(wagon_overweight, wagon_S, wagons)
        #
    if not is_train_info_sufficient:
        print(f"Train {train['train_number']} has insufficient/incorrect data about 'wagons' to form a train")
        continue
    wagons_weight = weight_of_the_structure(wagons)
    target_destination = data[data["train_number"] == train["train_number"]]

    unique_train = Train(train["train_number"],
                         locomotive=locomotive,
                         wagons=wagons,
                         wagons_weight=wagons_weight,
                         current_city=train["train_current_location"],
                         target_destination=target_destination["target_destination"].to_string(index=False))
    is_towable = bool(unique_train)
    unique_train.move_to_other_city(is_towable)

    trains.append(unique_train)

# with open("train_new_data.json", "w") as new_train_data:
#     json.dump(new_data, new_train_data, indent=4)
