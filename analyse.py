


import csv


# 1. Lire les données du fichier CSV
def lire_interventions(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        return list(lecteur)


# 2. Calculer les statistiques des délais
def calculer_statistiques(interventions):
    delais = []

    for intervention in interventions:
        delai = int(intervention["delai_minutes"])
        delais.append(delai)

    nombre = len(delais)

    if nombre == 0:
        return {
            "nombre": 0,
            "moyenne": None,
            "maximum": None
        }

    return {
        "nombre": nombre,
        "moyenne": sum(delais) / nombre,
        "maximum": max(delais)
    }


# 3. Compter les interventions par région
def compter_par_region(interventions):
    repartition = {}

    for intervention in interventions:
        region = intervention["region"]
        repartition[region] = repartition.get(region, 0) + 1

    return repartition


# 4. Afficher les résultats
def afficher_resultats(statistiques, repartition):
    print("===== AMBULANCE ANALYTICS =====")

    print(f"Nombre total d'interventions : {statistiques['nombre']}")

    if statistiques["nombre"] > 0:
        print(f"Délai moyen : {statistiques['moyenne']:.1f} minutes")
        print(f"Délai maximum : {statistiques['maximum']} minutes")
    else:
        print("Aucune intervention disponible.")

    print("\nInterventions par région :")

    if not repartition:
        print("- Aucune intervention")

    for region, nombre in repartition.items():
        print(f"- {region} : {nombre}")

    print("================================")


# 5. Fonction principale
def main():
    interventions = lire_interventions("data/interventions.csv")

    statistiques = calculer_statistiques(interventions)

    repartition = compter_par_region(interventions)

    afficher_resultats(statistiques, repartition)


# 6. Point d'entrée du programme
if __name__ == "__main__":
    main()

# 7. Compter le nombre de régions distinctes
def compter_regions(interventions):
    regions = set()
    for intervention in interventions:
        regions.add(intervention["region"])
    return len(regions)