# Relatório de Análise Exploratória de Dados (EDA)

## Introdução
Este documento descreve as etapas realizadas durante a Análise Exploratória de Dados (EDA) do conjunto de dados Iris. A EDA é uma etapa fundamental no processo de análise de dados, pois permite entender melhor a estrutura dos dados, identificar padrões e detectar anomalias.

## Importação dos Dados
Os dados foram importados do arquivo `iris.csv` localizado na pasta `data/raw`.

### Código para Importação dos Dados
```python
import pandas as pd

# Caminho para o arquivo CSV
filepath = 'data/raw/iris.csv'

# Carregar o conjunto de dados Iris
df = pd.read_csv(filepath)

# Exibir as primeiras linhas do dataset
print(df.head())
