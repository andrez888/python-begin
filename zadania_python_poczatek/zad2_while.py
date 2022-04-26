number = input('Podaj numer telefonu: ')
number = number.replace('-','')
count = 0
formated_number = ''
while count < len(number):
    if count % 3 == 0 and count != 0:
        formated_number += '-'
    formated_number += number[count]
    count += 1
print(formated_number)
print(formated_number[0])