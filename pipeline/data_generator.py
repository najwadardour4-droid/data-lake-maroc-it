import json
import random
from faker import Faker

fake = Faker(['fr_FR'])

def generate_job_data(n=5000):

    # Villes avec problèmes intentionnels
    villes = [
        "Casablanca", "casa", "CASABLANCA", "Casablanca ",
        "Rabat", "rabat", "RABAT",
        "Tanger", "tanger", "TANGER", "Tanja",
        "Marrakech", "marrakech", "MARRAKECH",
        "Agadir", "agadir",
        "Fès", "fes", "FES",
        "Meknès", "meknes",
        "Oujda"
    ]

    # Titres avec problèmes intentionnels
    titres_data = [
        "Data Engineer", "Data Eng.", "Dev Data", "Ingénieur Data",
        "Data Engineer Junior", "Senior Data Engineer", "Ingénieur Big Data"
    ]
    titres_analyst = [
        "Data Analyst", "BI Analyst", "Analyste Data", "Analyste BI",
        "Business Intelligence Analyst", "Reporting Analyst", "Développeur BI"
    ]
    titres_science = [
        "Data Scientist", "Machine Learning Engineer", "ML Engineer",
        "IA Engineer", "Deep Learning Engineer"
    ]
    titres_dev = [
        "Développeur Full Stack", "Dev Fullstack", "Full Stack Developer",
        "Développeur Backend", "Backend Developer",
        "Développeur Frontend", "Frontend Developer",
        "Développeur Mobile", "iOS Dev", "Android Dev"
    ]
    titres_infra = [
        "DevOps Engineer", "DevOps", "Cloud Engineer",
        "SysAdmin", "Administrateur Systèmes", "Network Engineer"
    ]
    titres_autre = [
        "Chef de Projet IT", "Project Manager", "Scrum Master",
        "Architecte Solution", "Cybersécurité Analyst", "Pentester"
    ]

    tous_titres = (
        titres_data * 4 +      # surreprésenter les profils data
        titres_analyst * 3 +
        titres_science * 2 +
        titres_dev * 3 +
        titres_infra * 2 +
        titres_autre
    )

    # Contrats avec problèmes intentionnels
    contrats = [
        "CDI", "cdi", "Contrat à durée indéterminée", "Permanent",
        "CDD", "cdd", "Contrat à durée déterminée",
        "Freelance", "freelance", "Consultant",
        "Stage", "PFE", "Alternance"
    ]

    # Compétences par profil
    competences_data_eng = [
        "Python, Spark, Airflow, Kafka, Docker, AWS, SQL",
        "Python, dbt, Airflow, PostgreSQL, GCP, Git",
        "Spark, Hadoop, Kafka, Scala, HDFS, AWS S3",
        "Python, Azure, Synapse, dbt, SQL, Git, Docker",
        "PySpark, Airflow, Kafka, Docker, Kubernetes, GCP"
    ]
    competences_analyst = [
        "SQL, Power BI, Excel, Python, Tableau",
        "SQL, Metabase, Python, Excel, Power BI",
        "Tableau, SQL, Excel, Python, Looker",
        "Power BI, SQL, DAX, Excel, Python",
        "SQL, Excel, Metabase, Power BI, Looker Studio"
    ]
    competences_scientist = [
        "Python, Machine Learning, TensorFlow, SQL, Pandas, Scikit-learn",
        "Python, Deep Learning, NLP, PyTorch, SQL",
        "R, Python, Machine Learning, Statistics, SQL",
        "Python, Keras, TensorFlow, Computer Vision, OpenCV",
        "Python, Scikit-learn, XGBoost, SQL, MLflow"
    ]
    competences_dev = [
        "React, Node.js, PostgreSQL, Docker, AWS, Git",
        "Angular, Spring Boot, Java, MySQL, Docker",
        "Python, Django, PostgreSQL, React, Git",
        "Vue.js, Laravel, PHP, MySQL, Docker",
        "React Native, Node.js, MongoDB, AWS"
    ]
    competences_devops = [
        "Docker, Kubernetes, Terraform, AWS, CI/CD, Git",
        "Azure DevOps, Docker, Kubernetes, Terraform, Jenkins",
        "AWS, Docker, Ansible, Jenkins, Linux, Git",
        "GCP, Kubernetes, Terraform, Docker, Prometheus"
    ]

    # Descriptions par profil
    descriptions_data = [
        "Nous recherchons un Data Engineer expérimenté pour rejoindre notre équipe data. Le candidat devra concevoir et maintenir nos pipelines de données. Maîtrise de Python, Spark et Airflow requise. Expérience avec les plateformes cloud (AWS/GCP/Azure) souhaitée. Travail en méthode Agile.",
        "Rejoignez notre équipe data en pleine croissance. Vous serez responsable de la conception des architectures de données et de l'optimisation de nos pipelines ETL. Compétences requises : Python, SQL, orchestration de workflows. Connaissance de dbt et Kafka appréciée.",
        "Dans le cadre du développement de notre Data Lake, nous cherchons un Ingénieur Data. Vous travaillerez sur l'ingestion, la transformation et la mise à disposition des données. Stack : Python, Spark, Airflow, cloud AWS.",
    ]
    descriptions_analyst = [
        "Nous recherchons un Data Analyst pour analyser nos données business et produire des rapports stratégiques. Maîtrise de SQL et Power BI indispensable. Python apprécié. Vous travaillerez en étroite collaboration avec les équipes métier.",
        "Rejoignez notre département Business Intelligence. Vous serez chargé de créer des dashboards et d'analyser les KPIs. Compétences requises : SQL, Power BI ou Tableau, Excel avancé.",
        "Poste de Data Analyst au sein de notre équipe analytique. Vous analyserez les données clients et produirez des insights actionnables. Stack : SQL, Python, Metabase, Excel.",
    ]
    descriptions_scientist = [
        "Nous recrutons un Data Scientist pour développer nos modèles de machine learning et d'intelligence artificielle. Maîtrise de Python, Scikit-learn, TensorFlow requise. PhD ou Bac+5 en Data Science ou équivalent.",
        "Rejoignez notre équipe IA pour développer des algorithmes de recommandation et de prédiction. Compétences : Python, Machine Learning, Deep Learning, SQL, statistiques avancées.",
    ]
    descriptions_dev = [
        "Nous cherchons un développeur Full Stack pour rejoindre notre équipe produit. Stack : React, Node.js, PostgreSQL. Connaissance de Docker et des méthodes Agile souhaitée.",
        "Poste de développeur Backend pour développer nos APIs et microservices. Compétences : Java, Spring Boot, Docker, SQL. Expérience en architecture microservices appréciée.",
    ]

    # Niveaux d'études
    niveaux_etudes = ["Bac+3", "Bac+5", "Bac+2", "Bac+4", "Doctorat", "Bac+5 Ingénieur"]

    # Télétravail
    teletravail_options = [
        "Présentiel", "Hybride", "Télétravail", "Remote", "100% Remote",
        "Hybride (2j/semaine)", "Présentiel uniquement", None
    ]

    # Langues
    langues_options = [
        ["Français"], ["Français", "Anglais"], ["Anglais"],
        ["Français", "Anglais", "Arabe"], ["Français", "Arabe"]
    ]

    # Secteurs
    secteurs = [
        "Informatique / Télécom", "Banque / Finance", "E-commerce",
        "Conseil IT", "Industrie", "Santé", "Énergie", "Logistique"
    ]

    # Expériences avec problèmes intentionnels
    experiences = [
        "0-1 ans", "1-2 ans", "2-3 ans", "3-5 ans", "5-7 ans", "7-10 ans",
        "Débutant accepté", "min 2 ans", "min 3 ans", "Senior (5+ ans)",
        "3 à 5 ans", "2 à 4 ans", None
    ]

    # Salaires avec problèmes intentionnels
    def generer_salaire():
        salaire_type = random.choices(
            ['fourchette_mad', 'k_mad', 'eur', 'txt', 'null'],
            weights=[35, 25, 10, 20, 10]
        )[0]

        if salaire_type == 'fourchette_mad':
            base = random.choice([8, 10, 12, 15, 18, 20, 25])
            return f"{base}000-{base + random.randint(3, 8)}000 MAD"
        elif salaire_type == 'k_mad':
            base = random.choice([8, 10, 12, 15, 18, 20])
            return f"{base}K-{base + random.randint(3, 8)}K"
        elif salaire_type == 'eur':
            base = random.randint(1500, 4000)
            return f"{base}-{base + random.randint(500, 1500)} EUR"
        elif salaire_type == 'txt':
            return random.choice(["Selon profil", "Confidentiel", "À négocier", "Non communiqué"])
        else:
            return None

    # Entreprises marocaines réalistes
    entreprises = [
        "TechMaroc SARL", "DataSolutions MA", "InnovateTech Maroc",
        "CloudSys Maroc", "DigitalHub Casablanca", "AI Solutions Maroc",
        "Maroc Telecom", "Attijariwafa Bank", "BMCE Bank", "OCP Group",
        "HPS", "SQLI Maroc", "Capgemini Maroc", "CGI Maroc",
        "Intelcia", "Webhelp Maroc", "IBM Maroc", "Oracle Maroc",
        "Microsoft Maroc", "SAP Maroc", "Sofrecom", "Accenture Maroc",
        "Deloitte Maroc", "McKinsey Maroc", "PwC Maroc",
        "StartupDev Tanger", "TechHub Rabat", "DataFactory Maroc",
        "NearShore Maroc", "BO Consulting", "Leyton Maroc",
        "Lydec", "Redal", "RAM IT", "ONCF Digital",
        "Tanger Med Tech", "Free2Move Maroc", "Renault Maroc IT"
    ]

    offres = []
    for i in range(n):

        # Choisir un profil dominant
        profil_type = random.choices(
            ['data_eng', 'analyst', 'scientist', 'dev', 'devops', 'autre'],
            weights=[20, 20, 10, 25, 15, 10]
        )[0]

        if profil_type == 'data_eng':
            titre = random.choice(titres_data)
            comp = random.choice(competences_data_eng)
            desc = random.choice(descriptions_data)
        elif profil_type == 'analyst':
            titre = random.choice(titres_analyst)
            comp = random.choice(competences_analyst)
            desc = random.choice(descriptions_analyst)
        elif profil_type == 'scientist':
            titre = random.choice(titres_science)
            comp = random.choice(competences_scientist)
            desc = random.choice(descriptions_scientist)
        elif profil_type == 'dev':
            titre = random.choice(titres_dev)
            comp = random.choice(competences_dev)
            desc = random.choice(descriptions_dev)
        elif profil_type == 'devops':
            titre = random.choice(titres_infra)
            comp = random.choice(competences_devops)
            desc = fake.paragraph(nb_sentences=3) + " Compétences: Docker, Kubernetes, AWS, Terraform."
        else:
            titre = random.choice(titres_autre)
            comp = "Gestion de projet, Agile, Scrum, Communication"
            desc = fake.paragraph(nb_sentences=3)

        # Dates cohérentes
        date_pub = fake.date_between(start_date='-2y', end_date='today')
        date_exp = fake.date_between(start_date=date_pub, end_date='+3m')

        # Quelques dates incohérentes intentionnelles (~3%)
        if random.random() < 0.03:
            date_exp = fake.date_between(start_date='-3y', end_date=date_pub)

        offres.append({
            "id_offre": f"RK-{date_pub.year}-{random.randint(10000, 99999)}",
            "source": random.choice(["rekrute", "marocannonce", "linkedin"]),
            "titre_poste": titre,
            "description": desc,
            "competences_brut": comp,
            "entreprise": random.choice(entreprises),
            "ville": random.choice(villes),
            "type_contrat": random.choice(contrats),
            "experience_requise": random.choice(experiences),
            "salaire_brut": generer_salaire(),
            "niveau_etudes": random.choice(niveaux_etudes),
            "secteur": random.choice(secteurs),
            "date_publication": date_pub.isoformat(),
            "date_expiration": date_exp.isoformat(),
            "nb_postes": random.choice([1, 1, 1, 2, 3]),
            "teletravail": random.choice(teletravail_options),
            "langue_requise": random.choice(langues_options)
        })

    return {"offres": offres}


if __name__ == "__main__":
    print("Génération de 5000 offres d'emploi IT marocaines...")
    data = generate_job_data(5000)
    with open('offres_emploi_it_maroc.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Fichier 'offres_emploi_it_maroc.json' généré avec {len(data['offres'])} offres !")
    print("📁 Fichier sauvegardé dans le dossier courant.")