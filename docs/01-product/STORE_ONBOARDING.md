# Astusoft Sales Manager — Configuration initiale d'un point de vente

**Version :** 0.1
**Statut :** Proposition fonctionnelle

## 1. Objectif

Permettre à un commerçant de configurer rapidement
son point de vente sans devoir maîtriser les concepts
avancés de gestion de caisse.

La configuration doit pouvoir évoluer lorsque
l'activité devient plus importante.

## 2. Principe

Chaque point de vente possède ses propres politiques
opérationnelles.

Lors de sa création, un profil de configuration
peut être choisi afin d'appliquer des paramètres
initiaux adaptés.

Le profil est une aide à la configuration et
ne constitue pas une limitation permanente.

## 3. Profils proposés

### 3.1. Boutique individuelle

Destinée à une boutique tenue par une seule personne.

Comportement initial envisagé :

- Compte utilisateur individuel.
- Possibilité d'ouvrir automatiquement une session.
- Aucune passation entre vendeurs.
- Fonds initial facultatif.
- Suivi des encaissements conservé.
- Clôture simplifiée.

### 3.2. Boutique avec relève

Destinée aux commerces où plusieurs vendeurs
se succèdent.

Comportement initial envisagé :

- Compte personnel pour chaque vendeur.
- Session personnelle obligatoire.
- Fermeture de la session avant remplacement.
- Fonds de caisse transmis explicitement.
- Confirmation du montant reçu par le remplaçant.
- Information du gérant.
- Conservation des écarts éventuels.

### 3.3. Commerce structuré

Destiné aux commerces possédant plusieurs caisses
et une organisation plus complexe.

Comportement initial envisagé :

- Identification des caisses.
- Affectation des utilisateurs autorisés.
- Sessions individuelles.
- Contrôle de l'ouverture et de la clôture.
- Passations enregistrées.
- Supervision des responsables.

## 4. Parcours initial proposé

1. Création de l'organisation.
2. Création du premier point de vente.
3. Choix d'un profil de fonctionnement.
4. Application des paramètres proposés.
5. Présentation d'un récapitulatif.
6. Accès aux opérations courantes.

Les paramètres avancés peuvent être configurés
ultérieurement.

## 5. Règles communes

- Chaque utilisateur utilise son propre compte.
- Une session de caisse appartient à une seule personne.
- Une personne ne possède qu'une session active à la fois.
- Les encaissements sont attribuables à leur auteur.
- Une session clôturée ne reçoit plus de nouveaux paiements.
- Le mode de fonctionnement est configurable
  indépendamment pour chaque point de vente.
- Les opérations passées ne sont pas réécrites lors
  d'un changement de configuration.

## 6. Évolution de la configuration

Un point de vente doit pouvoir modifier ses politiques
opérationnelles sans perdre son historique.

Les effets sur les sessions actives, les caisses et
les utilisateurs doivent être définis avant
l'implémentation de ces changements.

## 7. Questions ouvertes

- Quel profil proposer par défaut ?
- Quelles informations sont obligatoires à l'inscription ?
- Une caisse physique doit-elle être créée automatiquement ?
- Comment démarre une session automatique ?
- Quand demander le premier fonds de caisse ?
- Comment guider un commerçant vers un profil
  plus adapté lorsque son activité grandit ?
- Quelles modifications de politique exigent
  l'absence de session active ?

## 8. Hors périmètre de cette spécification

Ce document ne définit pas :

- Les bounded contexts.
- Les agrégats.
- Les APIs.
- Le schéma de base de données.
- Les permissions techniques.
- L'architecture de synchronisation.
