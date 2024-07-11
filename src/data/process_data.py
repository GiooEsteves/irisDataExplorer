import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Realiza o pré-processamento dos dados.

    Parâmetros:
    df (DataFrame): DataFrame com os dados.

    Retorna:
    DataFrame: DataFrame pré-processado.
    """
    # Selecionar apenas as colunas numéricas para normalização
    numeric_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    df_numeric = df[numeric_columns]

    # Verificar e tratar dados ausentes, se houver
    if df_numeric.isnull().any().any():
        df_numeric = df_numeric.dropna()  # Exemplo simples: remover linhas com dados ausentes

    # Normalizar os dados, se necessário (exemplo com StandardScaler)
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df_numeric)

    return df

# Exemplo de uso
if __name__ == "__main__":
    # Caminho para o arquivo CSV
    filepath = 'data/raw/iris.csv'

    # Carregar os dados
    df = pd.read_csv(filepath)

    # Exibir as colunas carregadas
    #print("Colunas carregadas do arquivo CSV:")
    #print(df.columns)

    # Pré-processar os dados
    df_processed = preprocess_data(df)

    # Exibir as primeiras linhas do dataset pré-processado
    print("Primeiras linhas do dataset pré-processado:")
    print(df_processed.head())

    # Salvar DataFrame pré-processado em um arquivo CSV
    output_filepath = 'data/processed/iris_processed.csv'
    df_processed.to_csv(output_filepath, index=False)
