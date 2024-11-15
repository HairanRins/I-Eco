import matplotlib.pyplot as plt

def plot_results(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label="Ventes réelles", marker='o')
    plt.plot(y_pred, label="Ventes prédites", linestyle="--")
    plt.title("Comparaison des ventes réelles et prédites")
    plt.xlabel("Index")
    plt.ylabel("Ventes")
    plt.legend()
    plt.show()
