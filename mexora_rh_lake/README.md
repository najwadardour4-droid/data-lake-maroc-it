# 📊 Mexora RH Intelligence - Data Lake Project

## 📝 Présentation du Projet
Ce projet consiste à mettre en place une architecture **Data Lake** (Zones Bronze, Silver, Gold) pour analyser le marché de l'emploi IT au Maroc. L'objectif est d'aider le DRH de Mexora à prendre des décisions basées sur les données pour le recrutement.

## 🏗️ Architecture du Data Lake
Le projet suit une architecture Médaille :
* **Zone Bronze :** Ingestion des données brutes au format JSON (Données immuables).
* **Zone Silver :** Nettoyage, normalisation des salaires et extraction des compétences via NLP.
* **Zone Gold :** Tables analytiques prêtes pour le reporting (format Parquet).

## 🛠️ Technologies Utilisées
* **Python 3.x**
* **Pandas** (Manipulation des données)
* **DuckDB** (Requêtes SQL analytiques performantes)
* **PyArrow** (Support du format Parquet)

## 🚀 Comment lancer le projet ?

1.  **Installation des dépendances :**
    ```bash
    pip install pandas duckdb pyarrow
    ```

2.  **Exécution du Pipeline :**
    Lancer le script principal pour transformer les données de la zone Bronze vers Gold :
    ```bash
    python main.py
    ```

## 📈 Analyses Disponibles
Une fois le pipeline terminé, les analyses suivantes sont générées dans la zone `/gold` :
- Top compétences par profil.
- Médiane des salaires par ville.
- Répartition des contrats (CDI, Freelance).