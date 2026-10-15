# Ouverture de caisse des journées suivantes

- Projet : Astusoft Sales Manager
- Nature : décision fonctionnelle — découverte métier
- Statut : principes d'ouverture confirmés ; politique des écarts acceptée dans son orientation, paramètres détaillés encore en discussion

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

## Décision ASM-CASH-OPEN-001 — Politique configurable des écarts

**Statut :** orientation métier acceptée le 15 octobre 2026. Les seuils chiffrés et certains traitements d'exception restent à arbitrer.

### Référence de calcul

Le fonds attendu correspond au dernier montant physique validé, augmenté des entrées et diminué des sorties d'espèces enregistrées depuis ce point de référence. Les paiements non réalisés en espèces ne modifient pas ce fonds.

`écart = fonds effectivement compté - fonds attendu`

Un montant attendu inconnu est distinct d'un fonds attendu de zéro. L'ouverture enregistre toujours le montant réellement compté, sans le remplacer par le montant théorique. Les écarts négatifs et positifs restent historisés.

### Configuration des contrôles

- L'organisation définit une politique de référence et des limites d'autorisation.
- Chaque point de vente peut choisir une politique dans les limites autorisées par l'organisation.
- Chaque caisse peut recevoir une dérogation explicite à la politique du point de vente, dans les limites autorisées par l'organisation.
- En l'absence de dérogation, la configuration du niveau supérieur s'applique. La politique effective et sa version sont conservées au moment de chaque ouverture; un changement ultérieur ne réécrit pas l'historique.
- Le montant absolu de l'écart est comparé à deux seuils configurables, exprimés dans la devise de la caisse : tolérance et seuil critique. Les deux seuils doivent être positifs ou nuls, et le seuil critique ne peut être inférieur à la tolérance.
- Aucun montant de seuil chiffré n'a été accepté comme valeur par défaut. Tout exemple chiffré est indicatif.

### Classification

| Situation | Classification |
| --- | --- |
| Écart égal à zéro | Aucun écart |
| Écart non nul et valeur absolue inférieure ou égale à la tolérance | Mineur |
| Valeur absolue supérieure à la tolérance et inférieure ou égale au seuil critique | Significatif |
| Valeur absolue supérieure au seuil critique | Critique |

La classification ne définit pas à elle seule le blocage : chaque niveau possède une action configurée dans les limites de la politique d'organisation. Les actions envisagées sont consignation seule, justification obligatoire, notification, et approbation avant ouverture. L'absence de fonds attendu fiable doit être traitée explicitement, sans fabriquer un écart nul.

### Habilitations et responsabilités

- Le vendeur habilité déclare et confirme son fonds réel et peut justifier l'écart.
- Le gérant ou responsable habilité consulte les écarts des caisses dont il a la charge et peut approuver ceux soumis à validation.
- L'administrateur habilité configure les politiques; cette faculté n'implique pas automatiquement le droit d'approuver ses propres écarts.
- Un vendeur ne peut pas approuver son propre écart par défaut. Une exception explicite peut être prévue pour un propriétaire exploitant seul, mais ses modalités restent à valider.
- Les déclarations, justifications, décisions, auteurs, horodatages et versions de politique sont conservés sans réécriture des faits validés.
- Le vendeur entrant reconnaît ce qu'il reçoit et n'est pas automatiquement tenu responsable des écarts antérieurs.

### Notifications et indisponibilité

- Les écarts mineurs sont journalisés; le déclenchement de notifications reste configurable.
- Les écarts significatifs peuvent déclencher une notification au responsable; selon la politique, l'ouverture peut rester autorisée.
- Les écarts critiques peuvent imposer une approbation préalable. En pareil cas, l'absence d'approbation ne vaut jamais autorisation.
- La notification intégrée est le canal de référence envisagé; les canaux externes restent optionnels.
- Une défaillance de notification ne doit pas contourner un contrôle obligatoire. L'envoi peut être repris de manière fiable sans multiplier les notifications.
- La délégation, l'escalade et les exceptions en cas d'indisponibilité du gérant restent à arbitrer avant implémentation.

### Critères d'acceptation additionnels

1. Un retrait enregistré entre deux sessions diminue le montant attendu, sans créer artificiellement un écart.
2. Un écart positif et un écart négatif de même amplitude reçoivent la même classe, mais conservent leur signe.
3. Une somme attendue inconnue n'est jamais présentée comme zéro.
4. Une valeur réellement comptée différente du montant attendu est conservée telle quelle.
5. Une caisse sans dérogation hérite de la configuration applicable du point de vente; une dérogation ne dépasse pas les limites de l'organisation.
6. Une modification ultérieure des seuils ne modifie pas la classification et la décision historiques.
7. Un vendeur ordinaire ne peut pas approuver son propre écart soumis à validation.
8. Lorsqu'une approbation préalable est requise, les encaissements restent impossibles avant une décision autorisée.
9. Une notification en échec ne supprime ni l'écart ni la demande d'approbation.
10. Une relève conserve séparément les montants remis et reçus et les identités des deux personnes.
