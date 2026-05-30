from pipeline.bronze_ingestion import ingerer_bronze
from pipeline.silver_transform import charger_depuis_bronze, nettoyer_titres_postes, normaliser_salaires, normaliser_experience, normaliser_villes, normaliser_type_contrat, ajouter_colonnes_date
from pipeline.silver_nlp import extraire_competences, sauvegarder_silver
from pipeline.gold_aggregation import construire_gold

DATA_LAKE = 'data_lake_mexora_rh'
JSON_OFFRES = 'offres_emploi_it_maroc.json'
REFERENTIEL = 'referentiel_competences_it.json'

# 1. Ingestion Bronze
print("=== ETAPE 1 : BRONZE ===")
ingerer_bronze(JSON_OFFRES, DATA_LAKE)

# 2. Transformation Silver
print("\n=== ETAPE 2 : SILVER ===")
df = charger_depuis_bronze(DATA_LAKE)
df = nettoyer_titres_postes(df)
df = normaliser_salaires(df)
df = normaliser_experience(df)
df = normaliser_villes(df)
df = normaliser_type_contrat(df)
df = ajouter_colonnes_date(df)

# 3. NLP & Sauvegarde Silver
print("\n=== ETAPE 3 : NLP ===")
df_comp = extraire_competences(df, REFERENTIEL)
sauvegarder_silver(df, df_comp, DATA_LAKE)

# 4. Gold
print("\n=== ETAPE 4 : GOLD ===")
construire_gold(DATA_LAKE)

print("\n✅ Pipeline terminé avec succès !")