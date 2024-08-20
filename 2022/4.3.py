from itertools import combinations

# Wczytanie liczb z pliku
with open('./data/przyklad.txt', 'r') as file:
    liczby = [int(line.strip()) for line in file]

# Znalezienie dobrych trójek
dobre_trojki = []
for x, y, z in combinations(liczby, 3):
    if y % x == 0 and z % y == 0 and x != y != z:
        dobre_trojki.append((x, y, z))

# Zapisanie dobrych trójek do pliku
with open('trojki.txt', 'w') as file:
    for trojka in dobre_trojki:
        file.write(f"{trojka[0]} {trojka[1]} {trojka[2]}\n")

# Znalezienie dobrych piątek
dobre_piatki = []
for u, w, x, y, z in combinations(liczby, 5):
    if w % u == 0 and x % w == 0 and y % x == 0 and z % y == 0 and u != w != x != y != z:
        dobre_piatki.append((u, w, x, y, z))

# Wyświetlenie wyników
print("Liczba dobrych trójek:", len(dobre_trojki))
print("Liczba dobrych piątek:", len(dobre_piatki))
