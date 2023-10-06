class Wagon:
    def __init__(self, mass, mass_of_the_load, max_mass_of_the_load, unique_wagon_number):
        self.overweight = 0
        self.mass = mass
        self.mass_of_the_load = mass_of_the_load
        self.max_mass_of_the_load = max_mass_of_the_load
        self.unique_wagon_number = unique_wagon_number

    def __add__(self, other):
        """Adds the wagon and its mass to the total"""
        unloaded_wagons_mass = self.mass + other.mass
        self.load_mass = self.mass_of_the_load + other.mass_of_the_load
        max_all_wagons_capacity = self.max_mass_of_the_load + other.max_mass_of_the_load
        wagons_combined_mass = unloaded_wagons_mass + self.load_mass
        return Wagon(wagons_combined_mass, self.load_mass, max_all_wagons_capacity, self.unique_wagon_number)

    def check_mass(self):
        if self.mass_of_the_load > self.max_mass_of_the_load:
            print(f"Wagon {self.unique_wagon_number} cannot carry this load")
            self.overweight = self.mass_of_the_load - self.max_mass_of_the_load
            print(self.overweight)
        return self.overweight

    def prepare_for_json(self):
        return {
            "wagon_number": self.unique_wagon_number,
            "mass": self.mass,
            "load_mass": self.mass_of_the_load,
            "max_load_mass": self.max_mass_of_the_load,
        }
