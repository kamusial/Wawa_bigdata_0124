import pandas as pd                 # czytania i analizy danych
import matplotlib.pyplot as plt     # wykresy
import seaborn as sns               # fajne wykresy

print('program start, czytam plik')
df = pd.read_csv('otodom.csv')
print()
print('..............')
print('wyswietlam plik')
print(df.head().to_string())
print()
print('..............')
print('wyswietlam szczegoly danych - describe')
print(df.describe().T.to_string())
# describe - przygotuj zestawienie danych
# T - zamień wiersze z kolumnami
# przygotuj jako string - nie obcinaj kolumn

print()
print('..............')
print('Wykres')
# wykres, podstawowy histogram
# sns.histplot(data=df, x="cena")
# plt.show()

print()
print('..............')
print('cwiczenia')
print(df.iloc[ 3, 1 ])   # wiersz, kolumna - od 0
print(df.iloc[ 2:4 , 3:6 ])  # wiersze od 3 do 4 i kolumny od 4 do 6
print(df.iloc[ :2, 4: ])   # od początku, albo do końca
print(df.iloc[ :5, :-1 ])   # 5 pierwszy wierszy, komny bez ostatniej

print()
print('..............')
print('wybieram dane')

q1 = df.describe().T.loc['cena', '25%']
q3 = df.describe().T.loc['cena', '75%']
# print(q1, q3)

df1 = df[(df.cena >= q1) & (df.cena <= q3)]   # wycięcie najtańśzych i najdrozszych mieszkań
print(df1.describe())

print()
print('..............')
print('Wykres')
# wykres, podstawowy histogram
sns.histplot(data=df1, x="cena")
plt.show()

print()
print('..............')
print('Korelacja')

sns.heatmap (df.iloc[ : , 1: ].corr(), annot=True)
plt.show()