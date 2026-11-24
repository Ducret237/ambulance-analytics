

import csv

# 1. Lire les interventions
interventions = []

with open("data/interventions.csv", "r", encoding="utf-8", newline="") as fichier:
    lecteur = csv.DictReader(fichier)

    for intervention in lecteur:
        interventions.append(intervention)


# 2. Compter les interventions
nombre_interventions = len(interventions)


# 3. Préparer les statistiques
total_delais = 0
delais = []
interventions_par_region = {}


# 4. Parcourir les interventions
for intervention in interventions:

    # Convertir et additionner le délai
    delai = int(intervention["delai_minutes"])
    total_delais += delai
    delais.append(delai)

    # Compter les interventions par région
    region = intervention["region"]

    interventions_par_region[region] = (
        interventions_par_region.get(region, 0) + 1
    )


# 5. Afficher les statistiques
print("===== AMBULANCE ANALYTICS =====")

print(f"Nombre total d'interventions : {nombre_interventions}")

if nombre_interventions > 0:
    moyenne = total_delais / nombre_interventions
    delai_maximum = max(delais)

    print(f"Délai moyen : {moyenne:.1f} minutes")
    print(f"Délai maximum : {delai_maximum} minutes")
else:
    print("Aucune intervention disponible.")


# 6. Afficher les interventions par région
print("\nInterventions par région :")

for region, nombre in interventions_par_region.items():
    print(f"- {region} : {nombre}")

print("================================")

# 7. Afficher la region ayant le plus d'interventions

if interventions_par_region:
    region_max = max(interventions_par_region, key=interventions_par_region.get)
    nombre_max = interventions_par_region[region_max]

    print(f"\nRégion avec le plus d'interventions : {region_max} ({nombre_max})")
