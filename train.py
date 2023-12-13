import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(file_path):
    """
    Entraîne un modèle de classification sur les données prétraitées du Titanic.

    :param file_path: Chemin vers le fichier CSV contenant les données prétraitées.
    """
    # Charger les données traitées
    df_processed = pd.read_csv(file_path)
    df_processed = pd.get_dummies(df_processed, columns=['Embarked'], drop_first=True)

    # Diviser les données en ensembles d'entraînement et de test
    X = df_processed.drop('Survived', axis=1)
    y = df_processed['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Classificateur Random Forest
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)

    # Prédictions
    y_pred = rf_model.predict(X_test)

    # Évaluer l'exactitude
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Exactitude : {accuracy}")

if name == "main":
    train_model("Data/processed_train.csv")
