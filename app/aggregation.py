import pandas as pd


class Periods:
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    HOUR_OF_THE_DAY = "hour of the day"


def aggregate_measurements(tvec: pd.DataFrame, data: pd.DataFrame, period: Periods):
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
