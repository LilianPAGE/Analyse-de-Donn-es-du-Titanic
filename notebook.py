# %% [markdown]
# <a href="https://colab.research.google.com/github/LilianPAGE/Analyse-de-Donn-es-du-Titanic/blob/main/notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("data/train.csv")
df

# %%
# exploration initiale
print(df.info())

print(df.describe())

print(df.isnull().sum())


# %%
#visualisations pertinentes
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Nombre de survivants par classe')
plt.show()


# %%
# Remplir les valeurs manquantes de la colonne age par la median
df['Age'].fillna(df['Age'].median(), inplace=True)
df


# %%
#Créer une nouvelle caractéristique 'Family_Size'
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
df


# %%

# Convertir le type de la colonne 'Sex' en int64 et convertir male et female en 0 et 1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Sex'] = df['Sex'].astype('int64')

df


# %%
#Supprimer les colonnes 'Name', 'Ticket', 'Cabin'
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
df

# %%
# Sauvegarder les données traitées dans un nouveau fichier CSV
df.to_csv("processed_train.csv", index=False)


# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Charger les données traitées
df_processed = pd.read_csv("processed_train.csv")
df_processed

# %%
df_processed = pd.get_dummies(df_processed, columns=['Embarked'], drop_first=True)

#  Diviser les données en ensembles d'entrainement et de test
X = df_processed.drop('Survived', axis=1)
y = df_processed['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# %%
#Classificateur Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Prédictions
y_pred = rf_model.predict(X_test)

# Evaluer l'exactitude
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitude : {accuracy}")


# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# %%
# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


dt_classifier = DecisionTreeClassifier()
dt_scores = cross_val_score(dt_classifier, X, y, cv=5)
print("\nDecision Tree Classifier Cross-validated scores:")
print("Cross-validated scores:", dt_scores)
print("Average score:", dt_scores.mean())

# %%
# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

rf_classifier = RandomForestClassifier()
rf_scores = cross_val_score(rf_classifier, X, y, cv=5)
print("\nRandom Forest Classifier Cross-validated scores:")
print("Cross-validated scores:", rf_scores)
print("Average score:", rf_scores.mean())

# %%
# Evaluation with confusion_matrix and classification_report
from sklearn.metrics import confusion_matrix, classification_report

# Logistic Regression
print("\nLogistic Regression Evaluation:")
y_pred_log_reg = log_reg.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log_reg))
print("Classification Report:\n", classification_report(y_test, y_pred_log_reg))


# %%
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                        display_labels=log_reg.classes_)
disp.plot()

# %%
# Decision Tree Classifier
y_pred_dt = dt_classifier.fit(X_train, y_train).predict(X_test)
print("\nDecision Tree Classifier Evaluation:")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))
print("Classification Report:\n", classification_report(y_test, y_pred_dt))

# %%

cm = confusion_matrix(y_test, y_pred_dt)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dt_classifier.classes_)

disp.plot()

# %%
# Random Forest Classifier
y_pred_rf = rf_classifier.fit(X_train, y_train).predict(X_test)
print("\nRandom Forest Classifier Evaluation:")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
print("Classification Report:\n", classification_report(y_test, y_pred_rf))

# %%
cm = confusion_matrix(y_test, y_pred_rf)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dt_classifier.classes_)

disp.plot()

# %%
# Discussion of results
print("\nDiscussion of Results:")
print("The model that performs the best based on cross-validation scores is:", end=" ")
if log_reg_scores.mean() > dt_scores.mean() and log_reg_scores.mean() > rf_scores.mean():
    print("Logistic Regression")
elif dt_scores.mean() > log_reg_scores.mean() and dt_scores.mean() > rf_scores.mean():
    print("Decision Tree Classifier")
else:
    print("Random Forest Classifier")

# %%


# %%


# %%


# %%


# %%



