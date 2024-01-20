import pandas

df = pandas.read_csv('otodom.csv')
print(df.head().to_string())