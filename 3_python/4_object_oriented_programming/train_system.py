import json
import pandas as pd
from locomotive import Locomotive
from wagon import Wagon
from train import Train, UntowableTrain
from exceptions import *


class TrainStation:
    def __init__(self, train_data_file, operations_file):
        self.train_data_file = train_data_file
        self.operations_file = operations_file
        self.locomotive_new = Locomotive(locomotive_name="Add_loco",
                                         locomotive_mass=15000,
                                         max_towable_mass=1000000,
                                         is_wagon=0)
        self.wagon_S = Wagon(mass=10000,
                             mass_of_the_load=0,
                             max_mass_of_the_load=10000,
                             unique_wagon_number="ADD001"
                             )
        self.trains = []
        self.untowable_trains = []

    def process_train_data(self):
        train_data = self.load_train_data()
        operations_data = self.load_operations_data()

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
                try:
                    is_train_info_sufficient = self.check_locomotive(locomotive)

                except InsufficientData:
                    print(f"Train {train['train_number']} has insufficient/incorrect data about 'locomotive' to form "
                          f"a train")
                    break
                if not is_train_info_sufficient:
                    print(f"Train {train['train_number']} has insufficient/incorrect data about 'locomotive' to form "
                          f"a train")
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

            train["wagons"].sort(key=lambda wagon: wagon["max_load_mass"], reverse=True)

            for wagon in train["wagons"]:
                if self.check_wagon(wagon):
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
                    total_loaded_mass, wagons = self.add_wagon(total_loaded_mass, self.wagon_S, wagons)
            else:
                is_enough = False
                for wagon_index in wagons:
                    if is_enough:
                        wagons.remove(wagon_index)
                    elif wagon_index.max_mass_of_the_load > total_loaded_mass:
                        wagon_index.mass_of_the_load = total_loaded_mass
                        is_enough = True

            wagons_weight = self.weight_of_the_structure(wagons)

            target_destination = operations_data[operations_data["train_number"] == train["train_number"]]

            unique_train = Train(train["train_number"],
                                 locomotives=working_locomotives,
                                 locomotive_wagons=non_working_locomotives,
                                 wagons=wagons,
                                 wagons_weight=wagons_weight.mass,
                                 current_city=train["train_current_location"],
                                 target_destination=target_destination["target_destination"].to_string(index=False))

            is_towable = unique_train.add_locomotives_until_towable(self.locomotive_new)

            unique_train.move_to_other_city(is_towable)

            if is_towable:
                self.trains.append(unique_train)
            else:
                self.untowable_trains.append(UntowableTrain(train["train_number"]))

        self.sort_trains_by_wagons()
        self.save_trains_to_json()

    # def build_new_train_with_given_load(self):
    #     should_i_build = input("Should I load this train with a load in csv file? Type yes/no")
    #     if should_i_build.lower() == "yes":
    #         self.process_train_data()
    #     else:
    #         print("The program has closed, ")
    #         pass

    def load_train_data(self):
        """Load calculated train data"""
        with open(self.train_data_file) as train_data_file:
            return json.load(train_data_file)

    def load_operations_data(self):
        """Read given train data"""
        return pd.read_csv(self.operations_file)

    @staticmethod
    def weight_of_the_structure(train_structures: list) -> int:
        """Calculates the total weight of the combined train components masses"""
        weight = train_structures[0]
        for structure in range(1, len(train_structures)):
            weight += train_structures[structure]
        return weight

    @staticmethod
    def check_wagon(given_wagon: dict) -> bool:
        """Checking if wagon has sufficient information"""
        return (
                isinstance(given_wagon.get("mass", 0), int) and
                isinstance(given_wagon.get("load_mass", 0), int) and
                isinstance(given_wagon.get("max_load_mass", 0), int) and
                given_wagon.get("wagon_number") is not None and
                given_wagon.get("mass", 0) > 0 and
                given_wagon.get("load_mass", 0) > 0 and
                given_wagon.get("max_load_mass", 0) > 0
        )

    @staticmethod
    def check_locomotive(given_locomotive: Locomotive) -> bool:
        """Checking if locomotive has sufficient information"""
        if (
                isinstance(given_locomotive.locomotive_name, str)
                and given_locomotive.locomotive_mass > 0
                and given_locomotive.max_towable_mass > 0
                and given_locomotive.is_wagon in (0, 1)
        ):
            return True
        else:
            raise InsufficientData

    @staticmethod
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

    def sort_trains_by_wagons(self):
        """Sorts the list of trains by the number of wagons"""
        self.trains.sort(key=lambda train: len(train.wagons))

    def save_trains_to_json(self):
        with open("train_new_data.json", "w") as new_train_data:
            json.dump({"trains": [train.prepare_for_json() for train in self.trains + self.untowable_trains]},
                      new_train_data, indent=4)


if __name__ == "__main__":
    train_station = TrainStation("train_original_data.json", "train_operations.csv")
    train_station.process_train_data()
    # train_station.build_new_train_with_given_load()

    instructions = """
    # Train operations

    This program reads and distributes randomly loaded cargo in given trains preparing it to travel to the next train station. 
    If the train is overloaded, program adds more locomotives (up to 3) and/or wagons. 
    If locomotives are overloaded, trains cannot move.
    Locomotives can be counted as wagons if is_wagon in .json file is 1 (True). 
    Working locomotives has is_wagon = 0 (False). 
    
    
    ## Usage
    - For the program to work you will need a train_original_data.json and train_operations.csv file.
    - In train_original_data.json file cargo should be loaded. The file should have trains information - 
    Train number, train current location, locomotives, wagons.
    - train_operations.csv file has a train number and a target destination where this train must travel.
    
    
    ## Functions:
    - TrainStation class:
        - process_train_data - uses loaded train data from json and csv file to create a new dictionary of trains.
        These trains are stored in a new json file. If trains are untowable, they are marked as untowable in a file.
        - load_train_data and load_operations_data - loads train_original_data.json and reads the data provided by the user.
        - weight_of_the_structure - calculates the total weight of the train
        - check_wagon and check_locomotive - checks if the data provided by the user is sufficient/valid to create a train.
        - add_wagon - Adds a wagon if the mass of the load is too high. Returns overloaded mass and a list of new connected wagons. 
        - sort_train_by_wagons - Sorts the list of trains by the number of wagons. Returns new train list.
        - save_train_to_json - creates a new json file.
    """

    readme_file_path = "README.md"
    with open(readme_file_path, "w") as readme_file:
        readme_file.write(instructions)
