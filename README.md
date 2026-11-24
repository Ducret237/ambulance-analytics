# Ambulance Analytics

## Présentation

Ambulance Analytics est un mini-projet personnel développé en Python dans le but de pratiquer la manipulation de fichiers CSV, les calculs statistiques, les dictionnaires et l'organisation du code.

L'application analyse un jeu de données fictives d'interventions ambulancières et présente les principaux résultats dans le terminal.

## Fonctionnalités

- Lecture des interventions à partir d'un fichier CSV.
- Calcul du nombre total d'interventions.
- Calcul du délai moyen d'intervention.
- Calcul du délai maximum.
- Comptage des interventions par région.
- Tests automatisés simples.

## Technologies

- Python 3
- Module `csv`
- Module `unittest`
- Git et GitHub

Aucune bibliothèque externe n'est nécessaire.

## Structure du projet

```text
ambulance-analytics/
├── data/
│   └── interventions.csv
├── tests/
│   └── test_analyse.py
├── analyse.py
├── README.md
└── .gitignore
```

## Exécution

Depuis le dossier principal du projet :

```bash
python analyse.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Données

Le fichier `data/interventions.csv` contient uniquement des données fictives.

Les colonnes utilisées sont :

- `id` : identifiant de l'intervention.
- `region` : région associée.
- `delai_minutes` : délai d'intervention en minutes.

## Limites actuelles

Cette première version suppose que le fichier CSV existe et que les délais sont des nombres entiers valides.

Elle ne comporte pas d'interface graphique, de base de données ni de traitement avancé des erreurs.

## Objectif pédagogique

Ce projet permet de mettre en pratique les fondamentaux de Python et les bonnes pratiques de versionnement, de documentation et de tests logiciels.
