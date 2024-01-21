import matplotlib.pyplot as plt

# numbers = [5, 10, 15, 3, 20]
# plt.plot(numbers)
# plt.show()

# print('\nprosty wykres')
# zuzynie_pamieci = [5, 4, 7, 7, 6, 9, 9, 4, 5, 6, 5, 54, 65, 0, 1, 1, 2, 54, 3, 6, 7, 87, 6, 5]
# plt.plot(zuzynie_pamieci, 'mp--')
# plt.show()

# print('\nwykres z wygenerowanymi danymi')
# yki = [4, 6, 8, 6, 11, 12, 11, 3, 0, 0, 6, 4]
# Xy =  [2, 4, 8, 7, 6, 4, 4, 1, 0, 12, 2, 4]
# plt.plot(Xy, yki, 'mp')
# plt.show()

print('\nwykresY z wygenerowanymi danymi')
y1 = [2, 3, 4, 5, 6, 6, 6, 7, 4, 3, 3, 2, 3, 4]
y2 = [6, 6, 6, 6, 6, 5, -2, 3, 2, 2, 2, 2, 3, 4]
y3 = [0, -4, 0, 0, 0, 0, 10, 10, 10, 9, 8, 7, 7, 7]
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.axhline()   # oś
plt.axvline()   # oś
plt.xlabel('Opis osi X')
plt.ylabel('Opis osi Y')
plt.title('Tytul wykresu')
plt.show()