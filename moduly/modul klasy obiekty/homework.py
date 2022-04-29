import random
class Product:
    def __init__(self,name,category,unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price
class Order:
    def __init__(self,first_name,last_name,products=None):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products=[]
        self.products = products
        total_cost = 0
        for produkt in products:
            total_cost += produkt.unit_price
        self.total_cost = total_cost
class Apple:
    def __init__(self,species_name,size,price):
        self.species_name = species_name
        self.size = size
        self.price = price
class Potatoe:
    def __init__(self,species_name,size,price):
        self.species_name = species_name
        self.size = size
        self.price = price
def describe_order(order):
    print(f'Zamówienie przyjęte od {order.first_name.title()} {order.last_name.title()}')
    print('Zamówione produkty:\n')
    for produkt in order.products:
        print(f'Nazwa:{produkt.name.title()} | Kategoria:{produkt.category.title()} | Cena:{produkt.unit_price}')
    print(f'\nCałkowity koszt zamówienia:\t{order.total_cost}')
def make_order(order,product):
    order.products.append(product)
    return order.products
def losowy_order():
    products = []
    number_product = random.randint(1,30)
    for produkt in range(number_product):
        name = f'produkt {produkt}'
        category = 'Inne'
        cena = random.randint(1,15)
        product= Product(name,category,cena)
        products.append(product)
    order= Order('andrzej','piontkowski',products)
    return order
def homework():
    perla = Product('perla','piwo',3.5)
    order1 = Order('andrzej','piontek')
    order2 = make_order(order1,perla)
    describe_order(order2)
def homework2():
    perla = Product('perla', 'piwo', 3.5)
    woda = Product('cisowianka', 'woda', 1.2)
    order1 = Order('andrzej', 'piontek')

    lista = make_order(order1, woda)
    make_order(order1, perla)
    make_order(order1, perla)

    zamowienie = Order('and', 'pio', lista)
    describe_order(zamowienie)
    losowe_zamowienie = losowy_order()
    describe_order(losowe_zamowienie)
if __name__ == "__main__":
   homework2()