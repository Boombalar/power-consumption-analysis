import matplotlib.pyplot as plt
import pandas as pd

''' 
Created May 2021 

Purpose: to show plots of the data 

@author Mathias Fager, s175182 
'''


def plot(tvec: pd.DataFrame, data: pd.DataFrame, combineZones: bool):
    '''
    Function to plot the data
    :param tvec: Time vector for all the data measurements
    :param combineZones: Whether or not to sum all the zones into 1 value
    :param data: The data to plot
    :return: Does not return anything, will show a plot on the screen.
    '''
    if tvec.empty or data.empty:
        raise Exception("The dataset is empty")
    x = pd.to_datetime(tvec)
    if combineZones:
        if len(data) < 25:
            plt.bar(x, data.sum(axis=1), width=12)
        else:
            plt.plot(x, data.sum(axis=1))
        plt.xlabel("Time")
        plt.ylabel("Consumption (Wh)")
        plt.title("Energy consumption (all zones)")
        plt.show()
    else:
        for column in data:
            if len(data) < 25:
                plt.bar(x, data[column], width=12)
            else:
                plt.plot(x, data[column])
            plt.xlabel("Time")
            plt.ylabel("Consumption (Wh)")
            plt.title(f"Energy consumption ({column})")
            plt.show()
