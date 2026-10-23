
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. CONFIGURATION DES CHEMINS
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "data" / "clients.csv"
OUTPUT_DIR = ROOT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# ==========================================
# 2. CHARGEMENT ET NETTOYAGE
# ==========================================

df = pd.read_csv(DATA_FILE)

df = df.drop_duplicates().copy()
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("Inconnue")

# ==========================================
# 3. ANALYSE DE L'ANCIENNETE
# ==========================================

print("\n--- ANCIENNETE ET DEPENSES ---")

print(df[["client_id", "months_active", "monthly_spend"]])

# ==========================================
# 4. CALCUL DE LA CORRELATION
# ==========================================

correlation = df["months_active"].corr(df["monthly_spend"])

print("\n--- CORRELATION ANCIENNETE ET DEPENSES ---")
print(f"Correlation : {correlation:.2f}")

# ==========================================
# 5. TRI DES CLIENTS
# ==========================================

print("\n--- CLIENTS PAR ANCIENNETE DECROISSANTE ---")

clients_tries = df.sort_values(
    by="months_active",
    ascending=False
)

print(clients_tries[["client_id", "months_active", "monthly_spend"]])

# ==========================================
# 6. GENERATION DU GRAPHIQUE
# ==========================================

print("\n--- GENERATION DU GRAPHIQUE ---")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["months_active"],
    df["monthly_spend"]
)

plt.title("Relation entre anciennete et depenses")
plt.xlabel("Anciennete (mois)")
plt.ylabel("Depenses mensuelles (DH)")
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Enregistrer obligatoirement dans outputs/
graph_file = OUTPUT_DIR / "correlation_anciennete_depenses.png"
plt.savefig(graph_file, dpi=150)
plt.close()

print(f"Graphique enregistre : {graph_file}")
print("\n--- ANALYSE AVANCEE TERMINEE ---")
