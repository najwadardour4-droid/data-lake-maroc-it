from pipeline.bronze_ingestion import ingerer_bronze
from pipeline.silver_transform import charger_depuis_bronze, nettoyer_titres_postes, normaliser_salaires, normaliser_experience
from pipeline.silver_nlp import extraire_competences, sauvegarder_silver
from pipeline.gold_aggregation import construire_gold

# 1. Ingestion Bronze
# T-akedi beli l-fichier .json kayna f nafs l-blassa
ingerer_bronze('offres_emploi_it_maroc.json', 'data_lake_mexora_rh')

# 2. Transformation Silver
df = charger_depuis_bronze('data_lake_mexora_rh')
df = nettoyer_titres_postes(df)
df = normaliser_salaires(df)
df = normaliser_experience(df)

# 3. NLP & Sauvegarde Silver
df_comp = extraire_competences(df, 'referentiel_competences_it.json')
sauvegarder_silver(df, df_comp, 'data_lake_mexora_rh')

# 4. Gold (Analytics)
construire_gold('data_lake_mexora_rh')