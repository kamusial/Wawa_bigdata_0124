import pandas as pd
import numpy as np     # bibliteka do obliczeń numerycznych
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes.csv')
print(df.head(5).to_string())

print(df.describe().T.to_string())

print(df.isna().sum())    #ile pól bez wartości
print(df.outcome.value_counts())    #policz, ile jakich wartości w kolumnie "outcome"

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NAN, inplace=True)   # zamień zera na "nic"
    mean_ = df[col].mean()    #policz średnią z kolumny
    df[col].replace(np.NAN, mean_, inplace=True)   # wpisz średnią tam, gdzie brak wartości
print(df.isna().sum())    #sprawdź

df.to_csv('cukrzyca.csv', sep=';', index=False)

print('regresja logistyczna')
X = df.iloc[ : , :-1 ]    # dane wejściowe, bez ceny i bez id
y = df.outcome              # dane wyjściowe

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)   # dane testowe 20%

model = LogisticRegression()
model.fit(X_train, y_train)    #naucz się na danych treningowych
print(model.score(X_test, y_test))   #sprawdź
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nZmiana danych')
df1 = df.query('outcome==0').sample(n=500)    # wybierz 500 zdrowych
df2 = df.query('outcome==1').sample(n=500)    # wybierz 500 chorych
df3 = pd.concat([df1, df2])     # łączenie tabel
print(df3)

X = df3.iloc[ : , :-1 ]    # dane wejściowe, bez ceny i bez id
y = df3.outcome              # dane wyjściowe

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)   # dane testowe 20%

model = LogisticRegression()
model.fit(X_train, y_train)    #naucz się na danych treningowych
print(model.score(X_test, y_test))   #sprawdź
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))