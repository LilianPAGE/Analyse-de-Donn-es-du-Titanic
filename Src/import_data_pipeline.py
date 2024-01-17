import pandas as pd
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine

# Définir une classe pour l'importation des données
class DataImportPipeline:

    def __init__(self, db_url, table_name):
        self.db_url = db_url
        self.table_name = table_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Charger les données à partir d'un fichier CSV
        titanic_data = pd.read_csv(X)

        # Connexion à la base de données MySQL
        engine = create_engine(self.db_url)

        # Charger les données dans la table spécifiée
        titanic_data.to_sql(self.table_name, con=engine, if_exists='replace', index=False)

        return titanic_data

# Définir le pipeline d'importation des données
db_url = 'mysql+mysqlconnector://root:cqfd14sAfe@localhost/sinkingship'
table_name = 'personne'
import_pipeline = Pipeline([
    ('import_data', DataImportPipeline(db_url, table_name))
])

# Utiliser le pipeline pour charger les données
file_path = 'C:/Users/Proprietaire/Desktop/COURS/ESTIAM/test.csv'
imported_data = import_pipeline.transform(file_path)

# Afficher les premières lignes des données importées
print(imported_data.head())
