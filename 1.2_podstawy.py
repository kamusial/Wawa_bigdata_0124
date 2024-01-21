# pętla for

for i in range(0, 5, 1):    # od, do, krok
    print('Moj iterator to:', i)
print('Lecimy dalej\n')

for i in range(5, 50, 4):    # od, do, krok
    print('Moj iterator to', i)
print('Lecimy dalej\n')

for i in range(50, 10, -3):    # od, do, krok
    print('Moj iterator to', i)
print('Lecimy dalej\n')

lista_imion = ['Kamil', 'Agata', 'Anna', 'Maciej', 'Weronika', 'Oliwia', 'Tomasz']
print(lista_imion)
print(lista_imion[2])   # 3ci element, Anna
print(lista_imion[1:4])  # 2gie, 3cie, 4te imie

imie = 'Mateusz'
print(imie[2])    # litera t
print(imie[2:5])   # kilka liter

for i in range(5):     # domyslnie od 0, do 5, z krokiem 1
    print(lista_imion[i])

for imie in lista_imion:
    print(imie)