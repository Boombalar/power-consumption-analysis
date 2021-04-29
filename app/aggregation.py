import pandas as pd


class periods:
    hour = "hour"
    day = "day"
    month = "month"
    hour_of_the_day = "hour of the day"


def aggregate_measurements(tvec: pd.DataFrame, data: pd.DataFrame, period: periods):
    dataset = pd.concat([tvec, data], axis=1)
    if period == periods.hour_of_the_day:
        data_a = dataset.groupby("hour").mean()
        data_a = data_a.iloc[:, 5:10]
        tvec_a = data_a.index
    else:
        dataset = dataset.groupby(period).sum()
        tvec_a = dataset.index
        data_a = dataset.iloc[:, 5:10]

    return tvec_a, data_a
