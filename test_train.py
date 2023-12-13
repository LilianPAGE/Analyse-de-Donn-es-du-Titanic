import pandas as pd
import train

def test_train_model():
    # Créer un DataFrame de test
    data = {
        'Age': [25, 30, 35],
        'SibSp': [1, 0, 2],
        'Parch': [0, 1, 1],
        'Sex': [0, 1, 0],
        'Embarked': ['S', 'C', 'Q'],
        'Survived': [1, 0, 1]
    }
    df_test = pd.DataFrame(data)

    # Sauvegarder le DataFrame de test dans un fichier CSV
    df_test.to_csv("test_data.csv", index=False)

    # Appeler la fonction d'entraînement
    train.train_model("test_data.csv")

    # Supprimer les fichiers temporaires
    import os
    os.remove("test_data.csv")

if name == "main":
    test_train_model()
