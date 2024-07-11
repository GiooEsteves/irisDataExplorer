import pandas as pd

# Caminho para o arquivo CSV
filepath = 'data/raw/iris.csv'

# Carregar o conjunto de dados Iris
df = pd.read_csv(filepath)

# Exibir as primeiras linhas do dataset
print(df.head())
