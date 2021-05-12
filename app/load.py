import numpy as np
import pandas as pd

'''
Created May 2021

Purpose: to load the data from the data folder

@author Mathias Fager, s175182
'''

def load_measurements(filename: str, fmode: str):
    '''
    Function to load the data from the data folder
    :param filename: The filename of the dataset to load from the data folder
    :param fmode: filling mode, whether to backward or forward fill
    :return: 2 datasets containing the timevectors and the data from the zones
    '''
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
