# Astusoft Sales Manager

Astusoft Sales Manager est un projet de plateforme de gestion commerciale destiné à accompagner les activités quotidiennes des entreprises et de leurs points de vente.

Le projet est actuellement en phase de cadrage. Son périmètre fonctionnel, son modèle métier et son architecture technique seront définis progressivement à partir d'une démarche de découverte et de modélisation Domain-Driven Design (DDD).

## Objectifs du projet

- Comprendre et formaliser les besoins des utilisateurs.
- Concevoir un modèle métier explicite et cohérent.
- Construire une application maintenable, testable et évolutive.
- Garantir la traçabilité des décisions fonctionnelles et techniques.
- Permettre la reprise du développement après une interruption prolongée.

## Principes de développement

Le projet adopte les principes suivants :

1. **Le métier avant la technologie** : comprendre le domaine avant de sélectionner les solutions techniques.
2. **Documentation versionnée** : conserver dans Git les exigences, décisions et plans de livraison.
3. **Implémentation incrémentale** : développer des unités de travail limitées, vérifiables et traçables.
4. **Qualité continue** : définir des critères d'acceptation et vérifier chaque livraison.
5. **Reprise autonome** : maintenir dans le dépôt les informations nécessaires pour poursuivre le développement sans dépendre des conversations précédentes.

## État du projet

**Phase actuelle :** Fondations documentaires (LOT-00) en cours et découverte métier engagée.

Les premières décisions relatives aux caisses, aux sessions individuelles et à l'ouverture quotidienne sont documentées. Elles ne constituent pas une implémentation applicative. Aucune architecture technique n'a encore été acceptée.

Consulter [PROJECT_STATE.md](PROJECT_STATE.md) pour la reprise du travail et [l'ouverture quotidienne de caisse](docs/02-domain/discovery/CASH_SESSION_DAILY_OPENING.md) pour les règles métier concernées.

## Organisation du dépôt

Le dépôt comporte déjà les documents de gouvernance, de vision produit, de découverte métier et les enregistrements de livraison LOT/EPIC/TASK. Des outils de validation documentaire et leurs tests sont présents ; leur validation opérationnelle reste à établir par des vérifications exécutées.

## Contribution

Les conventions de contribution, le workflow de développement, les règles de documentation et les procédures de validation seront établis avant le démarrage de l'implémentation métier.

## Licence

Le régime de licence du projet reste à définir.
