import pandas as pd

import load
import statistics
from termcolor import colored
# Need this module for colors to work
import colorama

# Init the module so it works
colorama.init()
"""
Created May 2021

Purpose: to extract the navigation from __init__.py into helper methods to keep the main script less crowded

@author Oliver Køppen, s175108
"""


# def startMenu(data_loaded: bool) -> int:
def startMenu(data: tuple) -> int:
    """
    The start menu used to print all the options from the start menu
    :param data: Boolean to whether load simple menu or advanced menu
    :return: the number corresponding to the selected menu choice
    """
    # if data.isnull:
    #     print("No data is currently loaded.")
    #     input(colored("ENTER", "blue") + " Load data")
    #     return 1

        # if data:
        #     input("Press enter to load data")
        #     return 1
        # while True:
    try:
        print(colored("1", "blue") + " Load data")
        print(colored("2", "blue") + " filter data")
        print(colored("3", "blue") + " displaying statistics")
        print(colored("4", "blue") + " generate plots")
        print(colored("5", "blue") + " reset filter")
        print(colored("6", "blue") + " to print data")
        print(colored("7 EXIT", "red"))
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
    # if data is None:
    print("No data is currently loaded.")
    print(default_file + " is loaded.")
    # else:
    #     print("Resetting ")
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
    # filename = input("Please enter the filename you wish to load, default is 'test.txt' \n")
    # if filename:
    #     print("Loading: " + filename)
    #     return load.load_measurements(filename)
    # else:
    #     print("Loading: " + default_file + " (Default)")
    #     return load.load_measurements(default_file)

#
# def filterMenu(data: pd.DataFrame) -> pd.DataFrame:
#     """
#     Method for printing the options for filtering the dataset
#     :param data: The dataset where a filter is to be set
#     :return: The filtered dataset
#     """
#     while True:
#         try:
#             print(colored("1", "blue") + " filter by bacteria type")
#             print(colored("2", "blue") + " interval of growth rate")
#             print(colored("3", "blue") + " BACK")
#             userInput = int(input("What do you wish to do? \n"))
#             break
#         except ValueError:
#             print("Input could not compute, try again")
#             input("Press enter to continue")
#     if userInput == 1:
#         return filterBacteriaMenu(data)
#     elif userInput == 2:
#         return filterIntervalGrowthRate(data)
#     # Special case if the user goes back to keep the dataset untouched
#     elif userInput == 3:
#         return data
#     else:
#         print("Input could not compute, try again")
#         input("Press enter to continue")
#
#
# def filterBacteriaMenu(data: pd.DataFrame):
#     """
#     Method for printing the options for filtering by bacteria
#     :param data: The dataset to filter
#     :return: The filtered dataset
#     """
#     while True:
#         try:
#             print(colored("1", "blue") + " Salmonella Enterica")
#             print(colored("2", "blue") + " Bacillus Cereus")
#             print(colored("3", "blue") + " Listeria")
#             print(colored("4", "blue") + " Brochothrix Thermosphacta")
#             bacteria = int(input("Choose bacteria \n"))
#             if 1 <= bacteria <= 4:
#                 break
#         except ValueError:
#             print("Input could not compute, try again")
#             input("Press enter to continue")
#     return data[data['bacteria'] == bacteria]
#
#
# def filterIntervalGrowthRate(data):
#     """
#     Method for printing the options for filtering between an interval of growth rates
#     :param data: The dataset to filter
#     :return: the filtered dataset
#     """
#     while True:
#         try:
#             lowerboundGR = float(input("Please enter lowerbound growth rate\n"))
#             upperboundGR = float(input("Please enter upperbound growth rate\n"))
#             break
#         except ValueError:
#             print("Input could not be compute, try again")
#             input("Press enter to continue")
#     return data[(data['growth'] >= lowerboundGR) & (data['growth'] <= upperboundGR)]
#
#
# def statisticsMenu(data):
#     """
#     Method for printing all the options for printing the statistical values
#     :param data: The dataset to caclulate statistical values from
#     :return: returns nothing, used to exit the method
#     """
#     while True:
#         while True:
#             try:
#                 print(colored("1", "blue") + " mean temperature")
#                 print(colored("2", "blue") + " growth rate")
#                 print(colored("3", "blue") + " standard deviation of the temperature")
#                 print(colored("4", "blue") + " standard deviation of the growth rate")
#                 print(colored("5", "blue") + " amount of rows in the dataset")
#                 print(colored("6", "blue") + " mean growth rate with temperature below 20")
#                 print(colored("7", "blue") + " mean growth rate with temperature above 50")
#                 print(colored("8", "blue") + " BACK")
#                 statistic = int(input("Which statistic do you want? \n"))
#                 break
#             except ValueError:
#                 print("Input could not compute, try again")
#                 input("Press enter to continue")
#
#         if statistic == 1:
#             print("The mean temperature is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.MEAN_TEMPERATURE)))
#             input("Press enter to continue")
#         elif statistic == 2:
#             print("The mean growth rate is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.MEAN_GROWTH_RATE)))
#             input("Press enter to continue")
#         elif statistic == 3:
#             print("The standard deviation of the temperature is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.STD_TEMPERATURE)))
#             input("Press enter to continue")
#         elif statistic == 4:
#             print("The standard deviation of the growth rate is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.STD_GROWTH_RATE)))
#             input("Press enter to continue")
#         elif statistic == 5:
#             print("The amount of rows in the dataset is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.ROWS)))
#             input("Press enter to continue")
#         elif statistic == 6:
#             print("The mean growth rate with temperature below 20 is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.MEAN_COLD_GROWTH_RATE)))
#             input("Press enter to continue")
#         elif statistic == 7:
#             print("The mean growth rate with temperature above 50 is " + str(
#                 data_statistics.dataStatistics(data, data_statistics.StatisticType.MEAN_HOT_GROWTH_RATE)))
#             input("Press enter to continue")
#         elif statistic == 8:
#             return
#         else:
#             print("Input did not compute, try again")
#             input("Press enter to continue")
