Prédiction du Prix des Maisons - Régression Linéaire

Ce projet utilise la régression linéaire pour prédire le prix des maisons en fonction de leur surface. Il est implémenté en Python avec des bibliothèques populaires comme pandas, matplotlib et scikit-learn.
Fonctionnalités

    Affichage des données : Visualisation de la relation entre la surface des maisons et leur prix sous forme de graphique.
    Préparation des données : Division du jeu de données en deux ensembles : un pour l'entraînement (train) et un pour le test.
    Entraînement du modèle : Utilisation de la régression linéaire pour entraîner un modèle à prédire les prix en fonction de la surface.
    Évaluation du modèle : Calcul du RMSE (Root Mean Square Error) pour mesurer la performance du modèle, et visualisation des prédictions par rapport aux valeurs réelles.

Installation
Prérequis

Avant de commencer, assurez-vous d'avoir Python 3 installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

    pandas : Pour manipuler les données.
    matplotlib : Pour afficher des graphiques.
    scikit-learn : Pour la régression linéaire et l'évaluation du modèle.
    math : Pour le calcul du RMSE.

Installez les dépendances nécessaires avec pip :

pip install pandas matplotlib scikit-learn

Utilisation
1. Télécharger les données

Ce projet utilise un fichier CSV intitulé prix_maisons.csv. Assurez-vous que le fichier est dans le même répertoire que votre script ou modifiez le chemin dans le code.
2. Préparer et exécuter le script

Voici les étapes à suivre pour exécuter le script :

    Initialisez et chargez les données : Le fichier CSV contient les informations de surface des maisons et de leur prix. Vous pouvez voir les premières lignes des données en affichant la dataframe data_df.

    Préparation des données : Le jeu de données est divisé en deux groupes : un pour l'entraînement et un pour le test (75% pour l'entraînement et 25% pour le test).

    Entraînement du modèle : Un modèle de régression linéaire est créé et entraîné sur les données d'entraînement.

    Test du modèle : Le modèle est testé sur les données de test. Le RMSE est calculé pour évaluer la précision des prédictions du modèle.

    Affichage des résultats : Le graphique montre les points réels (en bleu) et les prédictions du modèle (en rouge) pour les données de test.

3. Exécution du script

python script_name.py

Cela exécutera l'ensemble du pipeline : préparation des données, entraînement du modèle, évaluation et affichage des résultats.
Fonctionnalités supplémentaires

    Visualisation des données : Vous pouvez visualiser les données réelles en utilisant la fonction show_data(df). Il suffit de décommenter la ligne correspondante dans le script.

    Calcul du RMSE : Le RMSE permet d’évaluer l'écart moyen entre les valeurs prédites et réelles. Un RMSE plus faible indique une meilleure précision du modèle.

Structure du projet

/linear_regression_project
  ├── prix_maisons.csv           # Fichier de données
  ├── script_name.py             # Code Python principal
  ├── README.md                 # Ce fichier

Auteurs

    elhadji4+
