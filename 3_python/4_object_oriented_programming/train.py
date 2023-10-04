class Train:
    def __init__(self, train_number, locomotive, wagons, wagons_weight, current_city, target_destination):
        self.train_mass = None
        self.train_number = train_number
        self.locomotive = locomotive
        self.wagons = wagons
        self.wagons_weight = wagons_weight
        self.current_city = current_city
        self.target_destination = target_destination

    def __bool__(self) -> bool:
        """Checks is the train towable"""
        self.train_mass = self.locomotive.locomotive_mass + self.wagons_weight
        if self.train_mass <= self.locomotive.max_towable_mass:
            return True
        return False

    def move_to_other_city(self, towable_or_not: bool) -> str:
        """Moves the train to the target location"""
        if towable_or_not:
            self.current_city = self.target_destination
            print(f"Train {self.train_number} has successfully reached the next destination - {self.current_city}.")
        else:
            print(f"The train {self.train_number} couldn't reach the destination. Current status - {self.current_city}.")
        return self.current_city

