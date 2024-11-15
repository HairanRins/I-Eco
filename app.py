import pandas as pd
from utils.preprocessing import preprocess_data
from models.regression import train_model
from models.evaluation import evaluate_model
from analysis.correlation import analyze_correlation
from analysis.visualisation import plot_results

# Charger ou générer les données
try:
    data = pd.read_csv("data/economic_data.csv")
    print("Dataset chargé avec succès.")
except FileNotFoundError:
    print("Dataset introuvable, génération des données...")

# Prétraitement des données
data = preprocess_data(data)

# Analyse de corrélation
analyze_correlation(data)

# Entraînement du modèle
model, X_test, y_test, y_pred = train_model(data)

# Évaluation du modèle
evaluate_model(y_test, y_pred)

# Visualisation des résultats
plot_results(y_test, y_pred)

