import matplotlib.pyplot as plt

wydatki = ['mieszkanie', 'media', 'jedzenie', 'nauka', 'inwestycje']
wartosci = [3000, 1000, 1500, 2000, 400]
wyciecia = [0, 0, 0.2, 0, 0.3]
kolory = ['black', 'red', "#A00F50", "#A4AFF0","#12AF10"]
plt.pie(wartosci, labels=wydatki, startangle=90, explode=wyciecia, shadow=True, colors=kolory)
plt.legend(title='Wydatki')
plt.show()
