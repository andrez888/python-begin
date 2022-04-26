from zadanieimport.funkcja2 import create_new_order
from zadanieimport.funkcja2 import orders
print("Witaj w naszym sklepie!")
product_name = input("Jaki towar chcesz kupić? ")
quantity = int(input("Ile sztuk/kg chcesz kupić? "))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"Łączny koszt wyniesie: {total_price} PLN")
else:
    print('Nie mamy takiego towaru')
