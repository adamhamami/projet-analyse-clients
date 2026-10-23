
import pandas as pd
import matplotlib.pyplot as plt

# 1. Charger les donnees
df = pd.read_csv("clients.csv")

# 2. Supprimer les doublons complets
df_clean = df.drop_duplicates().copy()

# 3. Traiter les valeurs manquantes
df_clean["age"] = df_clean["age"].fillna(
    df_clean["age"].median()
)

df_clean["city"] = df_clean["city"].fillna("Inconnue")

# 4. Afficher l'anciennete et les depenses
print("\n--- ANCIENNETE ET DEPENSES ---")

print(
    df_clean[
        ["client_id", "months_active", "monthly_spend"]
    ].to_string(index=False)
)

# 5. Calculer la correlation entre anciennete et depenses
print("\n--- CORRELATION ANCIENNETE ET DEPENSES ---")

correlation = df_clean["months_active"].corr(
    df_clean["monthly_spend"]
)

print("Correlation :", round(correlation, 2))

# 6. Trier les clients par anciennete
print("\n--- CLIENTS PAR ANCIENNETE DECROISSANTE ---")

clients_anciennete = df_clean.sort_values(
    by="months_active",
    ascending=False
)

print(
    clients_anciennete[
        ["client_id", "months_active", "monthly_spend"]
    ].to_string(index=False)
)

# 7. Creer un graphique en nuage de points
print("\n--- GENERATION DU GRAPHIQUE ---")

plt.figure(figsize=(8, 5))

plt.scatter(
    df_clean["months_active"],
    df_clean["monthly_spend"]
)

plt.title("Anciennete et depenses mensuelles des clients")
plt.xlabel("Anciennete (mois)")
plt.ylabel("Depense mensuelle (DH)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 8. Enregistrer le graphique
plt.savefig("correlation_anciennete_depenses.png", dpi=150)

# 9. Afficher le graphique
plt.show()
