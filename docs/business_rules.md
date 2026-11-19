ID	    Règle
RG-01	Chaque intervention possède un identifiant unique et non vide.
RG-02	Chaque intervention appartient à une seule région.
RG-03	Une région peut être associée à zéro ou plusieurs interventions.
RG-04	Chaque intervention possède un seul type.
RG-05	Un type peut être associé à zéro ou plusieurs interventions.
RG-06	La priorité appartient à l'ensemble des valeurs 1, 2 et 3.
RG-07	La date et l'heure de réception de l'appel sont obligatoires et valides.
RG-08	La date et l'heure d'arrivée sont obligatoires et valides.
RG-09	L'arrivée ne peut pas précéder la réception de l'appel.
RG-10	Deux interventions portant le même identifiant ne peuvent pas être enregistrées séparément.
RG-11	Une intervention invalide doit être rejetée et signalée.
RG-12	Aucune donnée personnelle ou médicale réelle ne doit être utilisée.
RG-13	Un doublon contradictoire ne doit pas écraser une intervention existante. Si plusieurs lignes contradictoires concernent un nouvel identifiant, elles sont toutes rejetées.