shop= {
    'piwo':{'cena': 2.3,
            'ilosc': 1000},
    'woda':{'cena':1.50,
            'ilosc': 200}
}

def aktualizacja_ilosci(product_name,zamowiona_ilosc):
    shop[product_name]['ilosc'] -= zamowiona_ilosc

