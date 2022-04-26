import math as m
print('Obliczanie przeciprostokątenj trójkata\n')
while True:
    bok_1 = float(input('Podaj długośc pierwszej przyprostokątnej:\t'))
    bok_2 = float(input('Podaj długośc drugiej przyprostokątnej:\t'))
    result = m.sqrt(m.pow(bok_1,2) + m.pow(bok_2,2))
    wynik = input(f'Twój wynik to {result}, chcesz obliczyć inną (t/n):\t')
    if wynik == 'n':
        print('Dziękujemy za zabawę')
        break