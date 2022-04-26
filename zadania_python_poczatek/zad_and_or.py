kredyt= float(input('Podaj kwote kredytu:\t\t '))
oprocentowanie= float(input('Podaj oprocentowanie kredytu:\t '))
wklad= float(input('Podaj kwote wkladu własnego:\t '))
okres= float(input('Podaj okres kredytu w latach:\t\t '))
przychod= float(input('Podaj swój przychód:\t '))
wydatki= float(input('Podaj sumę miesięcznych wydatków:\t '))

rata = (kredyt * oprocentowanie /100) /12 + kredyt/(okres*12)
dostepne_srodki = przychod - wydatki
print(rata)
wartosc_mieszkania = wklad + kredyt

procent_wkladu = (wklad/wartosc_mieszkania)*100
print(procent_wkladu)
print(dostepne_srodki)
if procent_wkladu > 20 and dostepne_srodki >= rata + 1000 :
    print('congratulations')
else:
    if 10 < procent_wkladu <= 20 and dostepne_srodki > rata + 2000:
        print('udalo ci sie dostales kredyt')
    else:
        print('nie udalo sie')






