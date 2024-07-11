import matplotlib.pyplot as plt
import os

def load_and_display_figures():
    """
    Carrega e exibe todas as figuras PNG na pasta figures.

    Retorna:
    None
    """
    figures_dir = os.path.join(os.path.dirname(__file__), '../../reports/figures')

    # Verificar se a pasta figures existe
    if not os.path.exists(figures_dir):
        print(f"A pasta {figures_dir} não existe.")
        return

    # Listar todos os arquivos PNG na pasta figures
    figures = [f for f in os.listdir(figures_dir) if f.endswith('.png')]

    if not figures:
        print(f"Nenhuma figura PNG encontrada na pasta {figures_dir}.")
        return

    for fig in figures:
        fig_path = os.path.join(figures_dir, fig)
        img = plt.imread(fig_path)
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')
        plt.title(fig.replace('_', ' ').replace('.png', '').title())
        plt.show()

if __name__ == "__main__":
    load_and_display_figures()
