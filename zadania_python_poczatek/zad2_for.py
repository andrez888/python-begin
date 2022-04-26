number = input('Podaj numer telefonu: ')
number = number.replace('-','')
formatted_number = ''
for index, letter in enumerate(number):
    if index % 3 ==0 and index != 0:
        formatted_number += '-'
    formatted_number += number[index]

print(formatted_number)