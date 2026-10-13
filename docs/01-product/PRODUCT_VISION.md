# Astusoft Sales Manager — Vision produit

**Version :** 0.1  
**Statut :** Proposition de cadrage  
**Responsable :** Porteur du projet

## 1. Présentation

Astusoft Sales Manager est un projet de plateforme de gestion commerciale destiné à accompagner les entreprises dans leurs opérations quotidiennes de vente.

La plateforme vise principalement les commerces de détail qui commercialisent des produits variés : alimentation générale, articles ménagers, habillement, quincaillerie, produits cosmétiques et autres catégories de marchandises.

Elle doit permettre aux commerçants de mieux organiser leurs activités, de suivre leurs opérations et de disposer d'informations fiables pour prendre leurs décisions.

Le produit est envisagé comme une solution simple à utiliser, adaptée aux contraintes des commerces ciblés et capable d'évoluer avec leur activité.

## 2. Problème à résoudre

Dans de nombreux commerces, les opérations quotidiennes reposent encore sur des cahiers, des calculs manuels, des fichiers isolés ou des pratiques informelles.

Cette organisation peut entraîner plusieurs difficultés :

- Difficulté à connaître précisément les ventes réalisées.
- Manque de visibilité sur les recettes quotidiennes.
- Erreurs dans les calculs et les enregistrements.
- Difficulté à contrôler les opérations des employés.
- Absence d'historique fiable des transactions.
- Suivi des marchandises parfois approximatif.
- Difficulté à comparer les performances entre plusieurs points de vente.
- Perte de temps lors de la préparation des bilans.

Ces difficultés constituent des hypothèses de découverte métier. Leur fréquence et leur importance devront être vérifiées auprès des utilisateurs ciblés.

## 3. Vision

Permettre aux commerçants de piloter leurs activités commerciales avec davantage de simplicité, de transparence et de maîtrise, grâce à un outil accessible et adapté à leur environnement.

Astusoft Sales Manager doit devenir un outil de travail quotidien, et non uniquement un logiciel utilisé pour produire des rapports.

## 4. Utilisateurs ciblés

### 4.1. Propriétaire ou responsable d'entreprise

Personne chargée de superviser l'activité commerciale.

Besoins supposés :

- Consulter les performances des ventes.
- Contrôler les opérations réalisées.
- Suivre plusieurs points de vente.
- Comprendre les résultats de son activité.
- Identifier les anomalies nécessitant son attention.

### 4.2. Responsable de point de vente

Personne chargée de l'organisation quotidienne d'un établissement.

Besoins supposés :

- Superviser les opérations.
- Consulter les ventes de son établissement.
- Organiser le travail des employés.
- Signaler et résoudre les incidents opérationnels.

### 4.3. Caissier ou vendeur

Personne chargée de réaliser les ventes auprès des clients.

Besoins supposés :

- Retrouver rapidement les produits.
- Enregistrer les articles vendus.
- Calculer le montant à payer.
- Enregistrer les paiements.
- Finaliser les transactions avec peu de manipulations.

### 4.4. Gestionnaire des marchandises

Personne chargée du suivi des produits et des mouvements de marchandises.

Besoins supposés :

- Organiser le catalogue.
- Consulter les quantités disponibles lorsqu'elles sont suivies.
- Enregistrer les opérations affectant les stocks.
- Identifier les écarts.

Ces profils représentent des responsabilités métier potentielles.

Ils ne constituent pas encore une définition définitive des rôles et permissions de l'application.

## 5. Proposition de valeur

Astusoft Sales Manager cherche à apporter cinq bénéfices principaux.

### 5.1. Simplicité opérationnelle

Faciliter les opérations commerciales courantes sans imposer des procédures inutilement complexes.

### 5.2. Fiabilité des informations

Conserver un historique cohérent des opérations permettant de retrouver leur origine et leur résultat.

### 5.3. Visibilité sur l'activité

Donner aux responsables une meilleure compréhension des ventes et de l'évolution de leur activité.

### 5.4. Contrôle des opérations

Permettre d'identifier les personnes responsables des opérations et de détecter certaines anomalies.

### 5.5. Adaptation au contexte local

Prendre en compte les pratiques des commerces ciblés, leur organisation et leurs contraintes économiques et techniques.

## 6. Hypothèses structurantes

Les hypothèses suivantes orientent la découverte sans constituer des décisions définitives.

**HYP-001 — Organisations commerciales**

Une entreprise peut exploiter un ou plusieurs points de vente.

**HYP-002 — Catalogue de produits**

Un commerce peut vendre différents types de produits nécessitant des informations variables.

**HYP-003 — Identification des produits**

