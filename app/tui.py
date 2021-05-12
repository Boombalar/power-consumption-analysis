import pandas as pd

import load
import statistics
from termcolor import colored
# Need this module for colors to work
import colorama
import aggregation

# Init the module so it works
colorama.init()
"""
Created May 2021

Purpose: to extract the navigation from __init__.py into helper methods to keep the main script less crowded

@author Oliver Køppen, s175108
"""


def startMenu(data: tuple) -> int:
    """
    The start menu used to print all the options from the start menu
    :param data: Boolean to whether load simple menu or advanced menu
    :return: the number corresponding to the selected menu choice
    """

    try:
        if data is None:
            print(colored("1", "blue") + " Load data")
        else:
            print(colored("1", "blue") + " Reload data")
            print(colored("2", "blue") + " Aggregate data")
            print(colored("3", "blue") + " Display statistics")
            print(colored("4", "blue") + " Visualize electricity consumption")
        print(colored("9", "red") + " EXIT")
        return int(input("What do you wish to do? \n"))
    except ValueError:
        print("Input could not compute, try again")
        input("Press enter to continue")


corruption_mode = {
    "1": 'forward fill',
    "2": 'backward fill',
    "3": 'drop'
}


def loadDataMenu() -> tuple:
    """
    Method for printing the option to load the dataset, if no selected dataset, use the test.txt in the data folder
    :return: The dataset in the from of a DataFrame type.
    """
    default_file = "2008.csv"
    print("No data is currently loaded.")
    print(default_file + " is loaded.")
    print("How should corrupted measurement be handled?")
    print(colored("1", "blue") + " Forward Fill - Replace with latest valid measurement")
    print(colored("2", "blue") + " Backward Fill - Replace with next valid measurement")
    print(colored("3", "blue") + " Drop - Deleted corrupted measurement")
    fmode = input("Choose one")
    try:
        mode = corruption_mode[fmode]
        data = load.load_measurements(default_file, mode)
        print(colored("Data was loaded successfully", "green"))
        return data
    except Exception:
        print(colored("Data could not be loaded successfully", "red"))


aggregation_mode = {
    "1": None,
    "2": aggregation.Periods.HOUR,
    "3": aggregation.Periods.DAY,
    "4": aggregation.Periods.MONTH,
    "5": aggregation.Periods.HOUR_OF_THE_DAY,
}


def aggregateDataMenu(data: tuple):
    print("How should the data be aggregated?")
    print(colored("1", "blue") + " Consumption per minute (no aggregation)")
    print(colored("2", "blue") + " Consumption per hour")
    print(colored("3", "blue") + " Consumption per day")
    print(colored("4", "blue") + " Consumption per month")
    print(colored("5", "blue") + " Hour-of-day consumption (hourly average)")
    amode = input("Choose one")
    try:
        mode = aggregation_mode[amode]
        data = aggregation.aggregate_measurements(data[0], data[1], mode)
        print(colored("Data was aggregated", "green"))
        return data, mode
    except Exception as e:
        print(e)
        print(colored("Data could not be aggregated", "red"))
