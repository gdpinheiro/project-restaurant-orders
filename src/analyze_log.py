import csv
from collections import Counter


def most_ordered_by_maria(orders):
    maria_orders = []

    for order in orders:
        if order[0] == "maria":
            maria_orders.append(order[1])

    return Counter(maria_orders).most_common()[0][0]


def arnaldo_ordered_hamburger(orders):
    arnaldo_orders = []

    for order in orders:
        if order[0] == "arnaldo":
            arnaldo_orders.append(order[1])

    return Counter(arnaldo_orders)["hamburguer"]


def joao_never_ordered(orders):
    dishes = set()
    joao_orders = set()

    for order in orders:
        if order[1] not in dishes:
            dishes.add(order[1])
        if order[0] == "joao":
            joao_orders.add(order[1])

    return dishes.difference(joao_orders)


def joao_never_weekday(orders):
    days = set()
    joao_days = set()

    for order in orders:
        if order[2] not in days:
            days.add(order[2])
        if order[0] == "joao":
            joao_days.add(order[2])

    return days.difference(joao_days)


def write_to_file(result):
    with open("./data/mkt_campaign.txt", "w", encoding="utf-8") as file:
        for line in result:
            file.write(str(line))
            file.write("\n")


def check_path(path):
    if path.endswith("csv"):
        return
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path}'")


def analyze_log(path_to_file):
    check_path(path_to_file)
    try:
        orders = []

        with open(path_to_file, encoding="utf-8") as file:
            orders_reader = csv.reader(file, delimiter=",", quotechar='"')
            for row in orders_reader:
                orders.append(row)

        result = []
        result.append(most_ordered_by_maria(orders))
        result.append(arnaldo_ordered_hamburger(orders))
        result.append(joao_never_ordered(orders))
        result.append(joao_never_weekday(orders))

        write_to_file(result)

        return print(result)
    except IOError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


analyze_log("./data/orders_1.csv")
