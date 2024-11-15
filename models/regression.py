from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(data):
    # Variables explicatives et cible
    X = data[["Prix", "Publicité", "PIB", "Saisonnalité"]]
    y = data["Ventes"]

    # Diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle de régression
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    return model, X_test, y_test, y_pred
