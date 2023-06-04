from tabulate import tabulate


def table(data: dict):
    column1 = (list(data.keys()))
    column2 = (list(data.values()))

    headers = ['Values', 'Options']

    table = list(filter(lambda x: x[1] is not None, zip(column1, column2)))

    print(tabulate(table, headers, tablefmt='mixed_grid', stralign='center'))
