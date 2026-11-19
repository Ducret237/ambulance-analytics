11. Rédaction des User Stories
Un récit utilisateur décrit un besoin du point de vue de la personne qui utilisera le produit.

Product Backlog initial

| ID    | Récit utilisateur                                                                                                               | Exigences | Points |
| :---- | :------------------------------------------------------------------------------------------------------------------------------ | :-------: | :----: |
| US-01 | En tant que responsable des données, je veux importer un fichier CSV afin d'exploiter les données d'interventions.              |   EF-01   |   3    |
| US-02 | En tant que responsable des données, je veux détecter les interventions invalides afin de garantir la qualité des données.      |   EF-02   |   5    |
| US-03 | En tant que responsable des données, je veux éliminer les doublons et normaliser les valeurs afin d'éviter les incohérences.    |   EF-03   |   3    |
| US-04 | En tant que gestionnaire, je veux consulter la liste des interventions valides afin de connaître l'activité enregistrée.        |   EF-05   |   2    |
| US-05 | En tant que responsable des données, je veux conserver les interventions afin de les retrouver après la fermeture de l'application. |   EF-04   |   5    |
| US-06 | En tant que responsable des données, je veux consulter un rapport d'importation afin d'identifier les anomalies.                |   EF-10   |   3    |
| US-07 | En tant que gestionnaire, je veux connaître les délais d'intervention afin d'analyser les temps de réponse.                     |   EF-06   |   3    |
| US-08 | En tant que gestionnaire, je veux consulter les indicateurs globaux afin d'obtenir une synthèse de l'activité.                  |   EF-07   |   3    |
| US-09 | En tant qu'analyste, je veux visualiser les statistiques sous forme de graphiques afin de comparer les régions et les périodes. |   EF-08   |   5    |
| US-10 | En tant qu'analyste, je veux filtrer les interventions afin de réaliser des analyses ciblées.                                   |   EF-09   |   5    |
| US-11 | En tant qu'analyste, je veux exporter les résultats filtrés afin de pouvoir les exploiter dans un autre outil.                  |   EF-11   |   3    |


Toutes ces User Stories sont initialement à l'état À faire.

Les estimations sont proposées selon l'échelle relative de Fibonacci : 1, 2, 3, 5, 8. Elles expriment l'effort, la complexité et l'incertitude, et non des heures de travail.

12. Critères d'acceptation

Les critères d'acceptation nous permettront de savoir objectivement si une fonctionnalité répond au besoin.
User Story	Critères d'acceptation

US-01	CA-01 : un fichier CSV valide est lu correctement. CA-02 : un fichier inexistant ou dépourvu d'une colonne obligatoire est refusé avec un message explicite.
US-02	CA-01 : une intervention dont tous les champs respectent les règles est acceptée. CA-02 : une arrivée antérieure à l'appel entraîne le rejet de la ligne. CA-03 : une valeur obligatoire manquante est signalée.
US-03	CA-01 : deux lignes identiques ne produisent qu'une intervention. CA-02 : les espaces inutiles sont supprimés. CA-03 : les doublons contradictoires sont signalés.
US-04	CA-01 : toutes les interventions valides disponibles sont affichées ; après intégration de US-05, elles proviennent de SQLite. CA-02 : la liste vide produit un message explicite.
US-05	CA-01 : les interventions sont conservées après redémarrage. CA-02 : réimporter un fichier identique ne crée aucun doublon.
US-06	CA-01 : les nombres de lignes importées, rejetées et ignorées sont affichés. CA-02 : les motifs de rejet sont accessibles.
US-07	CA-01 : un appel à 10 h et une arrivée à 10 h 12 donnent 12 minutes. CA-02 : un délai négatif est refusé.
US-08	CA-01 : les trois indicateurs correspondent aux données valides sélectionnées. CA-02 : l'absence de données affiche zéro intervention et des délais et pourcentages non disponibles.
US-09	CA-01 : les graphiques présentent les statistiques par région et par période. CA-02 : les valeurs représentées correspondent aux données analysées.
US-10	CA-01 : sélectionner Outaouais affiche uniquement les interventions de cette région. CA-02 : plusieurs filtres peuvent être combinés. CA-03 : les indicateurs et graphiques sont recalculés.
US-11	CA-01 : le fichier exporté contient uniquement les résultats filtrés. CA-02 : le fichier CSV peut être ouvert et lu correctement.

13. Planification des itérations

1. Itération 1 — Importer et consulter les interventions
   
   US-01, US-02, US-03, US-04.
   
   Livrable : un programme Python en console permettant de lire un fichier CSV, de contrôler les données et d'afficher les interventions valides. Dans cette version, elles restent en mémoire.
2. Itération 2 — Conserver les données
   
   US-05, US-06.
   
   Livrable : une application capable d'enregistrer les données dans SQLite, de les retrouver et de produire un rapport d'importation.
3. Itération 3 — Analyser les interventions
   
   US-07, US-08.
   
   Livrable : un programme capable de calculer et d'afficher les principaux indicateurs.
4. Itération 4 — Visualiser les résultats
   
   US-09, US-10.
   
   Livrable : un tableau de bord Streamlit interactif avec graphiques et filtres.
5. Itération 5 — Exportation et amélioration
   
   US-11, améliorations et corrections.
   
   Livrable : une application documentée et reproductible permettant également d'exporter les résultats.

Les tests, la documentation et les commits seront réalisés durant chaque itération, et non uniquement à la fin.