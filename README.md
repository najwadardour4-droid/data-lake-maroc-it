# 📊 Mexora RH Intelligence – Data Lake Project

## 📝 Présentation du Projet

Ce projet consiste à concevoir et implémenter une architecture Data Lake basée sur les zones Bronze, Silver et Gold afin d'analyser le marché de l'emploi IT au Maroc.

L'objectif est d'aider le département RH de Mexora à prendre des décisions stratégiques concernant le recrutement grâce à des indicateurs fiables et des analyses basées sur les données.

---

## 🎯 Objectifs du Projet

- Collecter les offres d'emploi depuis différentes sources.
- Centraliser les données dans un Data Lake.
- Nettoyer et transformer les données.
- Standardiser les informations salariales.
- Extraire les compétences recherchées.
- Produire des indicateurs RH exploitables.
- Préparer les données pour la visualisation et le reporting.

---

## 🏗️ Architecture du Data Lake

### 🥉 Zone Bronze

Contient les données brutes collectées depuis les plateformes d'emploi.

Sources :

- LinkedIn Jobs
- Rekrute

Les données sont stockées sans modification afin de conserver la version originale.

### 🥈 Zone Silver

Contient les données nettoyées et transformées :

- Suppression des doublons
- Gestion des valeurs manquantes
- Uniformisation des formats
- Normalisation des salaires
- Nettoyage des colonnes textuelles

### 🥇 Zone Gold

Contient les tables analytiques finales utilisées pour répondre aux besoins métier :

- Top compétences recherchées
- Salaires par ville
- Répartition des contrats
- Répartition des offres d'emploi
- Statistiques RH

---

## 📂 Structure du Projet

```text
Mexora-RH-Intelligence/
│
├── bronze/
│   ├── linkedin/
│   └── rekrute/
│
├── silver/
│   └── cleaned_data/
│
├── gold/
│   └── kpis/
│
├── analysis/
│   ├── q1.png
│   ├── q2.png
│   ├── q3.png
│   ├── q4.png
│   ├── q5.png
│   └── analysis.ipynb
│
├── pipeline/
│   ├── bronze_to_silver.py
│   ├── silver_to_gold.py
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Utilisées

- Python 3
- Pandas
- DuckDB
- PyArrow
- Jupyter Notebook
- Git & GitHub

---

## ⚙️ Installation

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Ou manuellement :

```bash
pip install pandas duckdb pyarrow
```

---

## ▶️ Exécution du Pipeline

Lancer le pipeline complet :

```bash
python pipeline/main.py
```

Le pipeline effectue automatiquement :

1. Lecture des données brutes (Bronze)
2. Nettoyage et transformation (Silver)
3. Création des indicateurs analytiques (Gold)

---

## 📈 Analyses Réalisées

### Q1 – Top compétences recherchées

Identification des compétences les plus demandées dans les offres IT.

### Q2 – Médiane des salaires par ville

Analyse comparative des rémunérations selon les villes marocaines.

### Q3 – Répartition des contrats

Distribution des types de contrats :

- CDI
- CDD
- Freelance
- Stage

### Q4 – Répartition géographique des offres

Analyse du nombre d'offres par ville.

### Q5 – Analyse globale du marché IT

Vue synthétique des tendances du recrutement.

Les résultats sont disponibles dans le dossier **analysis/**.

---

## 📊 Résultats

Les données finales produites dans la zone Gold permettent :

- D'identifier les compétences les plus recherchées.
- D'analyser les tendances salariales.
- D'étudier la répartition des contrats.
- D'aider les responsables RH à prendre des décisions basées sur les données.

---

## 👩‍💻 Réalisé par

**Najwa Dardour**

Étudiante en :AD

---

## 🔗 Repository GitHub

Lien du projet :

https://github.com/najwadardour4-droid/data-lake-maroc-it.git
