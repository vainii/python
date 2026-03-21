import pandas as pd

df = pd.read_csv('Clientes.csv', sep=';')

df.drop_duplicates(inplace=True)

df.to_csv('Clientes_limpos.csv', index=False, sep=';')

