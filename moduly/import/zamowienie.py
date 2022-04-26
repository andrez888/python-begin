from zadanie_import.Shop import shop
from zadanie_import.make_order import making_order
from zadanie_import.check_order import  check_order
if __name__ == '__main__':
        print('Witamy na naszej stronie')
        product_name = input("Podaj produkt, który chcesz zamówić:\t")
        if check_order(product_name):
            quantity = int(input(f'Podaj ilość {product_name} do zamówienia:\t'))
            wynik = making_order(product_name, quantity)

            cena = wynik['cena']
            print(f'do zapłaty {cena:.2f}')
    # print(f'Twoje zamowienie to {wynik}')
        else:
            print("I huj")



