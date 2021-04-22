import pandas as pd


def load_measurements(filename: str, fmode: str) -> pd.DataFrame:
    try:
        data = pd.read_csv("../data/" + filename)
        data.columns = ['year', 'month', 'day', 'hour', 'minute', 'second', 'zone1', 'zone2', 'zone3', 'zone4']
        return data
    except IOError:
        print(f"File with name {filename} could not be loaded")
    except Exception:
        print("An unexpected error occurred")


print(load_measurements("2008.csv", "")["year"])