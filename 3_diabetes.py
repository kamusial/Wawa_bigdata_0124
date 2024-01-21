import pandas as pd
import numpy as np     # bibliteka do obliczeń numerycznych

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
