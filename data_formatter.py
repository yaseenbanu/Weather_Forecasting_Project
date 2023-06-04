def format(data: dict, unit='metric'):

    units = {
        'standard': ['K', 'K', 'hPa', '%', 'K', 'K', 'hPa', 'hPa'],
        'metric': ['°C', '°C', 'hPa', '%', '°C', '°C', 'hPa', 'hPa'],
        'imperial': ['°F', '°F', 'hPa', '%', '°F', '°F', 'hPa', 'hPa']
    }

    data['Temperature'] = data.pop('temp', None)
    data['Feels Like'] = data.pop('feels_like', None)
    data['Pressure'] = data.pop('pressure', None)
    data['Humidity'] = data.pop('humidity', None)
    data['Minimum Temperature'] = data.pop('temp_min', None)
    data['Maximum Temperature'] = data.pop('temp_max', None)
    data['Sea Level'] = data.pop('sea_level', None)
    data['Ground Level'] = data.pop('grnd_level', None)

    for index, key in enumerate(data):
        if data[key] is not None:
            data[key] = str(data[key]) + units[unit][index]

    return data
