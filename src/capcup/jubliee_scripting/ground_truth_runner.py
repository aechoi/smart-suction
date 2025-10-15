import numpy as np
# import pandas as pd
import csv

from jubilee_controller.jubilee_controller import JubileeMotionController


def main():
    jubilee = JubileeMotionController("192.168.2.5", debug=True)
    jubilee.gcode('M950 P4 C"io4.out"')
    
#     labeled_data = pd.read_csv("ground_truth.csv")
    
    lip_to_board_height = 6.7
    center = np.array([0, 0, lip_to_board_height + 5])
    dwell = 5000
    
    jubilee.move_xyz_absolute(z = center[-1])
    jubilee.move_xyz_absolute(*center)
    
    with open("ground_truth_x1000.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for idx, row in enumerate(reader):
            if idx == 0: continue
            position = np.array(row[:3], dtype=float)
            orientation = np.array(row[3:-1], dtype=float)
            
            jubilee.move_xyz_absolute(*position[:-1])
            jubilee.gcode(f"G4 P{dwell}")
            jubilee.gcode("M400")
            jubilee.gcode("M42 P4 S1")
            jubilee.gcode("M400")
            jubilee.move_xyz_absolute(z=position[-1])
            jubilee.gcode("M400")
            jubilee.gcode("M42 P4 S0")
            
            jubilee.gcode(f"G4 P{dwell}")
            jubilee.gcode("M400")
            jubilee.gcode("M42 P4 S1")
            jubilee.gcode("M400")
            jubilee.move_xyz_absolute(z=center[-1])
            jubilee.gcode("M400")
            jubilee.gcode("M42 P4 S0")
            
#     for idx, sample in labeled_data.iterrows():
#         jubilee.move_xyz_absolute(*sample[:-1])
#         jubilee.gcode(f"G4 P{dwell}")
#         jubilee.gcode("M400")
#         jubilee.gcode("M42 P4 S1")
#         jubilee.gcode("M400")
#         jubilee.move_xyz_absolute(z=sample[-1])
#         jubilee.gcode("M400")
#         jubilee.gcode("M42 P4 S0")
#         jubilee.move_xyz_absolute(z=center[-1])
        
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

if __name__ == "__main__":
    main()
        

        
