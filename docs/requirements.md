2. Mise en situation
Imaginons une organisation fictive chargée du suivi des services ambulanciers de plusieurs régions du Québec.

Chaque intervention génère des informations : région, heure de réception de l'appel, heure d'arrivée de l'ambulance, type d'intervention et niveau de priorité.

Ces informations sont enregistrées dans différents fichiers CSV.

Cependant, leur exploitation présente plusieurs difficultés :
- Présence de doublons.
- Difficulté à comparer les régions.
- Calcul manuel des indicateurs.
- Absence de visualisation centralisée.
- Difficulté à suivre l'évolution des délais d'intervention.
Demande du client fictif
Nous souhaitons disposer d'une application permettant de centraliser les données de nos interventions ambulancières, de vérifier leur qualité et de consulter les principaux indicateurs d'activité à travers un tableau de bord interactif.

3. Identification du problème
Problème identifié	Solution envisagée
Données dispersées	Pipeline d'intégration de données
Données incorrectes	Nettoyage et validation avec Python
Présence de doublons	Détection des identifiants dupliqués
Absence de stockage centralisé	Base de données SQLite
Calcul manuel des statistiques	Fonctions d'analyse automatisées
Difficulté de visualisation	Tableau de bord Streamlit
Difficulté de comparaison	Graphiques et filtres interactifs

4. Identification des parties prenantes
Partie prenante                                     	Rôle	                                                         Besoin principal
Gestionnaire des services ambulanciers	 Utilisateur principal	                                        Suivre les indicateurs d'activité
Analyste de données	 Utilisateur secondaire	                                                             Examiner et comparer les données
Responsable des données	Exploitation des données	                                        Importer et contrôler la qualité des fichiers
Développeur	Conception et maintenance	                                                     Développer, tester et documenter le logiciel
Organisation ambulancière fictive	Commanditaire	                                                      Disposer d'informations fiables

Dans notre première version, les trois profils d'utilisateurs pourront utiliser la même application locale. La gestion de comptes et de permissions individuelles n'est pas prévue dans le périmètre initial.

5. Objectif du produit (Product Goal)
Développer une application permettant de transformer des données fictives d'interventions ambulancières en informations structurées et exploitables, grâce à un pipeline Python, une base SQLite et un tableau de bord interactif

Partie 2 — Exigences du logiciel

6. Exigences fonctionnelles (EF)
Une exigence fonctionnelle décrit ce que le système doit permettre de réaliser.

Par exemple, « le système doit permettre à l'utilisateur d'importer un fichier CSV » constitue une exigence fonctionnelle.

Voici les exigences proposées pour Ambulance Analytics.

| ID | Fonctionnalité | Exigence fonctionnelle | Priorité |
| --- | --- | --- | --- |
| EF-01 | Importation | Le système doit permettre d'importer des données d'interventions depuis un fichier CSV. | Haute |
| EF-02 | Validation | Le système doit détecter les champs obligatoires manquants et les valeurs invalides. | Haute |
| EF-03 | Nettoyage | Le système doit normaliser les valeurs textuelles et éliminer les doublons identiques. | Haute |
| EF-04 | Stockage | Le système doit enregistrer les interventions valides dans une base SQLite sans créer de doublons. | Haute |
| EF-05 | Consultation | Le système doit permettre de consulter la liste des interventions enregistrées. | Haute |
| EF-06 | Calcul des délais | Le système doit calculer le délai entre la réception de l'appel et l'arrivée de l'ambulance. | Haute |
| EF-07 | Indicateurs | Le système doit afficher le nombre d'interventions, le délai moyen et le pourcentage d'arrivées dans un délai de 15 minutes. | Haute |
| EF-08 | Visualisation | Le système doit présenter des graphiques statistiques par région et par période. | Haute |
| EF-09 | Filtrage | Le système doit permettre de filtrer les données par région, période, priorité et type d'intervention. | Haute |
| EF-10 | Rapport d'importation | Le système doit indiquer le nombre de lignes importées, rejetées et ignorées comme doublons. | Moyenne |
| EF-11 | Exportation | Le système doit permettre d'exporter les données filtrées au format CSV. | Moyenne |

7. Exigences non fonctionnelles (ENF)
Une exigence non fonctionnelle décrit comment le système doit fonctionner, notamment en matière de performance, de sécurité, de fiabilité et de maintenabilité.

ID	Caractéristique	Exigence	Vérification prévue
ENF-01	Performance	Actualiser les indicateurs en moins de 3 secondes sur un jeu de 10 000 interventions, dans un environnement de référence documenté.	Test chronométré
ENF-02	Confidentialité	Utiliser exclusivement des données fictives, sans renseignements personnels ou médicaux réels.	Inspection du jeu de données
ENF-03	Sécurité	Utiliser des requêtes SQL paramétrées pour les valeurs provenant des utilisateurs ou des fichiers.	Revue du code
ENF-04	Fiabilité	Refuser les interventions invalides sans altérer les données déjà enregistrées.	Tests d'importation
ENF-05	Maintenabilité	Séparer l'extraction, la transformation, le stockage, les calculs et l'affichage.	Revue de l'architecture
ENF-06	Utilisabilité	Présenter des filtres identifiés, des unités explicites et des messages d'erreur compréhensibles.	Test manuel
ENF-07	Testabilité	Permettre de tester les fonctions de nettoyage et de calcul indépendamment de l'interface.	Tests Pytest
ENF-08	Reproductibilité	Permettre à une autre personne d'installer et d'exécuter le projet en suivant le README.	Installation depuis un nouveau clone
ENF-09	Portabilité	Permettre l'exécution locale sous Windows et Linux.	Vérification sur les deux environnements
ENF-10	Versionnement	Exclure du dépôt les secrets, l'environnement virtuel et les fichiers locaux générés inutilement.	Inspection du .gitignore

Ces exigences représentent des objectifs à atteindre, et non des performances déjà mesurées.

L'exigence ENF-05 est particulièrement pertinente pour notre projet. Dans ton cours de la semaine 5, la maintenabilité est associée à cinq caractéristiques : modularité, réutilisabilité, analysabilité, modifiabilité et testabilité. semaine-5.pdf


C'est directement lié au conseil du recruteur concernant la qualité de la structure d'un projet GitHub.
8. Périmètre du produit

 Inclus dans le MVP
- Importation CSV
- Nettoyage des données
- Validation des données
- Base SQLite
- Calcul des indicateurs
- Tableau de bord
- Graphiques et filtres
- Tests
- Documentation


 Hors périmètre initial
- Authentification
- Données médicales réelles
- Géolocalisation en temps réel
- Application mobile
- Intelligence artificielle
- Gestion des ambulanciers
- Répartition des ambulances
- Prédiction des urgences



Le MVP (Minimum Viable Product) est la première version suffisamment fonctionnelle pour répondre au besoin essentiel de l'utilisateur.