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
most_important = "jedzenie"
if total_precent['rozrywka'] > total_precent[most_important]:
    most_important= 'rozrywka'
if total_precent['rachunki'] > total_precent[most_important]:
    most_important = 'rachunki'
if total_precent['other'] > total_precent[most_important]:
    most_important = 'other'
print(f'Najwiecej wydajesz na {most_important}')