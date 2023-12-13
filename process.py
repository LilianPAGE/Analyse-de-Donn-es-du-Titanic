import pandas as pd

def process_data(file_path):
    """
    Prétraitement des données du Titanic.

    :param file_path: Chemin vers le fichier CSV contenant les données brutes.
    """
    # Charger le jeu de données
    df = pd.read_csv(file_path)

    # Exploration initiale
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())

    # Remplir les valeurs manquantes de l'âge par la médiane
    df['Age'].fillna(df['Age'].median(), inplace=True)

    # Créer une nouvelle caractéristique 'Family_Size'
    df['Family_Size'] = df['SibSp'] + df['Parch'] + 1

    # Convertir le type de la colonne 'Sex' en int64
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Sex'] = df['Sex'].astype('int64')

    # Supprimer les colonnes 'Name', 'Ticket', 'Cabin'
    df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    # Sauvegarder les données traitées dans un nouveau fichier CSV
    df.to_csv("Data/processed_train.csv", index=False)
