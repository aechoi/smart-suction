from dataclasses import dataclass
import numpy as np


@dataclass
class SuctionCup:
    diameter: float
    lip_height: float
    max_deflection: float

    @property
    def radius(self):
        return self.diameter / 2

    @property
    def origin(self):
        return np.array([0, 0, self.lip_height])


NBR_40mm = SuctionCup(diameter=40.0, lip_height=6.7, max_deflection=5.0)
