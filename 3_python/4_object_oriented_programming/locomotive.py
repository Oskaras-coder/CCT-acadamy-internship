from dataclasses import dataclass


@dataclass
class Locomotive:
    locomotive_mass: int
    max_towable_mass: int
