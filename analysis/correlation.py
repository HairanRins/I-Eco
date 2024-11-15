import seaborn as sns
import matplotlib.pyplot as plt

def analyze_correlation(data):
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.show()
