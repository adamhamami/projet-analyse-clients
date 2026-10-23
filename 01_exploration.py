
import pandas as pd
import matplotlib.pyplot as plt

# 1. Charger les donnees
df = pd.read_csv("clients.csv")

# 2. Afficher les premieres lignes
print("\n--- APERCU DES DONNEES ---")
print(df.head())

# 3. Dimensions du dataset
print("\n--- DIMENSIONS ---")
print(df.shape)

# 4. Noms des colonnes
print("\n--- COLONNES ---")
print(df.columns)

# 5. Informations generales
print("\n--- INFORMATIONS GENERALES ---")
df.info()

# 6. Statistiques descriptives
print("\n--- STATISTIQUES ---")
print(df.describe())

# 7. Valeurs manquantes
print("\n--- VALEURS MANQUANTES ---")
print(df.isnull().sum())

# 8. Lignes entierement dupliquees
print("\n--- DOUBLONS COMPLETS ---")
print(df.duplicated().sum())

# 9. Identifiants clients dupliques
print("\n--- IDENTIFIANTS DUPLIQUES ---")
print(df["client_id"].duplicated().sum())


# --- NETTOYAGE DES DONNEES ---

# 10. Creer une copie pour conserver les donnees originales
df_clean = df.copy()

# 11. Supprimer les doublons complets
df_clean = df_clean.drop_duplicates()

# 12. Calculer la mediane des ages
median_age = df_clean["age"].median()

# 13. Remplacer les ages manquants par la mediane
df_clean["age"] = df_clean["age"].fillna(median_age)

# 14. Remplacer les villes manquantes
df_clean["city"] = df_clean["city"].fillna("Inconnue")

# 15. Verifier le nettoyage
print("\n--- APRES NETTOYAGE ---")
print("Dimensions :", df_clean.shape)

print("\nValeurs manquantes :")
print(df_clean.isnull().sum())

print("\nDoublons complets :", df_clean.duplicated().sum())

print("\nDataset nettoye :")
print(df_clean.to_string(index=False))


# --- VERIFICATION DES COLONNES ---

print("\n--- VERIFICATION DES COLONNES ---")

print(
    df_clean[
        ["client_id", "monthly_spend", "months_active"]
    ].to_string(index=False)
)

print("\n--- TYPES DES COLONNES ---")
print(df_clean.dtypes)


# --- ANALYSE COMMERCIALE ---

# 1. Revenu mensuel total
print("\n--- 1. REVENU MENSUEL TOTAL ---")

total_revenue = df_clean["monthly_spend"].sum()

print(f"Revenu mensuel total : {total_revenue} DH")


# 2. Depense moyenne par abonnement
print("\n--- 2. DEPENSE MOYENNE PAR ABONNEMENT ---")

spend_by_subscription = (
    df_clean.groupby("subscription")["monthly_spend"].mean()
)

print(spend_by_subscription.round(2))


# 3. Nombre de clients par ville
print("\n--- 3. NOMBRE DE CLIENTS PAR VILLE ---")

clients_by_city = df_clean["city"].value_counts()

print(clients_by_city)


# 4. Top 5 clients
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


# 5. Revenu mensuel par ville
print("\n--- 5. REVENU MENSUEL PAR VILLE ---")

revenue_by_city = (
    df_clean.groupby("city")["monthly_spend"]
    .sum()
    .sort_values(ascending=False)
)

print(revenue_by_city)


# --- VISUALISATION 1 : DEPENSE PAR ABONNEMENT ---

spend_by_subscription = (
    df_clean.groupby("subscription")["monthly_spend"].mean()
)

plt.figure(figsize=(8, 5))

spend_by_subscription.plot(kind="bar")

plt.title("Depense mensuelle moyenne par abonnement")
plt.xlabel("Type d'abonnement")
plt.ylabel("Depense moyenne (DH)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("depenses_par_abonnement.png", dpi=150)
plt.show()


# --- VISUALISATION 2 : REVENU PAR VILLE ---

plt.figure(figsize=(8, 5))

revenue_by_city.plot(kind="bar")

plt.title("Revenu mensuel total par ville")
plt.xlabel("Ville")
plt.ylabel("Revenu mensuel total (DH)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("revenus_par_ville.png", dpi=150)
plt.show()
