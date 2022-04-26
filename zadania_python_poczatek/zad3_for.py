print('kalkulator wydatkow')
wydatki = {}
kategoria = input('Podaj kategorie swoich wydatkow albo jak chcesz skonczyc wpisz "x"')

while kategoria != 'x':
    wydatki[kategoria]= []
    wydatek = input(f'Podaj wartosc wydatkow dla {kategoria} albo zeby wyjsc wcisnij "x"')
    while wydatek != 'x':
        wydac = float(wydatek)
        wydatki[kategoria].append(wydac)
        wydatek = input(f'Podaj kolejne wydatki na kategorie {kategoria} albo zakoncz (x)')
    kategoria = input('Podaj kolejna kategorie lub jak chcesz skonczyc wcisnij "x"')
print(wydatki)

total_wydatkow = 0
for y in wydatki.values():
    for x in y:
        total_wydatkow += x
procentowe_wydatki = {}
for a,b in wydatki.items():

    total_b = 0
    for bi in b:
        total_b +=bi
    procentowe_wydatki[a] =total_b * 100 / total_wydatkow

most_kategoria = None
most_money = 0

for n,m in procentowe_wydatki.items():
    if m > most_money:
        most_money = m
        most_kategoria = n
for o,p in procentowe_wydatki.items():
    print(f'Na {o} wydajesz procentowo {p:.2f} %')
print(f'Najwiecej wydajesz na {most_kategoria} {most_money:.2f} % ')


