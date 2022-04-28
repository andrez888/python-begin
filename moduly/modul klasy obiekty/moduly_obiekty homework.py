
# Dodaj konstruktor do klas Product, Order, Apple i Potato
# Product: nazwa, rodzaj, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślne pusta),
# łączna cena (obliczona w konstuktorze na jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg


class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price


class Order:

    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


# class Apple:
#
#     def __init__(self, species_name, size, price):
#         self.species_name = species_name
#         self.size = size
#         self.price = price
#
#
# class Potato:
#     def __init__(self, species_name, size, price):
#         self.species_name = species_name
#         self.size = size
#         self.price = price
def read_order(order):
    print(f'Zamówienie złożone przez {order.first_name} {order.last_name}')
    for produkt in order.products:
        print(produkt.name)
    print(f'Calkowity koszt {order.total_price} zl')
    for x in order.products:
        print(x.unit_price)
def read_product(product):
    print(f'Produkt:{product.name} kategoria:{product.category_name} cena:{product.unit_price} ')

def total_price(order):
    print(order.total_price)

def make_order(order,product):
    order.products.append(product)
    lista = order.products
    return lista

# def run_homework():
#     green_apple = Apple(species_name="Green", size="M", price=3.5)
#     red_apple = Apple(species_name="Red", size="S", price=2.8)
#     print(green_apple.species_name, green_apple)
#     print(red_apple.species_name, red_apple)
#
#     old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
#     print(old_potato.species_name, old_potato)
#
#     cookies = Product(name="Cookies", category_name="Food", unit_price=4)
#     empty_order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski")
#     order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", products=[cookies])
#     print(cookies)
#     print(empty_order)
#     print(order)
def run_example():
    produkt_1 = Product('perla', 'piwo', 2.99)
    zamowienie1 = Order('Jan', 'Kowalski')
    produkt_2 = Product('cisowianka','woda',1.2)
    zamowienie2 = Order('Jan','Kowalski',)
    make_order(zamowienie1,produkt_1)
    zamowienie=make_order(zamowienie1,produkt_2)
    read_order(zamowienie)
    print(zamowienie.total_price)
if __name__ == '__main__':
    # run_homework()
    # run_example()
    # produkt_1 = Product('perla', 'piwo', 2.99)
    # zamowienie1 = Order('andrzej','piontkowski',[produkt_1,produkt_1])
    # print(zamowienie1.total_price)
    zamowienie1 = Order('Jan', 'Kowalski')
    produkt_2 = Product('cisowianka', 'woda', 1.2)
    inna = make_order(zamowienie1,produkt_2)
    inna =make_order(zamowienie1,produkt_2)
    zamowienie2 = Order('jan','kowalski',inna)
    print(zamowienie2.total_price)

