biedra = float(input("Jaka cena jablek jest w biedrze"))
lidl = float(input("Jaka cena jablek jest w lidlu"))
auchan = float(input("Jaka cena jablek jest w auchan"))

max_price = max(biedra,lidl,auchan)

print('Najwieksza cena jablek jest w:',max_price)