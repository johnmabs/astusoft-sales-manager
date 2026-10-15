# Ouverture de caisse des journées suivantes

- Projet : Astusoft Sales Manager
- Nature : décision fonctionnelle — découverte métier
- Statut : proposition consolidée à intégrer dans `docs/02-domain/discovery/SALES_PROCESS.md`

## Objectif

Permettre à une boutique de reprendre ses ventes chaque jour sans répéter inutilement sa configuration, tout en préservant la traçabilité des fonds et la responsabilité individuelle de chaque vendeur.

## Principes

1. Une session de caisse appartient à une seule personne identifiée et à une caisse déterminée.
2. Une nouvelle journée d'exploitation donne lieu à une nouvelle session. Une session de la veille n'est pas prolongée implicitement.
3. La configuration de la boutique et de la caisse persiste d'un jour à l'autre : on ne recommence pas l'intégration initiale.
4. Avant sa première vente de la nouvelle session, le vendeur confirme une seule fois le fonds de caisse effectivement disponible. Il peut modifier le montant proposé.
5. Le montant attendu à l'ouverture peut être proposé à partir de la dernière clôture validée, corrigée des mouvements de fonds enregistrés depuis celle-ci. Il ne devient pas automatiquement le montant déclaré.
6. L'ouverture enregistre l'identité du vendeur, la caisse, la date d'exploitation, l'heure, le fonds déclaré et, si disponible, la référence à la clôture précédente.
7. Un remplacement implique la clôture de la session sortante et l'ouverture d'une session distincte avec le compte du remplaçant. Le fonds transmis est déclaré et le gérant est informé.
8. Une session précédente non clôturée impose une régularisation tracée avant l'ouverture ordinaire d'une nouvelle session sur la même caisse. Aucune clôture silencieuse n'est autorisée.
9. Un écart entre fonds attendu et fonds déclaré est conservé comme fait métier; son traitement (justification, validation, notification) dépend de la configuration et des responsabilités, sans altérer les montants historiques.
10. Une seule session active à la fois pour une caisse physique; l'unicité doit être garantie côté serveur, y compris en cas d'accès simultanés.

## Parcours normal : même personne le lendemain

1. Le vendeur s'authentifie et sélectionne la caisse (ou retrouve la caisse habituelle si le contexte est sans ambiguïté).
2. Le système vérifie qu'aucune session incompatible n'est ouverte pour cette caisse et cette journée.
3. Le système affiche le fonds attendu, lorsqu'il peut être calculé, avec sa provenance.
4. Le vendeur confirme le montant réellement disponible ou le corrige.
5. Le système crée une nouvelle session avec un identifiant propre et enregistre son fonds d'ouverture.
6. Les ventes deviennent possibles; aucun second renseignement du fonds n'est demandé pour cette session.

## Parcours : caisse vide ou fonds non connu

Si aucun fonds précédent n'est disponible, le vendeur renseigne le montant présent, y compris zéro. Une valeur inconnue ne doit pas être assimilée à zéro et une session ne doit pas démarrer avec un montant supposé.

## Parcours : changement de vendeur

1. Le vendeur sortant clôture sa session et procède au comptage prévu par son mode de fonctionnement.
2. Les sommes retirées et le fonds remis au remplaçant sont déclarés séparément.
3. Le remplaçant se connecte avec son propre compte et confirme le fonds réellement reçu.
4. Le système ouvre sa session distincte et informe le gérant de la transmission, selon les canaux configurés.
5. Tout écart entre fonds remis et fonds reçu reste visible et traçable.

## Parcours d'exception : clôture oubliée

Une session restée ouverte au changement de journée bloque une ouverture ordinaire sur la même caisse. Une personne autorisée procède à une clôture tardive ou à une régularisation exceptionnelle, enregistrant l'auteur, l'heure réelle de l'action, la date d'exploitation concernée et un motif si nécessaire. Les données de la session précédente ne sont ni effacées ni silencieusement antidatées.

## Modes d'exploitation

- **Boutique individuelle** : accès rapide à la caisse habituelle; une seule confirmation du fonds à la première vente; le propriétaire-gérant peut remplir lui-même les responsabilités applicables.
- **Équipe et plusieurs caisses** : sélection explicite quand nécessaire, règles d'habilitation, contrôle d'unicité, transmission formelle et notifications au gérant.

Les modes changent la quantité d'interactions et les habilitations, pas la traçabilité fondamentale.

## Critères d'acceptation

- Un vendeur qui revient le lendemain obtient un nouvel identifiant de session.
- Le fonds de la veille n'est jamais accepté sans confirmation.
- Une caisse sans espèces peut être ouverte avec un fonds de 0 FCFA explicitement confirmé.
- Le retrait de fonds à la clôture diminue le montant de référence proposé le lendemain.
- Deux personnes ne peuvent pas ouvrir simultanément la même caisse.
- Une session de la veille non clôturée n'est ni recyclée ni clôturée automatiquement.
- Le remplacement conserve deux sessions distinctes, une trace du fonds transmis et une notification au gérant.
- En boutique individuelle, l'utilisateur ne confirme son fonds qu'une fois pour la session, avant la première vente.

## Points distincts à concevoir ultérieurement

- Les détails du calendrier d'exploitation en cas de vente après minuit.
- Les modalités exactes des notifications et des droits de régularisation.
- La stratégie hors ligne et la prévention des doubles ouvertures lors de synchronisations.

Ces sujets ne modifient pas les principes ci-dessus et ne doivent pas être présentés comme déjà arbitrés.
