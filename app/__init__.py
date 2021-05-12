import sys
import pandas as pd
import tui
# import data_plot
import os
import platform

"""
Created May 2021

Purpose: The main script to navigate the program

@author Oliver Køppen, s175108
"""

data = None
fullDataSet = pd.DataFrame()


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


def options(option):
    return {
        'load': tui.loadDataMenu(),
        1: tui.loadDataMenu(),
        2: tui.startMenu(data)
    }[option]


while True:
    """
    The main loop controlling the navigation of the script
    """

    clear()

    if data is None:
        data = options('load')

    selected_item = tui.startMenu(data)
    # if type(selected_item) != int:
    #     data = selected_item
    # else:
    options(selected_item)
    #
    # if fullDataSet.empty:
    #     userInput = tui.startMenu(True)
    # else:
    #     userInput = tui.startMenu(False)
    # if userInput == 1:
    #     data = tui.loadDataMenu()
    #     fullDataSet = data
    # elif userInput == 2:
    #     if data.empty:
    #         print("Dataset is not loaded")
    #         input("Press enter to input dataset")
    #         data = tui.loadDataMenu()
    #         fullDataSet = data
    #     data = tui.filterMenu(data)
    # elif userInput == 3:
    #     if data.empty:
    #         print("Dataset is not loaded")
    #         input("Press enter to input dataset")
    #         data = tui.loadDataMenu()
    #         fullDataSet = data
    #     tui.statisticsMenu(data)
    # elif userInput == 4:
    #     if data.empty:
    #         print("Dataset is not loaded")
    #         input("Press enter to input dataset")
    #         data = tui.loadDataMenu()
    #         fullDataSet = data
    #     # data_plot.dataPlot(data)
    # elif userInput == 5:
    #     data = fullDataSet
    #     print("Filter reset")
    #     input("Press enter to continue")
    # elif userInput == 6:
    #     print(data)
    #     input("Press enter to continue")
    # elif userInput == 7:
    #     sys.exit(0)
    # else:
    #     print("Input could not compute, try again")
    #     input("Press enter to continue")
