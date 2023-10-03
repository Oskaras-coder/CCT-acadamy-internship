import json


class Locomotive:
    def __init__(self, locomotive_mass, max_towable_mass):
        self.locomotive_mass = locomotive_mass
        self.max_towable_mass = max_towable_mass


class Wagon:
    def __init__(self, mass, mass_of_the_load, max_mass_of_the_load, unique_wagon_number):
        self.mass = mass
        self.mass_of_the_load = mass_of_the_load
        self.max_mass_of_the_load = max_mass_of_the_load
        self.unique_wagon_number = unique_wagon_number

    def __add__(self, other):
        unloaded_wagons_mass = self.mass + other.mass
        wagons_combined_mass = unloaded_wagons_mass + self.mass_of_the_load + other.mass_of_the_load
        return wagons_combined_mass


class Train:
    def __init__(self, train_number, locomotive, wagons):
        self.train_number = train_number
        self.locomotive = locomotive
        self.wagons = wagons


with open("train_original_data.json") as train_original_data:
    train_data = json.load(train_original_data)

trains = []
for train in train_data["trains"]:
    locomotive = Locomotive(locomotive_mass=train["locomotive"]["mass"],
                            max_towable_mass=train["locomotive"]["max_towable_mass"]
                            )
    wagons = []
    for wagon in train["wagons"]:
        train_wagon = Wagon(mass=wagon["mass"],
                            mass_of_the_load=wagon["load_mass"],
                            max_mass_of_the_load=wagon["max_load_mass"],
                            unique_wagon_number=wagon["wagon_number"]
                            )
        wagons.append(train_wagon)
    unique_train = Train("train_number", locomotive=locomotive, wagons=wagons)
    trains.append(unique_train)


# with open("train_new_data.json", "w") as new_train_data:
#     json.dump(new_data, new_train_data, indent=4)
