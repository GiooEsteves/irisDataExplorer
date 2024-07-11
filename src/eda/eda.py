import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_eda(df):
    """
    Realiza análise exploratória de dados no DataFrame fornecido.

    Parâmetros:
    df (DataFrame): DataFrame contendo os dados.

    Retorna:
    None
    """
    # Criar a pasta figures se não existir
    figures_dir = os.path.join(os.path.dirname(__file__), '../../reports/figures')
    os.makedirs(figures_dir, exist_ok=True)

    # 1. Estatísticas Descritivas
    print("Estatísticas Descritivas:")
    print(df.describe())

    # 2. Visualizações
    # Distribuição das variáveis numéricas
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 2, 1)
    sns.histplot(df['SepalLengthCm'], kde=True, bins=20, color='skyblue')
    plt.title('Distribuição do Comprimento da Sépala')
    plt.savefig(os.path.join(figures_dir, 'distribuicao_comprimento_sepala.png'))

    plt.subplot(2, 2, 2)
    sns.histplot(df['SepalWidthCm'], kde=True, bins=20, color='salmon')
    plt.title('Distribuição da Largura da Sépala')
    plt.savefig(os.path.join(figures_dir, 'distribuicao_largura_sepala.png'))

    plt.subplot(2, 2, 3)
    sns.histplot(df['PetalLengthCm'], kde=True, bins=20, color='green')
    plt.title('Distribuição do Comprimento da Pétala')
    plt.savefig(os.path.join(figures_dir, 'distribuicao_comprimento_petala.png'))

    plt.subplot(2, 2, 4)
    sns.histplot(df['PetalWidthCm'], kde=True, bins=20, color='gold')
    plt.title('Distribuição da Largura da Pétala')
    plt.savefig(os.path.join(figures_dir, 'distribuicao_largura_petala.png'))

    plt.tight_layout()
    plt.show()

    # Relação entre variáveis
    sns.pairplot(df, hue='Species', height=3, aspect=1.2)
    plt.suptitle('Relação entre Variáveis por Espécie', y=1.02)
    pairplot_path = os.path.join(figures_dir, 'relacao_variaveis_por_especie.png')
    plt.savefig(pairplot_path)
    plt.show()

    # Boxplot das medidas por espécie
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 2, 1)
    sns.boxplot(x='Species', y='SepalLengthCm', data=df)
    plt.title('Comprimento da Sépala por Espécie')
    plt.savefig(os.path.join(figures_dir, 'boxplot_comprimento_sepala.png'))

    plt.subplot(2, 2, 2)
    sns.boxplot(x='Species', y='SepalWidthCm', data=df)
    plt.title('Largura da Sépala por Espécie')
    plt.savefig(os.path.join(figures_dir, 'boxplot_largura_sepala.png'))

    plt.subplot(2, 2, 3)
    sns.boxplot(x='Species', y='PetalLengthCm', data=df)
    plt.title('Comprimento da Pétala por Espécie')
    plt.savefig(os.path.join(figures_dir, 'boxplot_comprimento_petala.png'))

    plt.subplot(2, 2, 4)
    sns.boxplot(x='Species', y='PetalWidthCm', data=df)
    plt.title('Largura da Pétala por Espécie')
    plt.savefig(os.path.join(figures_dir, 'boxplot_largura_petala.png'))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Obter o caminho para o arquivo CSV
    current_dir = os.path.dirname(__file__)
    input_filepath = os.path.join(current_dir, '../../data/processed/iris_processed.csv')

    # Carregar os dados
    df = pd.read_csv(input_filepath)

    # Realizar análise exploratória de dados
    perform_eda(df)
