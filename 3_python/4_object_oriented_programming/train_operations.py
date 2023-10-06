import json
from locomotive import Locomotive
from wagon import Wagon
from train import Train, UntowableTrain
from exceptions import *
import pandas


def weight_of_the_structure(train_structures: list) -> int:
    """Calculates the total weight of the combined train components masses"""
    weight = train_structures[0]
    for structure in range(1, len(train_structures)):
        weight += train_structures[structure]
    return weight


def check_wagon(given_wagon: dict) -> bool:
    """Checking if wagon has sufficient information"""
    if (given_wagon["mass"] > 0 and
            given_wagon["load_mass"] > 0 and
            given_wagon["max_load_mass"] > 0 and
            given_wagon["wagon_number"] is not None):
        return True


def check_locomotive(given_locomotive: Locomotive) -> bool:
    """Checking if locomotive has sufficient information"""
    if (type(given_locomotive.locomotive_name) is str and
            given_locomotive.locomotive_mass > 0 and
            given_locomotive.max_towable_mass > 0 and
            (given_locomotive.is_wagon == 0 or
             given_locomotive.is_wagon == 1)):
        return True


def add_wagon(overweight: int, wagon: Wagon, wagons: list):
    """Adds a wagon if the mass of the load is too high"""
    if wagon.max_mass_of_the_load < overweight:
        mass_added = wagon.max_mass_of_the_load

    else:
        mass_added = overweight

    new_wagon = Wagon(mass=wagon.mass,
                      mass_of_the_load=mass_added,
                      max_mass_of_the_load=wagon.max_mass_of_the_load,
                      unique_wagon_number=wagon.unique_wagon_number
                      )
    overweight -= mass_added
    wagons.append(new_wagon)
    return overweight, wagons


def sort_by_max_load_mass(elem):
    """Returns a wagons max loaded mass"""
    return elem["max_load_mass"]


def get_number_of_wagons(whole_train):
    """Returns the number of wagons in a train"""
    return len(whole_train.wagons)


with open("train_original_data.json") as train_original_data:
    train_data = json.load(train_original_data)

data = pandas.read_csv("train_operations.csv")

locomotive_new = Locomotive(locomotive_name="Add_loco",
                            locomotive_mass=15000,
                            max_towable_mass=1000000,
                            is_wagon=0)
wagon_S = Wagon(mass=10000,
                mass_of_the_load=0,
                max_mass_of_the_load=10000,
                unique_wagon_number="ADD001"
                )


trains = []
untowable_trains = []

for train in train_data["trains"]:
    is_train_info_sufficient = None
    working_locomotives = []
    non_working_locomotives = []
    for new_locomotive in train["locomotives"]:
        locomotive = Locomotive(locomotive_name=new_locomotive["locomotive"],
                                locomotive_mass=new_locomotive["mass"],
                                max_towable_mass=new_locomotive["max_towable_mass"],
                                is_wagon=new_locomotive["is_wagon"]
                                )
        is_train_info_sufficient = check_locomotive(locomotive)
        if not is_train_info_sufficient:

            print(f"Train {train['train_number']} has insufficient/incorrect data about 'locomotive' to form a train.")

            break
        is_wagon = bool(locomotive)
        if is_wagon:
            non_working_locomotives.append(locomotive)
        else:
            working_locomotives.append(locomotive)

    if not is_train_info_sufficient:
        continue
    wagons = []
    total_loaded_mass = 0
    total_max_mass_of_the_load = 0

    train["wagons"].sort(key=sort_by_max_load_mass, reverse=True)

    for wagon in train["wagons"]:
        if check_wagon(wagon):
            train_wagon = Wagon(mass=wagon["mass"],
                                mass_of_the_load=wagon["load_mass"],
                                max_mass_of_the_load=wagon["max_load_mass"],
                                unique_wagon_number=wagon["wagon_number"]
                                )
            wagons.append(train_wagon)
            total_loaded_mass += train_wagon.mass_of_the_load
            total_max_mass_of_the_load += train_wagon.max_mass_of_the_load
        else:
            is_train_info_sufficient = False
            break
    if not is_train_info_sufficient:
        print(f"Train {train['train_number']} has insufficient/incorrect data about 'wagons' to form a train")
        continue

    if total_loaded_mass > total_max_mass_of_the_load:
        print("Wagons are overloaded, need more wagons to carry.")
        for wagon_index in wagons:
            wagon_index.mass_of_the_load = wagon_index.max_mass_of_the_load
            total_loaded_mass -= wagon_index.max_mass_of_the_load
        while total_loaded_mass > 0:
            total_loaded_mass, wagons = add_wagon(total_loaded_mass, wagon_S, wagons)
    else:
        is_enough = False
        for wagon_index in wagons:
            if is_enough:
                wagons.remove(wagon_index)
            elif wagon_index.max_mass_of_the_load > total_loaded_mass:
                wagon_index.mass_of_the_load = total_loaded_mass
                is_enough = True

    wagons_weight = weight_of_the_structure(wagons)

    target_destination = data[data["train_number"] == train["train_number"]]

    unique_train = Train(train["train_number"],
                         locomotives=working_locomotives,
                         locomotive_wagons=non_working_locomotives,
                         wagons=wagons,
                         wagons_weight=wagons_weight.mass,
                         current_city=train["train_current_location"],
                         target_destination=target_destination["target_destination"].to_string(index=False))

    is_towable = unique_train.add_locomotives_until_towable(locomotive_new)

    unique_train.move_to_other_city(is_towable)
    if is_towable:
        trains.append(unique_train)
    else:
        untowable_trains.append(UntowableTrain(train["train_number"]))

sorted_trains = sorted(trains, key=get_number_of_wagons)

all_trains = sorted_trains + untowable_trains
with open("train_new_data.json", "w") as new_train_data:
    json.dump({"trains": [train.prepare_for_json() for train in all_trains]}, new_train_data, indent=4)
