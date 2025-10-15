import typing
import numpy as np
import time

from jubilee_controller.jubilee_controller import JubileeMotionController
import cup_configs

CLEAR = np.array([0, 0, 5])


def load_unload(
    jubilee: JubileeMotionController, dwell: float, displacements: typing.List[float]
):
    """
    Args
        - dwell: float, the dwell time in milliseconds
        - displacements: list, a list of displacements from the starting position, positive denotes separation
    """
    current_z = jubilee.position[2]

    for displacement in displacements:
        jubilee.gcode(f"G4 P{dwell}")

        jubilee.gcode("M400")
        jubilee.gcode("M42 P4 S1")
        jubilee.gcode("M400")
        jubilee.move_xyz_absolute(z=displacement)
        jubilee.gcode("M400")
        jubilee.gcode("M42 P4 S0")

    jubilee.gcode(f"G4 P{dwell}")

    jubilee.gcode("M400")
    jubilee.gcode("M42 P4 S1")
    jubilee.gcode("M400")
    jubilee.move_xyz_absolute(z=current_z)
    jubilee.gcode("M400")
    jubilee.gcode("M42 P4 S0")
    # jubilee.gcode(f"G4 P{dwell}")


def center_tool(jubilee, suction_cup):
    # clear and move above origin
    jubilee.move_xyz_absolute(z=(suction_cup.origin + CLEAR)[-1])
    jubilee.move_xyz_absolute(*(suction_cup.origin + CLEAR))


def end_signal(jubilee, suction_cup):
    # do a quick dance to signal the end
    center_tool(jubilee, suction_cup)
    done_offset = np.array([10, 0, 0])

    for _ in range(5):
        jubilee.move_xyz_absolute(*(suction_cup.origin + CLEAR))
        jubilee.move_xyz_absolute(*(suction_cup.origin + CLEAR + done_offset))

    center_tool(jubilee, suction_cup)


def board_cycles():
    jubilee = JubileeMotionController("192.168.2.5", debug=True)

    jubilee.move_xyz_absolute(z=10)
    center = np.array([155, 128, 10])
    jubilee.move_xyz_absolute(*center[:2], 8 - 2.5)
    jubilee.move_xyz_absolute(*center)

    thetas = np.array([np.pi / 2 - np.pi / 8])
    # thetas = np.linspace(np.pi/2-np.pi/8, 2*np.pi + np.pi/8, 8)
    radii = np.array([20])
    THETAS, RADII = np.meshgrid(thetas, radii)
    X_OFFSET = RADII * np.cos(THETAS)
    Y_OFFSET = RADII * np.sin(THETAS)
    Z_OFFSET = np.zeros_like(X_OFFSET)

    offsets = np.stack((X_OFFSET, Y_OFFSET, Z_OFFSET), axis=-1)
    mesh_samples = center[None, None, :] + offsets
    samples = mesh_samples.reshape(-1, 3)
    print(samples)

    for sample in samples:
        jubilee.move_xyz_absolute(*sample)
        # for _ in range(10):
        # load_unload(jubilee, 5000, [-2.5])
        load_unload(
            jubilee,
            5000,
            [
                8 - 2.5,
                0 - 2.5,
                8 - 2.5,
                1 - 2.5,
                8 - 2.5,
                2 - 2.5,
                8 - 2.5,
                3 - 2.5,
                8 - 2.5,
                4 - 2.5,
                8 - 2.5,
                5 - 2.5,
                8 - 2.5,
                6 - 2.5,
                8 - 2.5,
                7 - 2.5,
            ],
        )
        # load_unload(jubilee, 5000, [10, 1-2.5])


def ring_cycles(jubilee, suction_cup, dwell=5000, cycles=1):
    # NEED TO TEST
    thetas = np.linspace(-np.pi / 2 + np.pi / 8, -np.pi / 2 - np.pi / 8 + 2 * np.pi, 8)
    radii = np.array([suction_cup.radius])

    THETAS, RADII = np.meshgrid(thetas, radii)
    X_OFFSET = RADII * np.cos(THETAS)
    Y_OFFSET = RADII * np.sin(THETAS)
    Z_OFFSET = np.zeros_like(X_OFFSET)

    offsets = np.stack((X_OFFSET, Y_OFFSET, Z_OFFSET), axis=-1)
    mesh_samples = suction_cup.origin[None, None, :] + offsets
    samples = mesh_samples.reshape(-1, 3)

    for cycle in range(cycles):
        for sample in samples:
            jubilee.move_xyz_absolute(*sample)
            load_unload(jubilee, dwell, [suction_cup.lip_height[-1] - 3])


def cup_cycles(
    jubilee, suction_cup, dwell=5000, actuation=3, cycles=None, duration=None
):
    if cycles is None and duration is None:
        raise ValueError("Must specify either cycles or duration")

    if cycles is not None:
        for _ in range(cycles):
            load_unload(jubilee, dwell, [suction_cup.origin[-1] - actuation])
    else:
        start_time = time.time()
        while time.time() - start_time < duration:
            load_unload(jubilee, dwell, [suction_cup.origin[-1] - actuation])


def triangles(jubilee, suction_cup, duration=10):
    """
    Args:
        jubliee: the jubilee object
        origin: the cup origin (top of cup, centered)
        actuation: amount of distance to cycle
        duration: how long to cycle for
    """
    actuation = np.array([0, 0, suction_cup.max_deflection])
    jubilee.move_xyz_absolute(*suction_cup.origin)

    start_time = time.time()

    while time.time() - start_time < duration:
        jubilee.move_xyz_absolute(*(suction_cup.origin - actuation))
        jubilee.move_xyz_absolute(*suction_cup.origin)
        jubilee.gcode("M400")  # finish moves before moving on to next loop.


def main():
    suction_cup = cup_configs.NBR_40mm

    jubilee = JubileeMotionController("192.168.2.5", debug=True)
    jubilee.gcode('M950 P4 C"io4.out"')  # set connector 4 for io
    center_tool(jubilee, suction_cup)

    triangles(jubilee, suction_cup)
    # cup_cycles(jubilee, suction_cup)

    end_signal(jubilee, suction_cup)


if __name__ == "__main__":
    main()
