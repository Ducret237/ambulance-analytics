
import csv

with open("data/interventions.csv", "r", encoding="utf-8", newline="") as fichier:
    lecteur = csv.DictReader(fichier)

    for intervention in lecteur:
        
     print(f"Intervention {intervention['id']} - {intervention['region']} - {intervention['delai_minutes']} minutes")
    

