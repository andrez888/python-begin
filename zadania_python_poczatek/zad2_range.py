kwota = int(input('Jaka jest kwota Twojego kredytu:\t'))
oprocentowanie = int(input('Podaj oporcentowanie kredytu:\t'))
time = int(input('Podaj czas kredytowania w latach: \t '))
begin_cost = int(input('Miałas jakieś koszty początkowe jak prowizaj itp. \t'))

czas = time * 12
all_cost = begin_cost
month_pay = kwota / czas
for month_number in range(1,czas+1):

    left_to_pay = kwota - (month_number -1)*month_pay

    rata = (left_to_pay*oprocentowanie/100)/12 + month_pay
    all_cost+=rata
    if month_number ==1:
        print(f'Rata w {month_number} miesiacu wyniesie {rata:.2f}')
    else:
        print(f'Rata po {month_number} miesiącach wyniesie {rata:.2f}')
total_cost =f'{all_cost:.2f}'
print(total_cost)

