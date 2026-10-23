
# Analyse intelligente des données clients

Projet Python d'exploration, de nettoyage et d'analyse de données clients à l'aide de Pandas et Matplotlib.

## Objectif du projet

L'objectif est d'analyser un jeu de données clients afin de comprendre les dépenses mensuelles, de comparer les abonnements, d'étudier les revenus par ville et d'examiner la relation entre l'ancienneté des clients et leurs dépenses.

## Fonctionnalités

- Exploration des données et statistiques descriptives.
- Détection des valeurs manquantes et des doublons.
- Nettoyage des données : suppression des doublons, remplacement des âges manquants par la médiane et des villes manquantes par `Inconnue`.
- Analyse des dépenses moyennes par abonnement.
- Analyse du nombre de clients et des revenus par ville.
- Tableau croisé entre les villes et les abonnements.
- Calcul de la corrélation entre l'ancienneté et les dépenses mensuelles.
- Génération de graphiques et vérifications automatiques des résultats.

## Technologies utilisées

- Python
- Pandas
- Matplotlib
- Git et GitHub

## Structure du projet

```text
projet-analyse-clients/
├── data/
│   └── clients.csv
├── scripts/
│   ├── 01_exploration.py
│   ├── 02_analyse_avancee.py
│   └── 03_verification.py
├── outputs/
│   ├── depenses_par_abonnement.png
│   ├── revenus_par_ville.png
│   └── correlation_anciennete_depenses.png
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/adamhamami/projet-analyse-clients.git
cd projet-analyse-clients
```

### 2. Créer un environnement virtuel

Sous Windows PowerShell :

```powershell
python -m venv .venv
```

### 3. Activer l'environnement virtuel

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Exécution

Depuis la racine du projet, exécuter les scripts dans cet ordre :

```powershell
python scripts/01_exploration.py
python scripts/02_analyse_avancee.py
python scripts/03_verification.py
```

Les graphiques sont enregistrés dans le dossier `outputs/`.

## Résultats obtenus

Sur le jeu de données fourni :

| Indicateur | Résultat |
|---|---:|
| Nombre de lignes initiales | 15 |
| Nombre de lignes après nettoyage | 14 |
| Doublons restants | 0 |
| Valeurs manquantes après nettoyage | 0 |
| Dépenses mensuelles totales | 2 976 DH |
| Corrélation ancienneté-dépenses | 0,92 |

### Dépenses moyennes par abonnement

| Abonnement | Dépense moyenne |
|---|---:|
| Basic | 93 DH |
| Standard | 179 DH |
| Premium | 359 DH |

### Revenus mensuels par ville

| Ville | Revenus |
|---|---:|
| Rabat | 976 DH |
| Tanger | 897 DH |
| Casablanca | 686 DH |
| Marrakech | 238 DH |
| Inconnue | 179 DH |

La corrélation positive de 0,92 indique une forte association linéaire entre l'ancienneté et les dépenses dans cet échantillon. Elle ne démontre pas, à elle seule, une relation de causalité.

## Limites

Ce projet utilise un petit jeu de données de démonstration comprenant 15 lignes initiales. Les résultats sont descriptifs et ne peuvent pas être généralisés à une clientèle réelle sans données supplémentaires.

## Auteur

**hamami adam**

Projet d'analyse de données réalisé avec Python, Pandas et Matplotlib.

## Licence

Projet pédagogique. Aucune licence spécifique n'est définie pour le moment.
