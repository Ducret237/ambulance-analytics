Pour la première version, nous aurons six champs obligatoires dans les fichiers CSV.

| Champ               | Type logique  | Exemple                | Obligatoire |
| :------------------ | :------------ | :--------------------- | :---------: |
| `intervention_id`   | Texte         | `INT-0001`             |     Oui     |
| `region`            | Texte         | Outaouais              |     Oui     |
| `intervention_type` | Texte         | Accident               |     Oui     |
| `priority`          | Entier        | `1`                    |     Oui     |
| `call_received_at`  | Date et heure | `2026-11-01T13:00:00Z` |     Oui     |
| `arrival_at`        | Date et heure | `2026-11-01T13:12:00Z` |     Oui     |


Nous ajouterons une donnée calculée, response_time_minutes, correspondant au délai d'intervention.

Les dates seront exprimées en UTC pour simplifier les traitements et éviter les ambiguïtés liées aux changements d'heure. Le filtre par période utilisera également les dates UTC dans la première version.

Valeurs autorisées

| Champ                 | Valeurs retenues pour la simulation   |
| :-------------------- | :------------------------------------ |
| **Région**            | Outaouais, Montréal, Laval, Québec    |
| **Type d'intervention**| Accident, Malaise, Traumatisme, Autre |
| **Priorité 1**        | Élevée                                |
| **Priorité 2**        | Moyenne                               |
| **Priorité 3**        | Faible                                |

Modèle relationnel textuel

REGION(
    region_id PK,
    name UNIQUE
)

INTERVENTION_TYPE(
    type_id PK,
    name UNIQUE
)

INTERVENTION(
    intervention_id PK,
    region_id FK -> REGION.region_id,
    type_id FK -> INTERVENTION_TYPE.type_id,
    priority,
    call_received_at,
    arrival_at
)

Définition des indicateurs de performance (KPI)


| Indicateur                                        | Méthode de calcul                                                                                   |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| **Nombre d'interventions**                        | Nombre d'interventions valides et uniques sélectionnées                                             |
| **Délai d'intervention**                          | Heure d'arrivée moins heure de réception de l'appel                                                 |
| **Délai moyen**                                   | Somme des délais divisée par le nombre d'interventions sélectionnées                                |
| **Pourcentage d'arrivées en 15 minutes ou moins** | Nombre d'interventions respectant le seuil, divisé par le nombre total sélectionné, multiplié par 100 |
| **Interventions par région**                      | Nombre d'interventions regroupées par région                                                        |
| **Interventions par priorité**                    | Nombre d'interventions regroupées par priorité                                                      |
| **Évolution de l'activité**                       | Nombre d'interventions regroupées par période                                                       |
