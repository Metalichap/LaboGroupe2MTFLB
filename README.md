# Mon Petit Projet

* Metalichap - François
* maxdbxl - Maxime
* pehnny - Théo
* TheLO819 - Loïc

## Commit message template
`[user - action - module] description`

`user` correspond à l'identifiant du développeur.

`action` peut prendre les valeur *feature*, *update* et *fix* selon que le contenu du commit est une nouvelle fonctionnalité, une mise à jour ou une correction. Au besoin, d'autres actions peuvent être utilisées à l'appréciation du développeur.

`module` désigne le(s) modèles qui sont concernés.

`description` contient les détails du commit.

**Exemple :** `[dev_b - feature - ticket, user] implémentation des controlleurs à destination du tableau de bord.`

## Dev A : Théo (pehnny)

### Tables
**users**, **roles**, **userroles**, **teams**

### Controleurs
- [user](./app/controllers/user_controller.py)
- [roles](./app/controllers/)
- [userroles](./app/controllers/)
- [teams](./app/controllers/team_controller.py)

### Services
- [x] Attribution des rôles (admin)
- [ ] Création des équipes
- [ ] Affection des membres à une équipe
- [ ] Activation/Désactivation des comptes (admin)

Voir comment implémenter une authorization au niveau des rôles pour créer un droit d'admin et des routes isolées.