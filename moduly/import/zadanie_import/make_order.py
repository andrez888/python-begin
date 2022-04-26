from zadanie_import.Shop import shop
from zadanie_import.Shop import  aktualizacja_ilosci
orders=[]
def making_order(product_name,quantity):
    dostepna_ilosc = shop[product_name]['ilosc']
    total_price= quantity * shop[product_name]['cena']
    if quantity > dostepna_ilosc:
        print('Nie mamy takiej ilości towaru')
        return False

    new_order = {
        'product': product_name,
        'ilosc': quantity,
        'cena': total_price
    }

    aktualizacja_ilosci(product_name,quantity)
    orders.append(new_order)
    return new_order