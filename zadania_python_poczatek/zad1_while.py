number = 1
numer = int(input('podaj liczbe: '))

while number < 10 and numer % 2 !=0:

    print(f'Zła liczba {numer}')
    numer = int(input('Podaj inna liczbe: '))
    number += 1
print('udalo sie :)')