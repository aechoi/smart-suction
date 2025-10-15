import typing
import numpy as np
import time

from jubilee_controller.jubilee_controller import JubileeMotionController

def load_unload(jubilee: JubileeMotionController,
                dwell: float,
                displacements: typing.List[float]):
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
    #jubilee.gcode(f"G4 P{dwell}")
    
def board_cycles():
    jubilee = JubileeMotionController("192.168.2.5", debug=True)
    
    jubilee.move_xyz_absolute(z=10)
    center = np.array([155, 128, 10])
    jubilee.move_xyz_absolute(*center[:2], 8-2.5)
    jubilee.move_xyz_absolute(*center)

    
    thetas = np.array([np.pi/2 - np.pi/8])
    #thetas = np.linspace(np.pi/2-np.pi/8, 2*np.pi + np.pi/8, 8)
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
        #for _ in range(10):
            #load_unload(jubilee, 5000, [-2.5])
        load_unload(jubilee, 5000, [8-2.5, 0-2.5, 8-2.5, 1-2.5, 8-2.5, 2-2.5, 8-2.5, 3-2.5, 8-2.5, 4-2.5, 8-2.5, 5-2.5, 8-2.5, 6-2.5, 8-2.5, 7-2.5])
        #load_unload(jubilee, 5000, [10, 1-2.5])
def cup_cycles():
    mode = "40mm"
    heights = {
#         "55mm": 25.5,
#         "printed": 29,
#         "printed_1": 11.5,
        "40mm": 6.7,
#         "50mm": 13,
#         "25mm": 9,
        }
    radii = {
        "55mm": 55/2,
        "printed": 40/2,
        "printed_1": 40/2,
        "40mm": 20,
        "50mm": 25,
        "25mm": 25/2,
        }
    jubilee = JubileeMotionController("192.168.2.5", debug=True)
    jubilee.gcode('M950 P4 C"io4.out"')

    clear_z = heights[mode] + 5
    center = np.array([0, 0, clear_z])

    jubilee.move_xyz_absolute(z=clear_z)
    jubilee.move_xyz_absolute(*center)

#     thetas = np.linspace(-np.pi/2+np.pi/8, -np.pi/2-np.pi/8 + 2*np.pi, 8)
#     radii = np.array([radii[mode]])
#     
#     THETAS, RADII = np.meshgrid(thetas, radii)
#     X_OFFSET = RADII * np.cos(THETAS)
#     Y_OFFSET = RADII * np.sin(THETAS)
#     Z_OFFSET = np.zeros_like(X_OFFSET)
#     
#     offsets = np.stack((X_OFFSET, Y_OFFSET, Z_OFFSET), axis=-1)
#     mesh_samples = center[None, None, :] + offsets
#     samples = mesh_samples.reshape(-1, 3)
#     
#     for sample in samples:
#         jubilee.move_xyz_absolute(*sample)
#         load_unload(jubilee, 5000, [heights[mode]-3])
    num_cycles = 5
    for _ in range(num_cycles):
        load_unload(jubilee, 5000, [heights[mode] - 3])
    
    done_offset = np.array([10, 0, 0])
    jubilee.move_xyz_absolute(*center)
    jubilee.move_xyz_absolute(*(center + done_offset))
    jubilee.move_xyz_absolute(*center)
    jubilee.move_xyz_absolute(*(center + done_offset))
    jubilee.move_xyz_absolute(*center)
    jubilee.move_xyz_absolute(*(center + done_offset))
    jubilee.move_xyz_absolute(*center)
    jubilee.move_xyz_absolute(*(center + done_offset))
    jubilee.move_xyz_absolute(*center)
    
def triangles(jubilee, origin, actuation=5, duration = 10):
    """
    Args:
        jubliee: the jubilee object
        origin: the cup origin (top of cup, centered)
        actuation: amount of distance to cycle
        duration: how long to cycle for
    """
    clearance = origin + np.array([0, 0, 5])
    actuation = np.array([0, 0, actuation])
    jubilee.move_xyz_absolute(z=clearance[-1])
    jubilee.move_xyz_absolute(*clearance)
    jubilee.move_xyz_absolute(*origin)
    
    start_time = time.time()

    while time.time() - start_time < duration:
        jubilee.move_xyz_absolute(*(origin - actuation))
        jubilee.move_xyz_absolute(*origin)
        jubilee.gcode("M400")  # finish moves before moving on to next loop.


    jubilee.move_xyz_absolute(*clearance)

if __name__ == "__main__":
    #board_cycles()
#     cup_cycles()
    jubilee = JubileeMotionController("192.168.2.5", debug=True)
    origin = np.array([0, 0, 6.7])
    triangles(jubilee, origin)



