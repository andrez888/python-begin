from shop.product import Product
from shop.order import make_order, describe_order, losowy_order,Order
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