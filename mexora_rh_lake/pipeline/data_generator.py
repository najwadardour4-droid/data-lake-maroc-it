import json
import random
import os
from faker import Faker

fake = Faker(['fr_FR'])

def generate_job_data(n=5000):
    # Les problèmes intentionnels demandés (villes, titres, salaires)
    villes = ["Casablanca", "casa", "CASABLANCA", "Rabat", "rabat", "Tanger", "tanger", "Marrakech", "Agadir"]
    titres = ["Data Engineer", "Data Eng.", "Dev Data", "Data Analyst", "BI Analyst", "Data Scientist", "Dev Fullstack"]
    contrats = ["CDI", "cdi", "Freelance", "CDD", "Permanent"]
    
    offres = []
    for i in range(n):
        # Simulation des salaires mixtes (MAD, EUR, K, null)
        salaire_type = random.choice(['fourchette', 'k', 'eur', 'txt'])
        if salaire_type == 'fourchette':
            salaire = f"{random.randint(10, 15)}000-{random.randint(16, 25)}000 MAD"
        elif salaire_type == 'k':
            salaire = f"{random.randint(15, 20)}K-{random.randint(21, 28)}K"
        elif salaire_type == 'eur':
            salaire = f"{random.randint(2000, 5000)} EUR"
        else:
            salaire = random.choice(["Selon profil", "Confidentiel", None])

        offres.append({
            "id_offre": f"RK-2024-{random.randint(10000, 99999)}",
            "source": random.choice(["rekrute", "marocannonce", "linkedin"]),
            "titre_poste": random.choice(titres),
            "description": fake.paragraph(nb_sentences=3) + " Compétences: Python, SQL, Spark, Docker.",
            "competences_brut": "Python, SQL, Cloud, Docker",
            "entreprise": fake.company(),
            "ville": random.choice(villes),
            "type_contrat": random.choice(contrats),
            "experience_requise": f"{random.randint(0, 5)}-{random.randint(6, 10)} ans",
            "salaire_brut": salaire,
            "date_publication": fake.date_between(start_date='-1y', end_date='today').isoformat()
        })
    return {"offres": offres}

if __name__ == "__main__":
    # Sauvegarde à la racine du projet
    data = generate_job_data(5000)
    with open('offres_emploi_it_maroc.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ Fichier 'offres_emploi_it_maroc.json' généré avec 5000 offres !")