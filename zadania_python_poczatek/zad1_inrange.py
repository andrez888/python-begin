number = input('Podaj swoj nr telefonu: \t')

for x in range(10):
    ilosc = number.count(str(x))
    print(f'Cyfra {x} znajduje sie w numerze {ilosc} razy')
