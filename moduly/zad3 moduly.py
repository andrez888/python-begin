from calculations import obliczanie_lokaty
print('Obliczanie wartosci lokaty\n')
value= float(input('Podaj wartość wkładu: '))
percent = float(input('Podaj procent lokaty: '))
year= float(input('Podaj na ile lat lokata: '))

result = obliczanie_lokaty(value, percent, year)

print(f'Twoja lokata bedzie miala wartość {result:.2f}')