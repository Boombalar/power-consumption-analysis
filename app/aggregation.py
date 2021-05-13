import pandas as pd

'''
Created May 2021

Purpose: to aggregate data based on user input

@author Mathias Fager, s175182
'''


class Periods:
    '''
    class to avoid strings in the aggregate_measurements method
    '''
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    HOUR_OF_THE_DAY = "hour of the day"


def aggregate_measurements(tvec: pd.DataFrame, data: pd.DataFrame, period: Periods):
    '''
    Function to aggregate data, if hour is chosen the result is mean, else it's the sum
    :param tvec: time vector with all the different times measurements
    :param data: dataset containing the data from all the zones
    :param period: class that contains the different period options
    :return: a timevector and the data aggregated
    '''
    dataset = pd.concat([tvec, data], axis=1)
    if period == Periods.HOUR_OF_THE_DAY:
        data_a = dataset.groupby("hour").mean()
        data_a = data_a.iloc[:, 5:10]
        tvec_a = data_a.index
    else:
        dataset = dataset.groupby(period).sum()
        tvec_a = dataset.index
        data_a = dataset.iloc[:, 5:10]

    return tvec_a, data_a
