mat = int(input('Jaka masz ocene z matematyki'))
his = int(input('Jaka masz ocene z historii'))
fiz = int(input('Jaka masz ocene z fizyki'))
chem = int(input('Jaka masz ocene z chemii'))
wf = int(input('Jaka masz ocene z wf'))

number_failed = 0


if mat < 2:
    number_failed+=1
if his < 2:
    number_failed+=1
if fiz < 2:
    number_failed+=1
if chem < 2:
    number_failed+=1
if wf < 2:
    number_failed+=1

if number_failed == 0:
    print('zdales')
else:
    if number_failed == 1:
        srednia= (mat + his + fiz + chem + wf)/5
        if srednia > 3.5:
            print(f'udalo ci sie {srednia}')
        else:
            print('niestety')
    else:
        print('niestey kaplica')