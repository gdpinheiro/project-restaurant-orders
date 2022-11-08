from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []
        for order in self.orders:
            if order[0] == customer:
                customer_orders.append(order[1])
        return Counter(customer_orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        dishes = set()
        customer_orders = set()
        for order in self.orders:
            if order[1] not in dishes:
                dishes.add(order[1])
            if order[0] == customer:
                customer_orders.add(order[1])
        return dishes.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        customer_days = set()
        for order in self.orders:
            if order[2] not in days:
                days.add(order[2])
            if order[0] == customer:
                customer_days.add(order[2])
        return days.difference(customer_days)

    def get_busiest_day(self):
        customer_orders = []
        for order in self.orders:
            customer_orders.append(order[2])
        return Counter(customer_orders).most_common()[0][0]

    def get_least_busy_day(self):
        customer_orders = []
        for order in self.orders:
            customer_orders.append(order[2])
        counted_days = Counter(customer_orders).most_common()
        return counted_days[len(counted_days) - 1][0]
