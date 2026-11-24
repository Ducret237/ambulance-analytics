
import csv

# Lecture des données
interventions = []

with open("data/interventions.csv", "r", encoding="utf-8", newline="") as fichier:
    lecteur = csv.DictReader(fichier)

    for intervention in lecteur:
        interventions.append(intervention)


# Compter les interventions
nombre_interventions = len(interventions)


# Additionner les délais
total_delais = 0

for intervention in interventions:
    delai = int(intervention["delai_minutes"])
    total_delais = total_delais + delai


# Afficher les statistiques
print("===== AMBULANCE ANALYTICS =====")

print(f"Nombre total d'interventions : {nombre_interventions}")

if nombre_interventions > 0:
    moyenne = total_delais / nombre_interventions
    print(f"Délai moyen : {moyenne:.1f} minutes")
else:
    print("Aucune intervention disponible.")

print("================================")

# Afficher le delais maximun 

Liste_delais = [int(intervention["delai_minutes"]) for intervention in interventions]

delai_max = max(Liste_delais)
print(f"Délai maximum : {delai_max} minutes")
