import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df["Gender"] = df["Gender"].map({
        "Male": 0,
        "Female": 1
    })

    return df