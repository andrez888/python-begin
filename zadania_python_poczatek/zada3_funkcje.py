print('Kalkulator wydatków')

def slownik_wydatkow():
    wydatki = {}
    while True:
        kategoria = input('Podaj kategorię wydatków, jak chcesz skończyć wciśnij "x"\t')
        if kategoria == 'x':
            return wydatki
        wydatki[kategoria] = wartosci_slownika(kategoria)

def wartosci_slownika(kategoria):
    koszta= []
    while True:
        pay = input(f'Podaj koszta {kategoria}, jeśli chcesz skończyc wcisnij "n" \t')
        if pay == 'n':
            return koszta
        payment = int(pay)
        koszta.append(payment)

def suma_wydatkow(wydatki):
    suma_wydatkow = 0
    for suma in wydatki.values():
        suma_wydatkow += sum(suma)
    return suma_wydatkow

def procentowy_slownik(wydatki,calosc_wydatkow):
    procentowe_wydatki = {}
    for category,percent in wydatki.items():
        total_percent = sum(percent)
        procentowe_wydatki[category]= (total_percent*100)/calosc_wydatkow
    return procentowe_wydatki

def found_big_percent(procentowe_wydatki):
    the_most_percent = 0
    the_most_category = None
    for x,y in procentowe_wydatki.items():
        if y > the_most_percent:
            the_most_percent = y
            the_most_category = x
    return  the_most_percent,the_most_category

def describe_procent_naco(category,percent):
    print(f'Na {category} przeznaczasz {percent} %')

def najwiekszy_procent(x,y):
    print(f'Najwiecej wydajesz na {y} bo az {x:.2f} %')

wynik = slownik_wydatkow()




suma_wszustkich_wydatkow = suma_wydatkow(wynik)
procentowy_slownik = procentowy_slownik(wynik,suma_wszustkich_wydatkow)
a,b = found_big_percent(procentowy_slownik)
najwiekszy_procent(a,b)
for i,o in wynik.items():
    describe_procent_naco(i,o)



