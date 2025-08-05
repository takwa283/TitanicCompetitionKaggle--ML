### 1. **Acquisition et exploration des données (EDA)** 📊
* **Téléchargement** du fichier train.csv de Kaggle.
* **Exploration** de base avec les bibliothèques **Pandas**, **Matplotlib** et **Seaborn** pour comprendre la structure et les caractéristiques des données.
* **Visualisation** des relations entre les différentes variables, par exemple avec `sns.pairplot()`, pour identifier des schémas et des corrélations.

### 2. **Prétraitement des données** ⚙️
* **Gestion des valeurs manquantes** (`NaN`) : imputation des données manquantes dans les colonnes pertinentes.
* **Encodage des variables catégorielles** : transformation des variables non numériques comme le `Sex` et l'`Embarked` en format numérique pour que le modèle puisse les traiter.

### 3. **Modélisation** 🤖
* **Séparation du jeu de données** : division des données en ensembles d'entraînement et de test avec `train_test_split()`.
* **Entraînement d'un modèle** : utilisation d'un **XGBoostClassifier** pour prédire la survie. Le modèle est optimisé pour les performances en utilisant des objets `DMatrix`.

### 4. **Déploiement** 🚀
* **Exportation du modèle** : sauvegarde du modèle entraîné dans un format comme `xgb_model.json` ou `joblib` pour une utilisation future.
* **Création d'une API** avec **FastAPI** : développement d'un point de terminaison (`/predict`) qui charge le modèle sauvegardé, prend les données utilisateur en entrée, effectue une prédiction et renvoie le résultat. L'API est testée localement avec **Uvicorn**.
* **Développement de l'interface utilisateur** avec **Streamlit** : création d'une interface web conviviale avec un formulaire interactif (âge, sexe, classe, etc.). Cette interface **appelle l'API** pour envoyer les données saisies par l'utilisateur et affiche la prédiction de survie en retour.

