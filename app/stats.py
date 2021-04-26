import load
import pandas as pd
from tabulate import tabulate


def get_quantiles(data) -> []:
    data_quantiles = []
    quantiles = [0, .25, .50, .75, 1] # Add more quantiles if needed
    for quantile in quantiles:
        data_quantiles.append(data.quantile(quantile))
    data_quantiles.append(len(data))
    return data_quantiles


def print_statistics(tvec, data) -> None:
    '''
    Prints percentiles for each zone
    @Author: Oliver Storm Køppen s175108
    :param tvec:  An N × 6 matrix where each row is a time vector.
    :param data: An N × 4 matrix where each row is a set of measurements.
    :return: None
    '''
    table_data = []
    table_data.append(get_quantiles(data["zone1"]))
    table_data.append(get_quantiles(data["zone2"]))
    table_data.append(get_quantiles(data["zone3"]))
    table_data.append(get_quantiles(data["zone4"]))
    columns = ['Minimum', '1. quart.', '2. quart.', '3. quart.', 'Maximum', 'n']
    index = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'All Zones']
    table_data.append(get_quantiles(data["zone1"].append(data["zone2"]).append(data["zone3"]).append(data["zone4"])))
    table_data = pd.DataFrame(table_data, index, columns)
    print(tabulate(table_data, headers=columns, tablefmt='psql'))



print_statistics("test", load.load_measurements("2008.csv", ""))