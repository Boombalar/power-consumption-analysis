import load
from termcolor import colored
# Need this module for colors to work
import colorama
import aggregation
import visuals

# Init the module so it works
colorama.init()
"""
Created May 2021

Purpose: to extract the navigation from __init__.py into helper methods to keep the main script less crowded

@author Oliver Køppen, s175108
"""


def allowed_selection(selection: str, allowed: list) -> None:
    """
    Raises #InvalidSelectionException if the input is not among the allowed list
    :param selection: user input as string
    :param allowed: allowed user inputs as list of int
    """
    for item in allowed:
        if selection == str(item):
            return None
    raise InvalidSelectionException


def startMenu(data: tuple) -> int:
    """
    The start menu used to print all the options from the start menu
    :param data: (optional) loaded data containing tvec and data
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
        selection = input("What do you wish to do? \n")
        allowed_selection(selection, [1, 2, 3, 4, 9])
        return int(selection)
    except InvalidSelectionException:
        print(colored("Invalid selection", "red"))
    except ValueError:
        print("Input could not compute, try again")
        input("Press enter to continue")


def loadDataMenu() -> tuple:
    """
    Loads user defined csv file located in /data folder
    :return: The data set as a tuple containing tvec (index 0) and the data (index 1).
    """
    default_file = "2008.csv"
    print("No data is currently loaded.")
    file_name = input("Enter name of file followed or ENTER for default (" + default_file + ")")
    print(file_name or default_file + " is loaded.")
    print("How should corrupted measurement be handled?")
    print(colored("1", "blue") + " Forward Fill - Replace with latest valid measurement")
    print(colored("2", "blue") + " Backward Fill - Replace with next valid measurement")
    print(colored("3", "blue") + " Drop - Deleted corrupted measurement")
    try:
        fmode = input("Choose one")
        allowed_selection(fmode, [1, 2, 3])
        mode = corruption_modes[fmode]
        data = load.load_measurements(file_name or default_file, mode)
        if data is None:
            raise Exception
        print(colored("Data was loaded successfully", "green"))
        return data
    except InvalidSelectionException:
        print(colored("Invalid selection", "red"))
    except Exception:
        print(colored("Data could not be loaded successfully", "red"))


def visualsMenu(data):
    try:
        print("How should the energy consumption be visualized?")
        print(colored("1", "blue") + " Individual zones")
        print(colored("2", "blue") + " Combined zones")
        combined = input("Choose one")
        allowed_selection(combined, [1, 2])
        visuals.plot(data[0], data[1], True if combined == "2" else False)
    except InvalidSelectionException:
        print(colored("Invalid selection", "red"))


def aggregateDataMenu(data: tuple) -> tuple:
    """
    The menu to allow the user to pick an aggregation
    :param data:
    :type data: tuple containing tvec and data
    :return: data: tuple containing aggregated tvec and data
    """
    print("How should the data be aggregated?")
    print(colored("1", "blue") + " Consumption per minute (no aggregation)")
    print(colored("2", "blue") + " Consumption per hour")
    print(colored("3", "blue") + " Consumption per day")
    print(colored("4", "blue") + " Consumption per month")
    print(colored("5", "blue") + " Hour-of-day consumption (hourly average)")
    try:
        amode = input("Choose one")
        allowed_selection(amode, [1, 2, 3, 4, 5])
        mode = aggregation_modes[amode]
        data = aggregation.aggregate_measurements(data[0], data[1], mode)
        print(colored("Data was aggregated", "green"))
        return data
    except InvalidSelectionException:
        print(colored("Invalid selection", "red"))
    except Exception as e:
        print(e)
        print(colored("Data could not be aggregated", "red"))


corruption_modes = {
    "1": 'forward fill',
    "2": 'backward fill',
    "3": 'drop'
}


aggregation_modes = {
    "1": None,
    "2": aggregation.Periods.HOUR,
    "3": aggregation.Periods.DAY,
    "4": aggregation.Periods.MONTH,
    "5": aggregation.Periods.HOUR_OF_THE_DAY,
}


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidSelectionException(Error):
    """Raised when input is invalid"""
    pass
