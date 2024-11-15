import pandas as pd 

def preprocess_data(data):
    # Convertir les dates en format datetime
    data["Date"] = pd.to_datetime(data["Date"])
    
    # Vérifier les valeurs manquantes
    if data.isnull().sum().sum() > 0:
        data.fillna(data.mean(), inplace=True)
    
    return data
