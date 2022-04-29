import random
class Product:
    def __init__(self,name,category,unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price
class Order:
    def __init__(self,first_name,last_name,products = None):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products = []
        self.products = products
        total_price = 0
        for produkt in products:
            total_price += produkt.unit_price
        self.total_price = total_price

def make_order():
    products =[]
    ilosc = random.randint(1,50)
    for produkt in range(ilosc):
        name = f'produkt {produkt}'
        category = 'inne'
        unit_price = random.randint(1,30)
        zamowienie = Product(name,category,unit_price)
        products.append(zamowienie)
    order = Order('Andrzej','Piontkowski',products)
    return order
def describe_order(order):
    print('zamówienie')
    print('-'*20)
    print(f'Zamówienie {order.first_name} {order.last_name}')
    for produkt in order.products:
        print(f'Produkt:{produkt.name}| kategoria:{produkt.category}|cena:{produkt.unit_price}zł')
    print(f'Do zapłaty: {order.total_price}zł')

def run_homework():
    losowe_produkt = make_order()
    describe_order(losowe_produkt)
    losowy_produkt2 = make_order()
    describe_order(losowy_produkt2)
if __name__ == "__main__":
    run_homework()




