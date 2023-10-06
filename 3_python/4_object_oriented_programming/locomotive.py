from dataclasses import dataclass


@dataclass
class Locomotive:
    locomotive_name: str
    locomotive_mass: int
    max_towable_mass: int
    is_wagon: int

    def __bool__(self):
        if self.is_wagon == 0:
            return False
        return True

    def prepare_for_json(self):
        return {
            "locomotive_name": self.locomotive_name,
            "mass": self.locomotive_mass,
            "max_towable_mass": self.max_towable_mass,
            "is_wagon": self.is_wagon
        }
