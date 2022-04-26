from zadanie_import.Shop import shop
from zadanie_import.make_order import making_order
def check_order(product_name):
    if product_name in shop.keys():
        return True




    else:

        return False