# Étude de référence — dépôt historique

**Projet cible :** Astusoft Sales Manager
**Source analysée :** https://github.com/johnmabs/zandu-sales-manager
**Révision de lecture :** `74ed387142477ea49657243ed94a6334fb341258` (arbre Git)
**Statut :** matériau d'étude non normatif, à confirmer par découverte métier

## Règles d'utilisation

Le dépôt historique sert de **source d'inspiration et de contre-exemples**, pas de fondation à recopier. Astusoft Sales Manager est un projet indépendant : aucune API, classe, architecture, règle ou statut du dépôt historique n'est accepté automatiquement. Les documents métier d'Astusoft et leurs décisions validées ont priorité.

Chaque proposition issue de cette étude doit préciser : (1) fichier source et révision ; (2) observation technique ou métier ; (3) avantage et limite ; (4) décision Astusoft : retenue / adaptée / écartée / à arbitrer.

## Première lecture factuelle

| Sujet | Source observée dans le dépôt historique | Lecture pour Astusoft |
| --- | --- | --- |
| Vente | `backend/src/Modules/Sales/Domain/Sale.php` | Un agrégat conserve état, lignes, devise, acteur et date d'exploitation. Étudier les invariants avant de choisir un modèle. |
| Session de caisse | `backend/src/Modules/CashManagement/Domain/CashSession/CashSession.php` | Session liée à organisation, magasin, caisse et acteur ; ouverture et clôture enregistrent les montants. Ne prouve pas la gestion du transfert ni l'approbation des écarts d'ouverture. |
| Organisation métier | `backend/src/Modules/CashManagement/README.md`, `README.md` | Découpage par domaines présent dans la source ; **aucune architecture Astusoft décidée**. |
| Parcours POS | `README.md` | Le dépôt mentionne un shell POS de fondation ; ne pas assimiler le backend existant à une expérience de caisse terminée. |

## Écarts à examiner explicitement

- La session de caisse de référence représente un solde d'ouverture et un écart de clôture ; la politique configurable des écarts **à l'ouverture** d'Astusoft requiert une spécification dédiée.
- La clôture avec une valeur comptée n'est pas à elle seule une preuve de transfert de fonds, de réception par une autre personne ou de notification au gérant.
- La présence de `businessDate` dans une vente ne tranche pas le calendrier d'exploitation après minuit.
- Les hypothèses de plateforme, bibliothèques ou frontières de modules de la source ne constituent pas des décisions techniques du nouveau projet.

## Prochain travail d'étude

Inspecter séparément les contrats d'application d'ouverture/fermeture de caisse, les tests de sessions, les cas de vente, les tests d'accès et les flux POS ; compléter cette matrice avec des scénarios négatifs, des règles contradictoires et les questions d'arbitrage. Ne pas marquer ces inspections comme faites avant lecture effective des fichiers.
