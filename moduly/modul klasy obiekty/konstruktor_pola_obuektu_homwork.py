class Product:
    def __init__(self,name,category_name,price):
        self.price = price
        self.category_name = category_name
        self.name = name
class Order:
    def __init__(self,name,surname,order_list=None):

        self.surname = surname
        self.name = name
        if order_list is None:
            order_list = []
        self.order_list = order_list
        total_price = 0
        for order in order_list:
            total_price += order.price
        self.total_price = total_price


class Apple:
    def __init__(self,nazwa_gatunku,size,price):
        self.nazwa_gatunku = nazwa_gatunku
        self.size = size
        self.price = price
class Potatoe:
    def __init__(self,nazwa_gatunku,size,price):
        self.nazwa_gatunku = nazwa_gatunku
        self.size = size
        self.price = price
def run_homework():
    green_apple = Apple("green",6,3.5)
    red_apple = Apple("red",5,4.5)
    print(red_apple.nazwa_gatunku, red_apple)
    print(green_apple.nazwa_gatunku, green_apple)
    cola = Product('cola','napój',3.5)
    print(cola.name,cola.category_name,cola.price)
    piwo=Product('perła','napój',2.99)
    print(f'Najlepsze piwo to {piwo.name} w cenie {piwo.price}')
    order1 =Order('andrzej','piontek')
    print(f'zamowienie nr 1 od {order1.name.title()} {order1.surname.title()}')


run_homework()