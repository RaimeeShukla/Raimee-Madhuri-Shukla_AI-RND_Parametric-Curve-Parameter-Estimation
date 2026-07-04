import pandas as pd

def load_dataset(csv_path):
    """
    Load x-y coordinates from CSV.

    Output:
    1) x : ndarray
    2) y : ndarray
    """

    df = pd.read_csv(csv_path)
    x = df["x"].to_numpy()
    y = df["y"].to_numpy()

    return x, y