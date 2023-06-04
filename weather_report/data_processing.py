import numpy as np
import pandas as pd
import json


def etl():
    raw_data = pd.read_csv('weather_report/data/iso_3166_country_codes.csv')

    raw_data["alpha-2"].fillna("NA", inplace=True)

    data = raw_data[['name', 'alpha-2']].to_numpy()

    data[:, 0] = np.vectorize(str.casefold)(data[:, 0])

    cached_data = dict(data)

    with open("weather_report/data/cache.json", "w") as outfile:
        json.dump(cached_data, outfile)


if __name__ == '__main__':
    etl()
