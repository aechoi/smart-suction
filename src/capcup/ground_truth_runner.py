import pandas as pd


def main():
    labeled_data = pd.read_csv("ground_truth.csv")

    lip_to_board_height = 10
    clearance_z = lip_to_board_height + 5

    # deactuate z
    for idx, sample in labeled_data.iterrows():
        # move to xy
        # dwell
        # actuate z
        # dwell
        # deactuate z
        pass


if __name__ == "__main__":
    main()
