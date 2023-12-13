import pandas as pd
import process

def test_process_data():

    #Emplacement du fichier
    path = "Data/train.csv"

    # Appeler la fonction de traitement
    process.process_data(path)

    # Charger les données traitées
    df_processed = pd.read_csv("processed_test_data.csv")

    # Vérifier si les transformations ont été appliquées correctement
    assert 'Age' not in df_processed.columns
    assert 'Family_Size' in df_processed.columns
    assert 'Sex' in df_processed.columns
    assert 'Embarked' not in df_processed.columns

    # Supprimer les fichiers temporaires
    import os
    os.remove("processed_test_data.csv")
