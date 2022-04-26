print('ile wydajesz na :')
food = float(input('jedzenie? '))
fun = float(input('rozrywke? '))
bills = float(input('rachunki? '))
other = float(input('reszte? '))

total = food + fun +bills +other

total_precent= {
    "jedzenie": food *100 / total,
    "rozrywka": fun * 100 /total,
    "rachunki" : bills * 100/total,
    "other" : other * 100 / total
}

choice = input('WPisz jedną z kategorii - (jedzenie/rozrywka/rachunki/inne) ')
print(f'Na {choice} procentowo do całości wydajesz {total_precent[choice]:.2f}%')