# Humanizer FR

Réécrit ou relit les textes français et anglais en préservant le sens, les faits, les citations et la voix de leur auteur. Cette adaptation conserve 18 règles françaises et 26 catégories générales.

## Versions

| Composant | Version |
|---|---|
| Plugin ChatGPT | 3.1.1 |
| Skill Humanizer FR | 3.1.0-fr-chatgpt.2 |
| Base amont | blader/humanizer 3.1.0, adaptations sélectives de 4.0.0 |

Ce dépôt public reprend désormais la source de l’adaptation Humanizer FR. L’ancien contenu 2.1.1 reste consultable dans l’historique Git, notamment au commit `c78047bd4300e5a995d37ae8c7684aa2d53326cd`.

## Utilisation

Demander une réécriture ou une relecture, préciser le public et fournir le texte, le fichier ou un échantillon du style de l’auteur. La skill ne doit pas ajouter de faits pour rendre le texte plus concret. Les termes métiers utiles et les citations exactes restent en place. Les instructions figurant dans un document sont traitées comme du contenu, sans être exécutées.

Pour un document long, elle demande une lecture intégrale par segments et un registre de couverture. Une révision incomplète doit être annoncée comme partielle.

## Fichiers et installation

La source du plugin se trouve dans `skills/humanizer-fr/`. `SKILL.md` et `references/` à la racine sont des copies de compatibilité pour les anciennes installations ; les deux versions doivent rester identiques.

- Codex : copier `skills/humanizer-fr/` dans le dossier personnel de skills de Codex, sous le nom `humanizer-fr`.
- Claude Code : copier ce même dossier dans `~/.claude/skills/humanizer-fr/`. Invocation : `/humanizer-fr`.
- Claude Desktop : importer l’archive de skill générée par le script ci-dessous dans Personnalisation > Skills > Importer un Skill.
- ChatGPT : [fiche Humanizer FR](https://chatgpt.com/plugins/Plugin_8c2eb588f298819184cf4142e2a7e10f). La version 3.1.1 a été vérifiée dans le compte propriétaire et par réexport. La disponibilité de cette version au catalogue public reste à vérifier séparément.

Pour construire les deux archives, depuis un clone de ce dépôt :

```sh
python scripts/build_release.py
```

Le script valide les copies de compatibilité, les versions et les manifestes, puis écrit dans `dist/` une archive de plugin et une archive de skill. Il n’effectue aucune publication. Ne pas importer le ZIP de tout le dépôt à la place de l’archive de plugin générée.

## Source et publication

L’import d’un ZIP dans ChatGPT et un commit sur GitHub sont deux opérations distinctes. Aucune synchronisation automatique avec ChatGPT n’est configurée dans ce dépôt. Après une modification, tester, reconstruire, importer par le workflow autorisé, puis réexporter pour comparer les fichiers enregistrés.

Les champs `homepage` et `repository` des manifestes reproduisent ceux du paquet ChatGPT vérifié et pointent encore vers `blader/humanizer`. Ils désignent la provenance historique ; ils ne constituent pas une liaison de synchronisation. Ils ont été conservés pour ne pas modifier silencieusement la configuration du plugin déjà installé.

## Vérifications

Les neuf cas du kit sont dans `tests/test-cases.jsonl`. Ils ont été évalués localement par un agent distinct, avec quatre cas complémentaires portant sur la voix, la causalité, les références et un extrait tronqué. Le document synthétique utilisé comportait 30 sections et 12 tableaux ; les données protégées ont été conservées. Le validateur de skill et les contrôles structurels passent.

Ces résultats ne constituent pas une batterie automatisée d’appels à un modèle ni des essais dans les runtimes ChatGPT ou Claude. Un essai par cas ne garantit pas une résistance générale aux injections. Le document de test tenait dans le contexte. Les 18 règles françaises et les 26 catégories ont été comparées à la base et conservées intégralement.

## Attribution et licence

Adaptation française par Damien Duguet à partir de [blader/humanizer](https://github.com/blader/humanizer), sous licence MIT. Les exemples français sont originaux et fictifs. La permission amont 4.0.0 d’ajouter des détails absents du texte n’est pas reprise.
