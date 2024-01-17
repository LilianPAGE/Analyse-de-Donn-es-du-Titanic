import pandas as pd
from Src import process


def test_process_data():

    # Emplacement du fichier
    path = "../Data/train.csv"

    # Appeler la fonction de traitement
    process.process_data(path)

    # Charger les données traitées
    df_processed = pd.read_csv("../Data/processed_train.csv")

    # Vérifier si les transformations ont été appliquées correctement
    assert df_processed['Age'].notnull().all()
    assert df_processed['Age'].dtype == 'float64'
    assert 'Name' not in df_processed.columns
    assert 'Ticket' not in df_processed.columns
    assert 'Cabin' not in df_processed.columns

    # Supprimer les fichiers temporaires
    import os
    os.remove("../Data/processed_train.csv")
