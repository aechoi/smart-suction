"""Code for generating random offsets for data collection.

What do I want?
Generate a valid list of offsets and orientations.
    The tool must actuate the suction cup in the method described.
    The tool must not collide with the board.
Output to a file that can be used for ground truth and for gcode.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class SuctionCup:
    diameter: float
    lip_to_board_height: float
    max_actuation: float

    def get_max_depth(self) -> float:
        """For a particular convex tool orientation, what is the maximum deflection that
        can be achieved before the tool collides with the board."""
        return self.lip_to_board_height + self.diameter / 2


@dataclass
class Tool(ABC):
    """Class representing a tool with size and pose. All lengths in mm, angles in
    radians."""

    x: float = 0
    y: float = 0
    z: float = 0
    alpha: float = 0
    beta: float = 0
    gamma: float = 0

    @abstractmethod
    def sample(self, num_samples: int) -> np.ndarray:
        raise NotImplementedError


@dataclass
class Box(Tool):
    """Class representing a box with size and pose. All lengths in mm, angles in
    radians."""

    x_size: float = 1
    y_size: float = 1
    z_size: float = 1

    def sample(self, num_samples: int, cup: SuctionCup) -> np.ndarray:
        labeled_data = pd.concat(
            [
                self.sample_aligned(num_samples, cup),
                self.sample_edge_misaligned(num_samples, cup),
                self.sample_corner_misaligned(num_samples, cup),
            ],
            ignore_index=True,
        )

        shuffled_data = labeled_data.sample(frac=1).reset_index(drop=True)
        return shuffled_data

    def sample_aligned(self, num_samples: int, cup: SuctionCup) -> pd.DataFrame:
        x_bound = (
            -(self.x_size / 2 - cup.diameter / 2),
            self.x_size / 2 - cup.diameter / 2,
        )
        y_bound = (
            -(self.y_size / 2 - cup.diameter / 2),
            self.y_size / 2 - cup.diameter / 2,
        )
        z_bound = (cup.lip_to_board_height - cup.max_actuation, cup.lip_to_board_height)

        x_samples = np.random.uniform(*x_bound, num_samples)
        y_samples = np.random.uniform(*y_bound, num_samples)
        z_samples = np.random.uniform(*z_bound, num_samples)
        alpha_samples = np.zeros(num_samples)
        beta_samples = np.zeros(num_samples)
        gamma_samples = np.zeros(num_samples)

        labels = ["aligned"] * num_samples
        labeled_data = pd.DataFrame(
            {
                "x": x_samples,
                "y": y_samples,
                "z": z_samples,
                "alpha": alpha_samples,
                "beta": beta_samples,
                "gamma": gamma_samples,
                "label": labels,
            }
        )
        return labeled_data

    def sample_edge_misaligned(self, num_samples: int, cup: SuctionCup) -> pd.DataFrame:
        # Because the set is nonconvex, generate random samples for each and then randomly
        # choose between them.
        horizontal_x_bound = (
            self.x_size / 2 - cup.diameter / 2,
            self.x_size / 2 + cup.diameter / 2,
        )
        horizontal_y_bound = (
            -(self.y_size / 2 - cup.diameter / 2),
            self.y_size / 2 - cup.diameter / 2,
        )
        horizontal_x_samples = np.random.uniform(*horizontal_x_bound, num_samples)
        horizontal_y_samples = np.random.uniform(*horizontal_y_bound, num_samples)
        horizontal_side_sample = np.random.choice([-1, 1], num_samples)
        horizontal_x_samples *= horizontal_side_sample

        vertical_x_bound = (
            -(self.x_size / 2 - cup.diameter / 2),
            self.x_size / 2 - cup.diameter / 2,
        )
        vertical_y_bound = (
            self.y_size / 2 - cup.diameter / 2,
            self.y_size / 2 + cup.diameter / 2,
        )
        vertical_x_samples = np.random.uniform(*vertical_x_bound, num_samples)
        vertical_y_samples = np.random.uniform(*vertical_y_bound, num_samples)
        vertical_side_sample = np.random.choice([-1, 1], num_samples)
        vertical_y_samples *= vertical_side_sample

        # Now randomly choose between horizontal and vertical samples
        choose_horizontal = np.random.choice([True, False], num_samples)
        x_samples = np.where(
            choose_horizontal, horizontal_x_samples, vertical_x_samples
        )
        y_samples = np.where(
            choose_horizontal, horizontal_y_samples, vertical_y_samples
        )
        z_samples = np.random.uniform(
            cup.lip_to_board_height - cup.max_actuation,
            cup.lip_to_board_height,
            num_samples,
        )
        alpha_samples = np.zeros(num_samples)
        beta_samples = np.zeros(num_samples)
        gamma_samples = np.zeros(num_samples)

        labels = ["edge_misaligned"] * num_samples
        labeled_data = pd.DataFrame(
            {
                "x": x_samples,
                "y": y_samples,
                "z": z_samples,
                "alpha": alpha_samples,
                "beta": beta_samples,
                "gamma": gamma_samples,
                "label": labels,
            }
        )
        return labeled_data

    def sample_corner_misaligned(
        self, num_samples: int, cup: SuctionCup
    ) -> pd.DataFrame:
        # From a corner, sample uniformly in a circle around that corner.
        # Then randomly select a corner to center around.
        radii = cup.diameter / 2 * np.sqrt(np.random.uniform(0, 1, num_samples))
        thetas = np.random.uniform(0, np.pi * 2, num_samples)
        x_disk = radii * np.cos(thetas)
        y_disk = radii * np.sin(thetas)

        x_choice = np.random.choice([-1, 1], num_samples)
        y_choice = np.random.choice([-1, 1], num_samples)

        x_corner = x_choice * self.x_size / 2
        y_corner = y_choice * self.y_size / 2
        x_samples = x_disk + x_corner
        y_samples = y_disk + y_corner

        z_samples = np.random.uniform(
            cup.lip_to_board_height - cup.max_actuation,
            cup.lip_to_board_height,
            num_samples,
        )
        alpha_samples = np.zeros(num_samples)
        beta_samples = np.zeros(num_samples)
        gamma_samples = np.zeros(num_samples)

        labels = ["corner_misaligned"] * num_samples
        labeled_data = pd.DataFrame(
            {
                "x": x_samples,
                "y": y_samples,
                "z": z_samples,
                "alpha": alpha_samples,
                "beta": beta_samples,
                "gamma": gamma_samples,
                "label": labels,
            }
        )
        return labeled_data


def main():
    box = Box(x_size=100, y_size=100)
    cup = SuctionCup(diameter=40, lip_to_board_height=6.7, max_actuation=5)
    num_samples = 1000
    ground_truth = box.sample(num_samples, cup)
    ground_truth.to_csv("ground_truth.csv", index=False)


if __name__ == "__main__":
    main()
