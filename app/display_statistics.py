import pandas as pd
from tabulate import tabulate

"""
Created May 2021

Purpose: Display statistics of the quantiles

@author Oliver Køppen, s175108
"""


def get_quantiles(data) -> []:
    """
    Return list of quantiles of data
    :param data:
    :return:
    """
    data_quantiles = []
    quantiles = [0, .25, .50, .75, 1]  # Add more quantiles if needed
    for quantile in quantiles:
        data_quantiles.append(data.quantile(quantile))
    data_quantiles.append(str(len(data)))
    return data_quantiles


def print_statistics(tvec, data) -> None:
    """
    Prints percentiles for each zone
    @Author: Oliver Storm Køppen s175108
    :param tvec:  An N × 6 matrix where each row is a time vector.
    :param data: An N × 4 matrix where each row is a set of measurements.
    :param aggregation: (optional) Aggregation period
    :return: None
    """
    table_data = [
        get_quantiles(data["zone1"]),
        get_quantiles(data["zone2"]),
        get_quantiles(data["zone3"]),
        get_quantiles(data["zone4"])
    ]
    columns = [
        'Minimum\nWh',
        '1. quart.\nWh',
        '2. quart.\nWh',
        '3. quart.\nWh',
        'Maximum\nWh',
        '\nn'
    ]
    index = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'All Zones']
    table_data.append(get_quantiles(data["zone1"].append(data["zone2"]).append(data["zone3"]).append(data["zone4"])))
    table_data = pd.DataFrame(table_data, index, columns)
    print(tabulate(table_data, headers=columns, tablefmt='pretty'))
    try:
        print("The table shows consumption per " + tvec.name)
    except AttributeError:
        print("The table shows consumption per minute")
