import pandas as pd

# 1. Charger les données
df = pd.read_csv("clients.csv")

# 2. Afficher les premières lignes
print("\n--- APERCU DES DONNEES ---")
print(df.head())

# 3. Dimensions du dataset
print("\n--- DIMENSIONS ---")
print(df.shape)

# 4. Noms des colonnes
print("\n--- COLONNES ---")
print(df.columns)

# 5. Informations générales
print("\n--- INFORMATIONS GENERALES ---")
df.info()

# 6. Statistiques descriptives
print("\n--- STATISTIQUES ---")
print(df.describe())

# 7. Valeurs manquantes
print("\n--- VALEURS MANQUANTES ---")
print(df.isnull().sum())

# 8. Lignes entièrement dupliquées
print("\n--- DOUBLONS COMPLETS ---")
print(df.duplicated().sum())

# 9. Identifiants clients dupliqués
print("\n--- IDENTIFIANTS DUPLIQUES ---")
print(df["client_id"].duplicated().sum())

# --- NETTOYAGE DES DONNEES ---

# 1. Créer une copie pour conserver les données originales
df_clean = df.copy()

# 2. Supprimer les lignes entièrement dupliquées
df_clean = df_clean.drop_duplicates()

# 3. Calculer la médiane des âges
median_age = df_clean["age"].median()

# 4. Remplacer les âges manquants par la médiane
df_clean["age"] = df_clean["age"].fillna(median_age)

# 5. Remplacer les villes manquantes par "Inconnue"
df_clean["city"] = df_clean["city"].fillna("Inconnue")

# 6. Vérifier le résultat
print("\n--- APRES NETTOYAGE ---")
print("Dimensions :", df_clean.shape)

print("\nValeurs manquantes :")
print(df_clean.isnull().sum())

print("\nDoublons complets :", df_clean.duplicated().sum())

print("\nDataset nettoyé :")
print(df_clean.to_string(index=False))

print("\n--- VERIFICATION DES COLONNES ---")

print(
    df_clean[
        ["client_id", "monthly_spend", "months_active"]
    ].to_string(index=False)
)

print("\n--- TYPES DES COLONNES ---")
print(df_clean.dtypes)

# --- ANALYSE COMMERCIALE ---

print("\n--- 1. REVENU MENSUEL TOTAL ---")
total_revenue = df_clean["monthly_spend"].sum()
print(f"Revenu mensuel total : {total_revenue} DH")

print("\n--- 2. DEPENSE MOYENNE PAR ABONNEMENT ---")
spend_by_subscription = df_clean.groupby("subscription")["monthly_spend"].mean()
print(spend_by_subscription.round(2))

print("\n--- 3. NOMBRE DE CLIENTS PAR VILLE ---")
clients_by_city = df_clean["city"].value_counts()
print(clients_by_city)

print("\n--- 4. TOP 5 CLIENTS ---")
top_clients = df_clean.sort_values(
    by="monthly_spend",
    ascending=False
).head(5)

print(
    top_clients[
        ["client_id", "city", "subscription", "monthly_spend"]
    ].to_string(index=False)
)

import matplotlib.pyplot as plt

# Calculer la dépense moyenne par abonnement
spend_by_subscription = (
    df_clean.groupby("subscription")["monthly_spend"].mean()
)

# Créer le graphique
plt.figure(figsize=(8, 5))

spend_by_subscription.plot(kind="bar")

plt.title("Depense mensuelle moyenne par abonnement")
plt.xlabel("Type d'abonnement")
plt.ylabel("Depense moyenne (DH)")
plt.xticks(rotation=0)
plt.tight_layout()

# Enregistrer le graphique
plt.savefig("depenses_par_abonnement.png", dpi=150)

# Afficher le graphique
plt.show()