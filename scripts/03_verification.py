
from pathlib import Path
import pandas as pd

# ==========================================
# 1. CONFIGURATION DES CHEMINS
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "data" / "clients.csv"
OUTPUT_DIR = ROOT_DIR / "outputs"

# ==========================================
# 2. CHARGEMENT DES DONNEES
# ==========================================

df_initial = pd.read_csv(DATA_FILE)

# Nettoyage identique aux autres scripts
df = df_initial.drop_duplicates().copy()
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("Inconnue")

# ==========================================
# 3. VERIFICATION DES DONNEES
# ==========================================

print("\n--- VERIFICATION FINALE ---")

print("Lignes initiales :", len(df_initial))
print("Lignes apres nettoyage :", len(df))

print("Doublons restants :", df.duplicated().sum())
print("Valeurs manquantes :", df.isnull().sum().sum())

revenu_total = df["monthly_spend"].sum()
print("Revenu mensuel total :", revenu_total, "DH")

# Vérifier les revenus par ville
print("\n--- REVENUS PAR VILLE ---")

revenus_ville = df.groupby("city")["monthly_spend"].sum()
print(revenus_ville)

print("\nSomme des revenus par ville :", revenus_ville.sum(), "DH")

# ==========================================
# 4. CONTROLES AUTOMATIQUES
# ==========================================

print("\n--- CONTROLES AUTOMATIQUES ---")

verifications = {
    "14 lignes apres nettoyage": len(df) == 14,
    "Aucun doublon restant": df.duplicated().sum() == 0,
    "Aucune valeur manquante": df.isnull().sum().sum() == 0,
    "Revenu total egal a 2976 DH": revenu_total == 2976,
    "Somme des revenus par ville correcte": revenus_ville.sum() == revenu_total,
}

for nom, resultat in verifications.items():
    statut = "OK" if resultat else "ECHEC"
    print(f"[{statut}] {nom}")

# ==========================================
# 5. VERIFICATION DES GRAPHIQUES
# ==========================================

print("\n--- FICHIERS GRAPHIQUES ---")

graphiques = [
    "depenses_par_abonnement.png",
    "correlation_anciennete_depenses.png",
    "revenus_par_ville.png",
]

for nom_fichier in graphiques:
    chemin = OUTPUT_DIR / nom_fichier
    existe = chemin.is_file()

    statut = "OK" if existe else "MANQUANT"
    print(f"[{statut}] {nom_fichier} : {existe}")

    verifications[f"Graphique present : {nom_fichier}"] = existe

# ==========================================
# 6. RESULTAT FINAL
# ==========================================

print("\n--- RESULTAT FINAL ---")

if all(verifications.values()):
    print("Toutes les verifications sont reussies.")
else:
    print("Certaines verifications ont echoue.")
    print("Corrige les erreurs indiquees ci-dessus.")
