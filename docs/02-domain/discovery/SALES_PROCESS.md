# Astusoft Sales Manager — Découverte du processus de vente

**Identifiant :** DISC-SALES-001
**Version :** 0.1
**Statut :** Brouillon — hypothèses à valider

## 1. Objectif

Comprendre comment une vente est réalisée dans les
commerces ciblés par Astusoft Sales Manager.

Ce document décrit les pratiques observées ou supposées,
les scénarios possibles, les règles à clarifier et les
questions ouvertes.

Il ne définit pas encore une architecture logicielle.

## 2. Contexte

Le processus étudié concerne prioritairement les petites
boutiques et les commerces de détail de taille moyenne.

### Organisation des petites boutiques

Dans une petite boutique, l'activité quotidienne est
souvent assurée par une seule personne, qui peut être
le propriétaire ou un employé.

Cette personne assure simultanément plusieurs responsabilités :

- Accueillir et conseiller le client.
- Identifier les articles demandés.
- Déterminer les quantités.
- Communiquer les prix.
- Calculer le montant de la vente.
- Recevoir le paiement.
- Remettre les marchandises.

Le vendeur assure donc également l'encaissement.

### Organisation des boutiques de taille moyenne

Dans certaines boutiques de taille moyenne, le vendeur
reste également responsable de l'encaissement.

La présence de plusieurs employés n'implique donc pas
nécessairement une séparation entre la vente et la caisse.

### Conséquence pour le produit

Le processus nominal doit pouvoir être exécuté de bout
en bout par une seule personne.

L'organisation avec un vendeur et un caissier distincts
reste une variante à étudier, et non une obligation du
processus de vente.

Cette observation ne définit pas encore les permissions,
les sessions de caisse ni les contraintes techniques.

## 3. Déclencheur

Le processus commence lorsqu'un client souhaite
acheter un ou plusieurs articles.

Le client peut identifier lui-même les articles
ou demander l'assistance d'un vendeur.

## 4. Scénario nominal proposé

### Étape 1 — Identifier les articles

Le vendeur ou le caissier identifie les articles
que le client souhaite acheter.

Les articles peuvent être retrouvés par une recherche,
une sélection dans un catalogue ou une identification
automatisée lorsque le commerce dispose de l'équipement
nécessaire.

### Étape 2 — Déterminer les quantités

Pour chaque article, la quantité souhaitée est précisée.

Les unités de vente autorisées devront être étudiées :
pièce, paquet, kilogramme, litre ou autre unité.

### Étape 3 — Déterminer les prix

Le prix applicable à chaque article est déterminé.

Il reste à définir :

- Si les prix sont toujours prédéfinis.
- Si un prix peut être modifié pendant une vente.
- Qui peut autoriser une modification.
- Comment les remises sont appliquées.

### Étape 4 — Calculer le montant

Le montant des articles est calculé.

Le total peut éventuellement tenir compte de remises,
de frais ou d'autres éléments à identifier.

### Étape 5 — Confirmer les articles

Le client confirme les articles et le montant demandé.

Il reste à déterminer si cette confirmation constitue
une étape explicite du processus.

### Étape 6 — Encaisser le paiement

Le paiement est reçu et enregistré.

Les modes de paiement et les possibilités de combinaison
de plusieurs modes restent à étudier.

### Étape 7 — Finaliser la vente

La transaction est finalisée selon les conditions
métier applicables.

Il reste à préciser :

- Le moment exact de la finalisation.
- Le lien entre paiement et finalisation.
- Les conséquences d'un paiement incomplet.
- Les modifications encore autorisées.

### Étape 8 — Remettre les articles

Le client reçoit les articles achetés.

La possibilité de retirer les articles ultérieurement
reste à examiner.

### Étape 9 — Conserver une trace

Une trace de l'opération est conservée afin de
permettre sa consultation et son contrôle.

La forme et le contenu de cette trace restent à définir.

## 5. Variantes à explorer

### VAR-SALES-001 — Article sans code-barres

Le vendeur recherche l'article autrement.

### VAR-SALES-002 — Modification des quantités

Le client change la quantité d'un article avant
la finalisation.

### VAR-SALES-003 — Retrait d'un article

Le client renonce à acheter un article déjà sélectionné.

### VAR-SALES-004 — Remise commerciale

Une réduction est demandée ou proposée.

### VAR-SALES-005 — Paiement par plusieurs moyens

Le client souhaite répartir le règlement entre
plusieurs modes de paiement.

### VAR-SALES-006 — Paiement insuffisant

Le montant reçu ne couvre pas le total.

### VAR-SALES-007 — Vente à crédit

Le client reçoit les articles avec un paiement différé.

### VAR-SALES-008 — Article sans suivi de stock

L'article peut être vendu sans que le système
enregistre de quantité disponible.

### VAR-SALES-009 — Interruption de la vente

Le client abandonne ou suspend l'opération avant
sa finalisation.

### VAR-SALES-010 — Absence de connexion

Le réseau devient indisponible pendant une opération.

Toutes ces variantes sont des hypothèses de découverte.

Elles ne sont pas automatiquement incluses dans le MVP.

## 6. Questions de règles métier

### BRQ-SALES-001 — Finalisation

À quel moment une vente est-elle considérée comme
définitivement réalisée ?

### BRQ-SALES-002 — Paiement

Une vente peut-elle être finalisée si son montant
n'a pas été intégralement payé ?

### BRQ-SALES-003 — Modification

Quelles modifications restent possibles après
la finalisation ?

### BRQ-SALES-004 — Prix

Un vendeur peut-il modifier librement le prix
d'un article pendant la vente ?

### BRQ-SALES-005 — Stock

Une vente doit-elle être refusée lorsque la
quantité disponible est insuffisante ?

