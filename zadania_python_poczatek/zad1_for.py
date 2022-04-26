oceny=[]
ocena = int(input('Podaj swoja ocene: \t'))
while ocena != 'x':
    ocenka = int(ocena)
    oceny.append(ocenka)
    ocena = input('jesli chcesz kontynuowac wcisnij "x" albo podaj kolejna ocene\t')

suma = 0
for x in oceny:
    suma +=x
srednia = suma/ len(oceny)
print(f'Twoja srednia to {srednia:.2f}')