Tous les articles ne disposent pas nécessairement d'un code-barres.

**HYP-004 — Gestion des stocks**

Certains commerces souhaitent suivre précisément leurs quantités, tandis que d'autres privilégient principalement l'enregistrement des ventes.

**HYP-005 — Organisation du travail**

Plusieurs personnes peuvent intervenir dans les ventes, l'encaissement et la supervision.

**HYP-006 — Connectivité**

La qualité de la connexion Internet peut varier selon les lieux d'exploitation.

**HYP-007 — Moyens de paiement**

Les pratiques d'encaissement peuvent comprendre plusieurs modes de paiement, à étudier pendant la découverte métier.

Chaque hypothèse devra être confirmée, nuancée ou rejetée.

## 7. Capacités fonctionnelles envisagées

Les capacités suivantes constituent des pistes de travail.

| Domaine fonctionnel | Capacité envisagée                                |
| ------------------- | ------------------------------------------------- |
| Organisation        | Gestion des entreprises et points de vente        |
| Catalogue           | Enregistrement et consultation des produits       |
| Vente               | Création et finalisation des ventes               |
| Encaissement        | Enregistrement des paiements                      |
| Caisse              | Suivi des opérations de caisse                    |
| Stock               | Suivi facultatif ou configurable des marchandises |
| Personnel           | Gestion des utilisateurs et responsabilités       |
| Reporting           | Consultation des ventes et indicateurs            |

Ce tableau ne constitue ni le périmètre confirmé du MVP ni une cartographie DDD.

Les frontières métier seront étudiées séparément.

## 8. Principes d'expérience utilisateur

La plateforme devrait respecter les principes suivants :

1. Réduire le nombre d'actions nécessaires aux opérations fréquentes.
2. Utiliser une terminologie compréhensible par les utilisateurs.
3. Éviter de rendre obligatoires les informations qui ne sont pas toujours disponibles.
4. Afficher clairement les erreurs et les actions possibles.
5. Préserver la traçabilité des opérations sensibles.
6. Tenir compte des équipements utilisés dans les commerces.
7. Éviter de sacrifier la fiabilité pour la rapidité apparente.

## 9. Périmètre initial

Le périmètre exact de la première version reste à définir.

La découverte devra notamment déterminer :

- Le parcours minimal de vente.
- Les informations nécessaires pour enregistrer un produit.
- Les règles d'encaissement.
- Les responsabilités des utilisateurs.
- Les besoins réels de suivi des stocks.
- Les informations nécessaires à la supervision.
- Les contraintes de connectivité.

Les fonctionnalités seront priorisées en fonction de leur valeur métier, de leur complexité et des dépendances identifiées.

## 10. Hors périmètre actuel de conception

À ce stade, aucune décision n'est prise concernant :

- Le framework applicatif.
- Le langage de programmation.
- Le système de base de données.
- L'architecture de déploiement.
- Le découpage en bounded contexts.
- Les agrégats DDD.
- Les intégrations avec des services externes.

Ces choix seront faits lorsque les besoins concernés seront suffisamment compris.

## 11. Critères de réussite du produit

Les critères mesurables seront définis après découverte.

Les dimensions à étudier comprennent :

- Temps nécessaire pour réaliser une vente courante.
- Facilité de prise en main.
- Fiabilité des enregistrements.
- Capacité à retrouver une transaction.
- Visibilité sur les recettes et les ventes.
- Facilité de supervision.
- Satisfaction des utilisateurs.
- Coût d'adoption pour les commerces ciblés.

Aucun objectif chiffré n'est encore validé.

## 12. Questions ouvertes

1. Quel segment de commerces doit être ciblé en priorité ?
2. Une vente est-elle toujours liée à un point de vente physique ?
3. Une vente peut-elle être enregistrée sans suivi des stocks ?
4. Quels moyens de paiement doivent être pris en charge dès la première version ?
5. Quelle autonomie est nécessaire en l'absence de connexion Internet ?
6. Quelle est l'organisation réelle des caisses et des vendeurs ?
7. Quelles informations sont indispensables au propriétaire ?
8. Quelles fonctionnalités sont essentielles pour le premier déploiement ?

## 13. Prochaine étape

Commencer la découverte métier par le processus de vente.

Objectif :

Décrire précisément comment une vente se déroule dans
un commerce ciblé, depuis la sélection des produits
jusqu'à sa finalisation et son encaissement.

Identifier :

- Les acteurs.
- Les événements métier.
- Les règles.
- Les exceptions.
- Les informations manipulées.
- Les questions nécessitant une validation terrain.

Ne pas définir d'agrégats ou de bounded contexts avant
d'avoir compris les processus métier.
