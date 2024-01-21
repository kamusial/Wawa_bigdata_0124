import matplotlib.pyplot as plt
imiona = ['Agata', 'Tomasz', 'Magda', 'Alina', 'Mateusz']
punkty = [34, 54, 9, 12, 39]

plt.bar(imiona, punkty, color=['red', 'green', 'blue'])   #kolory będą powtarzane
plt.xticks(imiona)
plt.yticks(punkty)
plt.show()