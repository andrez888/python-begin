dishes = input('Podaj swoje ulubione dania rozdzielone przecinkiem :')

list_dishes = dishes.split(',')
favourite = 1
while favourite < len(list_dishes)+1:
    print(f'Twoim ulubionym daniem nr {favourite} jest {list_dishes[favourite-1]}')
    favourite += 1
