Étapes techniques d’un projet Titanic ML 

1. Acquisition & Exploration des données 

*Chargement du dataset train.csv depuis Kaggle.

*Analyse exploratoire des données (EDA) avec pandas, matplotlib, seaborn.

*Visualisations : sns.pairplot().


2. Prétraitement des données (Data preprocessing)

*Traitement des valeurs manquantes (NaN).

*Encodage des variables catégorielles (Sex, Embarked).

3. Modélisation (Model building)

*Séparation des données : train_test_split().

*Entraînement d’un modèle XGBoostClassifier ; Le modèle est entraîné à l’aide d’XGBoost en utilisant des objets DMatrix optimisés pour les performances.


4. Exportation du modèle

*Sauvegarde du modèle au format xgb_model.json ou joblib : model.save_model().

6. Création d’une API avec FastAPI

*Création d’un endpoint /predict qui charge le modèle et retourne la prédiction.

*Développement de api.py avec FastAPI.

*Test de l’API localement avec Uvicorn.

8. Interface utilisateur avec Streamlit

*Création d’un formulaire interactif (ex : saisie de l'âge, sexe, classe, etc.).

*Appel de l’API pour envoyer les données et afficher la prédiction.
*Design UI : ajout d’un fond, amélioration de l’ergonomie.

