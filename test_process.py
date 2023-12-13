import pandas as pd
import process

def test_process_data():
    # Créer un DataFrame de test
    data = {
        'Age': [25, None, 30],
        'SibSp': [1, 0, 2],
        'Parch': [0, 1, 1],
        'Sex': ['male', 'female', 'male'],
        'Embarked': ['S', 'C', 'Q'],
        'Survived': [1, 0, 1]
    }
    df_test = pd.DataFrame(data)

    # Sauvegarder le DataFrame de test dans un fichier CSV
    df_test.to_csv("test_data.csv", index=False)

    # Appeler la fonction de traitement
    process.process_data("test_data.csv")

    # Charger les données traitées
    df_processed = pd.read_csv("processed_test_data.csv")

    # Vérifier si les transformations ont été appliquées correctement
    assert 'Age' not in df_processed.columns
    assert 'Family_Size' in df_processed.columns
    assert 'Sex' in df_processed.columns
    assert 'Embarked' not in df_processed.columns

    # Supprimer les fichiers temporaires
    import os
    os.remove("test_data.csv")
    os.remove("processed_test_data.csv")
