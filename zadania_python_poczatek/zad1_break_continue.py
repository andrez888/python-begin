przedmioty = input('podaj przedmioty po przecinku:\t')

lista = przedmioty.split(',')
oceny = []
for x in lista:
    ocena = input(f'Podaj jaką masz ocene z {x}')
    oceny.append(ocena)
for jeden in oceny:
    if jeden == '1':
        print('Nie zdales losiu')
        break
else:
    print('Congratulations')