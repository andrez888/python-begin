numer = input('Ziomuś podaj jakieś liczby po przecinku a wyskocza nieparzyste:\t')
liczby = numer.split(',')
number= []
b= None
for x in liczby:
    b = int(x)
    number.append(b)
print('Twoje liczby nieparzyste')
for i in number:

    if i % 2 == 0 and i != 0:
        continue
    print(i)