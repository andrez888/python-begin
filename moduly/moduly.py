import srednia_predkosc as sp

s = int(input('Podaj Przebyta drogę w km:\t'))
t = float(input('podaj czas w h:\t'))

answer = sp.average_speed(s,t)
print(f'Twoja srednia predkosc to {answer:.2f} km')

