class Train:
    def __init__(self, train_number: str,
                 locomotives: list,
                 locomotive_wagons: list,
                 wagons,
                 wagons_weight: int,
                 current_city: str,
                 target_destination: str):
        self.added_wagons = 0
        self.train_mass = None
        self.train_number = train_number
        self.locomotives = locomotives
        self.locomotive_wagons = locomotive_wagons
        self.wagons = wagons
        self.wagons_weight = wagons_weight
        self.current_city = current_city
        self.target_destination = target_destination
        self.train_towable_power = 0

    def __bool__(self) -> bool:
        """Checks is the train towable"""
        if self.train_mass_calculator() <= self.locomotives_power():
            return True
        return False

    def move_to_other_city(self, towable_or_not: bool) -> str:
        """Moves the train to the target location"""
        if towable_or_not:
            self.current_city = self.target_destination
            print(f"Train {self.train_number} has successfully reached the next destination - {self.current_city}.")
        else:

            print(
                f"The train {self.train_number} couldn't reach the destination. Current status - {self.current_city}.")

        return self.current_city

    def train_mass_calculator(self) -> int:
        locomotives_mass = sum(locomotive.locomotive_mass for locomotive in self.locomotives)
        non_working_locomotives_mass = sum(locomotive.locomotive_mass for locomotive in self.locomotive_wagons)
        self.train_mass = self.wagons_weight + locomotives_mass + non_working_locomotives_mass
        return self.train_mass

    def locomotives_power(self) -> int:
        for locomotive in self.locomotives:
            self.train_towable_power += locomotive.max_towable_mass
        return self.train_towable_power

    def add_locomotives_until_towable(self, locomotive_new) -> bool:
        working_locomotives = self.locomotives if hasattr(self, 'locomotives') else []

        while not self.__bool__():
            working_locomotives.append(locomotive_new)
            self.locomotives = working_locomotives
            print("Locomotive added")
            if len(working_locomotives) > 3:
                print("No more than 3 locomotives can tow")
                return False
        return self.__bool__()

    def prepare_for_json(self) -> dict:
        return {
            "train_number": self.train_number,
            "locomotives": [locomotive.prepare_for_json() for locomotive in self.locomotives] + [loco.prepare_for_json()
                                                                                                 for loco in
                                                                                                 self.locomotive_wagons],
            "wagons": [wagon.prepare_for_json() for wagon in self.wagons],
            "wagons_weight": self.wagons_weight,
            "added_or_subtracted_wagons": self.added_wagons,
            "amount_of_wagons": len(self.wagons),
            "current_city": self.current_city,
            "target_destination": self.target_destination
        }


class UntowableTrain:
    def __init__(self, train_number):
        self.train_number = train_number

    def prepare_for_json(self) -> dict:
        return {
            "train_number": self.train_number,
            "status": "Untowable with given mass."
        }
