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
    if isinstance(tvec, pd.Index):
        x = tvec
        xLabel = f"Time ({x.name})"
    else:
        x = pd.to_datetime(tvec)
        xLabel = "Time (default)"
    if combineZones:
        if len(data) < 25:
            plt.bar(x, data.sum(axis=1))
        else:
            plt.plot(x, data.sum(axis=1))
        plt.xlabel(xLabel)
        plt.ylabel("Consumption (Wh)")
        plt.title("Energy consumption (all zones)")
        plt.show()
    else:
        fig, axs = plt.subplots(2, 2, figsize=(16, 10))
        axs = axs.flatten()
        for index, column in enumerate(data):
            if len(data) < 25:
                axs[index].bar(x, data[column])
                axs[index].set(xlabel=xLabel, ylabel="Consumption (Wh)")
                axs[index].set_title(f"Energy consumption ({column})")
            else:
                axs[index].plot(x, data[column])
                axs[index].set(xlabel=xLabel, ylabel="Consumption (Wh)")
                axs[index].set_title(f"Energy consumption ({column})")
        plt.show()