### BRQ-SALES-006 — Responsabilité

Quelle personne est responsable de la vente :
le vendeur, le caissier ou les deux ?

### BRQ-SALES-007 — Encaissement

Une vente peut-elle être encaissée par plusieurs
personnes ou dans plusieurs sessions de caisse ?

### BRQ-SALES-008 — Traçabilité

Quelles informations doivent être conservées pour
permettre une vérification ultérieure ?

### BR-SALES-009 — Configuration des caisses par point de vente

**Statut :** Orientation fonctionnelle confirmée

**Décision :**
Chaque point de vente peut définir son propre mode de
gestion des caisses dans l'administration.

La configuration d'un point de vente n'impose pas
automatiquement le même fonctionnement aux autres
points de vente de l'organisation.

**Modes envisagés :**

1. Caisse partagée entre plusieurs vendeurs.
2. Caisse individuelle affectée à un vendeur.

**Règles fonctionnelles :**

- Un point de vente possède une configuration de caisse
  qui lui est propre.
- Un vendeur autorisé peut réaliser une vente et encaisser
  le paiement.
- Chaque encaissement doit être attribuable à la personne
  qui l'a effectué.
- Les responsables autorisés doivent pouvoir consulter
  les opérations d'encaissement.
- Le fonctionnement de la caisse respecte le mode
  configuré pour le point de vente.

**Points restant à préciser :**

- Possibilité de modifier le mode après utilisation.
- Affectation et réaffectation des caisses.
- Gestion des sessions d'ouverture et de fermeture.
- Rapprochement entre encaissements enregistrés et
  argent réellement disponible.
- Gestion des opérations en cours lors d'un changement
  de configuration.

**Périmètre :** Point de vente

**Impact potentiel :**
Organisation, vente, encaissement et contrôle de caisse.

Cette décision ne préjuge pas du découpage technique
ou des frontières des bounded contexts.

### BR-SALES-010 — Responsabilité individuelle des sessions de caisse

**Statut :** Décision métier confirmée

**Périmètre :** Point de vente et encaissement

#### Règle principale

Chaque session de caisse est attribuée à un seul
utilisateur identifié.

Un utilisateur ne peut avoir qu'une seule session
de caisse active à la fois.

#### Ouverture de session

- Le vendeur doit utiliser son propre compte.
- Une session est ouverte à son nom.
- La session est associée à un point de vente.
- La caisse concernée est identifiée.
- Le fonds de caisse initial peut être enregistré.

#### Encaissement

- Les opérations sont attribuées au vendeur identifié.
- Les encaissements sont rattachés à sa session active.
- Un autre utilisateur ne peut pas encaisser dans
  cette session.
- Le vendeur reste responsable des opérations
  effectuées sous son compte.

#### Remplacement d'un vendeur

Lorsqu'un vendeur est remplacé :

1. Il termine ses opérations en cours.
2. Il procède au comptage de sa caisse.
3. Il clôture sa session.
4. Son remplaçant se connecte avec son compte.
5. Le remplaçant ouvre une nouvelle session.
6. Les encaissements suivants sont enregistrés
   dans cette nouvelle session.

Une session ne peut pas être transférée d'un
utilisateur à un autre.

#### Clôture

- La session conserve son historique.
- Le montant théorique est calculé.
- Le montant réellement compté est enregistré.
- Les éventuels écarts sont conservés.
- Une session clôturée ne reçoit plus de nouveaux
  encaissements.

#### Cas particuliers à préciser

- Clôture forcée par un responsable.
- Oubli de clôture en fin de journée.
- Panne pendant une session.
- Plusieurs caisses dans un même point de vente.
- Transmission du fonds de caisse au remplaçant.
- Gestion des paiements non effectués en espèces.

## 7. Informations métier potentielles

À étudier lors de la découverte :

- Identité du point de vente.
- Identité de la personne réalisant l'opération.
- Articles vendus.
- Quantités.
- Prix applicables.
- Réductions éventuelles.
- Montant total.
- Paiements reçus.
- Date et heure.
- État de l'opération.
- Références nécessaires à sa consultation.

Cette liste ne constitue pas encore un schéma de données.

## 8. Événements métier candidats

Les événements suivants peuvent aider à comprendre
le processus :

- Vente commencée.
- Article ajouté à la vente.
- Quantité modifiée.
- Article retiré.
- Montant calculé.
- Paiement reçu.
- Vente finalisée.
- Vente abandonnée.

Ces expressions décrivent des faits métier candidats.

Elles ne constituent pas des événements logiciels
déjà approuvés.

## 9. Points à confirmer sur le terrain

- Organisation réelle des vendeurs et caissiers.
- Fréquence des ventes à crédit.
- Pratiques de négociation des prix.
- Utilisation des codes-barres.
- Gestion des produits vendus par quantité variable.
- Moyens d'encaissement courants.
- Gestion des retours et annulations.
- Contraintes de réseau et d'équipement.
- Informations réellement utiles au responsable.

## 10. Décisions non prises

Ce document ne décide pas :

- Du découpage en bounded contexts.
- De l'existence d'un agrégat Sale.
- Des commandes et événements logiciels.
- Du modèle de persistance.
- De l'architecture du POS.
- Des mécanismes techniques de paiement.
- De la stratégie de synchronisation hors ligne.

Ces décisions devront être fondées sur des règles
métier clarifiées.

## 11. Prochaine activité de découverte

Examiner des situations de vente réelles ou
représentatives avec le porteur du projet.

Commencer par confirmer :

1. Qui participe à une vente ?
2. Qui calcule et confirme les prix ?
3. Qui reçoit le paiement ?
4. À quel moment la vente est-elle finalisée ?
5. Que se passe-t-il lorsqu'un client ne paie
   pas entièrement ?
