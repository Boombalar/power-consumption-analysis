import numpy as np
import pandas as pd


def load_measurements(filename: str, fmode: str):
    try:
        dataset = pd.read_csv("../data/" + filename, header=None)
        dataset.columns = ['year', 'month', 'day', 'hour', 'minute', 'second', 'zone1', 'zone2', 'zone3', 'zone4']

        if fmode == "drop":
            dataset = dataset[dataset.select_dtypes(include=[np.number]).ge(0).all(1)]
        elif fmode == "forward fill":
            if (dataset.head(1) < 0).any().any():
                dataset = dataset[dataset.select_dtypes(include=[np.number]).ge(0).all(1)]
                print("First row had invalid measurements, removed all invalid measurements")
            else:
                dataset = dataset.where(dataset.ge(0)).ffill()
        elif fmode == "backward fill":
            if (dataset.tail(1) < 0).any().any():
                dataset = dataset[dataset.select_dtypes(include=[np.number]).ge(0).all(1)]
                print("First row had invalid measurements, removed all invalid measurements")
            else:
                dataset = dataset.where(dataset.ge(0)).bfill()

        tvec = dataset.iloc[:, 0:6]
        data = dataset.iloc[:, 6:10]

        return tvec, data
    except IOError:
        print(f"File with name {filename} could not be loaded")
    except Exception:
        print("An unexpected error occurred")
