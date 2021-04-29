import pandas as pd


def aggregate_measurements(tvec: pd.DataFrame, data: pd.DataFrame, period: str):
    dataset = pd.concat([tvec, data], axis=1)
    if period == "hour of the day":
        data_a = dataset.groupby("hour").mean()
        data_a = data_a.iloc[:, 5:10]
        tvec_a = data_a.index
    else:
        dataset = dataset.groupby(period).sum()
        tvec_a = dataset.index
        data_a = dataset.iloc[:, 5:10]

    return tvec_a, data_a
