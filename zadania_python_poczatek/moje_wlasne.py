print('Kalkulator wydatków')



wydatki = {}

while True:
    category_payment = input('Podaj kategorię wydatków : ')
    wydatki[category_payment]=[]
    if category_payment == 'x':
        break
    while True:
        pay = input(f'Podaj  kwote na {category_payment} lub wcisnij "x" zeby wyjsc: ')
        if pay == 'x':
            break
        payment = int(pay)
        wydatki[category_payment].append(payment)



suma_wydatkow = 0
for sum in wydatki.values():
    for suma in sum:
        suma_wydatkow+=suma
procentowe_wydatki = {}
for kategoria, procent in wydatki.items():
    total_procent =0
    for percent in procent:
        total_procent+= percent
        procentowe_wydatki[kategoria] = total_procent *100 / suma_wydatkow

most_important_category = None
most_important_percent = 0

for a,b in procentowe_wydatki.items():
    if b > most_important_percent:
        most_important_percent = b
        most_important_category = a

for x, y in procentowe_wydatki.items():
    print(f'Na {x} wydajesz {y:.2f} %')

print(f'Najwiecej az {most_important_percent:.2f} % wydajesz na {most_important_category}')
print(procentowe_wydatki)
maxe = max(procentowe_wydatki.values())
print(maxe)