from typing import Union


class Customer:
    def __init__(self, email: str, customers_name="", tax_percent=2):
        self.total_price = None
        self.email = email
        self.customers_name = customers_name
        self.tax_percent = tax_percent

    def total_amount(self, price):
        self.total_price = price + price * self.tax_percent / 100
        return self.total_price


class LoyalCustomer(Customer):
    def __init__(self, email: str, customers_name=""):
        super().__init__(email, customers_name)
        self.tax_percent = 1


class Flat:
    def __init__(self, flat_price: float, flat_address: str):
        self.flat_price = flat_price
        self.flat_address = flat_address


class RealEstateCompany:
    def __init__(self, clients: list, flats: list):
        self.cheapest_flat = None
        self.flats = flats
        self.clients = clients

    def cheapest(self):
        cheapest_price = float("inf")
        for flat in self.flats:
            if flat.flat_price < cheapest_price:
                cheapest_price = flat.flat_price
        return cheapest_price

    def sell(self, flat: Flat, client: Union[Customer, LoyalCustomer]):
        print(f"Flat address: {flat.flat_address}")
        print(f"Customer email: {client.email}")
        print(f"Customer name: {client.customers_name}")
        print(f"Total amount paid: {client.total_amount(self.cheapest())}")
        self.flats.remove(flat)


customer_1 = Customer("a@b.com", "Darius", 3)
customer_2 = Customer("c@b.com", "Oskaras")
customer_3 = Customer("e@b.com")

customer_1.total_amount(100000)

loyal_customer_1 = LoyalCustomer("loyal@l.com", "Laurynas")
loyal_customer_2 = LoyalCustomer("love@l.com")

loyal_customer_1.total_amount(100000)

flat_1 = Flat(130000, "Sodu 4")
flat_2 = Flat(150000, "Barbaru 12")
flat_3 = Flat(120000, "Ponu 13")

customers_list = [customer_1, customer_2, loyal_customer_1]
flats_list = [flat_1, flat_2, flat_3]

instance = RealEstateCompany(clients=customers_list, flats=flats_list)
instance.sell(flat=flat_3, client=customer_1)
instance.sell(flat=flat_1, client=loyal_customer_1)
