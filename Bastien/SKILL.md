---
name: github-release-report
description: Transforme le modèle de données JSON d'une release GitHub (changelog, stats de code, breaking changes, dépendances, artefacts, stats de build, stats de PR) en un rapport HTML autonome et consultable hors-ligne. Utiliser cette skill dès qu'un rapport de comparaison entre deux releases GitHub doit être produit au format HTML — que ce soit à la demande explicite d'un rapport de release, ou en fin de pipeline de l'agent Release Report une fois le modèle de données assemblé. Toujours consulter cette skill avant d'écrire du HTML "à la main" pour ce type de rapport : elle fixe l'identité visuelle, la structure des sections et les conventions de gabarit à respecter.
---

# Rendu HTML du rapport de release

Cette skill ne collecte aucune donnée elle-même (c'est le rôle de l'agent Release Report et de ses outils MCP GitHub) : elle prend en entrée un modèle de données déjà assemblé et produit le fichier HTML final.

## 1. Contrat de données en entrée

Le modèle de données attendu est celui défini dans le prompt de l'agent Release Report :

```json
{
  "repo": "owner/name",
  "release_current": { "tag": "", "published_at": "", "url": "" },
  "release_previous": { "tag": "", "published_at": "", "url": "" },
  "changelog": [{ "type": "feature|fix|breaking|chore|other", "title": "", "ref": "", "url": "" }],
  "code_stats": { "files_changed": 0, "additions": 0, "deletions": 0, "by_component": [{ "component": "", "additions": 0, "deletions": 0 }] },
  "breaking_changes": [{ "description": "", "source": "", "migration_note": "" }],
  "dependencies": [{ "package": "", "ecosystem": "", "from": "", "to": "" }],
  "artifacts": [{ "name": "", "url": "", "release": "current|previous" }],
  "build_stats": { "total_runs": 0, "success": 0, "failed": 0, "success_rate": 0.0, "avg_duration_sec": 0 },
  "pr_stats": {
    "prs": [{ "number": 0, "title": "", "author": "", "created_at": "", "approved_at": "", "merged_at": "", "lead_time_to_approval_hours": 0.0, "agent_assisted": false }],
    "avg_lead_time_to_approval_hours": 0.0,
    "median_lead_time_to_approval_hours": 0.0,
    "pct_agent_assisted": 0.0
  },
  "assumptions": ["..."]
}
```

Si un champ est manquant ou non disponible, ne jamais laisser un placeholder brut ou inventer une valeur : afficher un texte explicite ("non disponible") ou supprimer la section concernée (voir section 4).

## 2. Gabarit à utiliser

Lire et partir de **`assets/template.html`** — ne pas réécrire le HTML/CSS depuis zéro. Ce gabarit encode déjà l'identité visuelle du rapport :

- **Palette fonctionnelle** : vert (`--added`) = ajouts/succès, rouille (`--removed`) = suppressions/échecs, ambre (`--flag`) = breaking changes. Ces couleurs ne doivent jamais être réutilisées pour autre chose.
- **Typographie à trois rôles** : serif système pour les titres (ton "rapport"), sans-serif système pour le corps, monospace système pour tout ce qui est littéralement une donnée (tag, SHA, chemin de fichier, durée, numéro de PR). Uniquement des polices système — le fichier doit rester autonome, sans dépendance externe (pas de CDN de polices).
- **Hero en frise temporelle** : les deux releases sont représentées comme deux points reliés par un trait, ce qui matérialise l'intervalle réellement analysé. Ne pas remplacer ce hero par des cartes ou bannières génériques.
- **Bandeau de synthèse** : chiffres nus avec libellé, séparés par des filets fins — pas de cartes à coins arrondis ni d'ombres.

## 3. Convention de substitution

Le gabarit utilise deux mécanismes :

- **Placeholders simples** : `{{NOM_CHAMP}}` → remplacer directement par la valeur du modèle de données (voir table de correspondance ci-dessous).
- **Blocs répétables** : `<!-- REPEAT:NOM --> ... <!-- END:NOM -->` → dupliquer le contenu entre les deux marqueurs une fois par élément de la liste correspondante, en substituant les placeholders internes à chaque itération, puis supprimer les marqueurs de commentaire dans le rendu final.

Table de correspondance (placeholders → champs du modèle) :

| Placeholder | Champ |
|---|---|
| `REPO`, `GENERATED_AT` | `repo`, horodatage de génération |
| `RELEASE_PREVIOUS_TAG/DATE`, `RELEASE_CURRENT_TAG/DATE` | `release_previous`, `release_current` |
| `CODE_ADDITIONS`, `CODE_DELETIONS`, `FILES_CHANGED` | `code_stats.additions/deletions/files_changed` |
| `BREAKING_COUNT` | longueur de `breaking_changes` |
| `BUILD_SUCCESS_RATE`, `PCT_AGENT_ASSISTED` | `build_stats.success_rate`, `pr_stats.pct_agent_assisted` |
| Bloc `CHANGELOG_ITEM` (`ITEM_TITLE/URL/REF`) | éléments de `changelog`, filtrés par `type` pour chaque sous-groupe |
| Bloc `COMPONENT_ROW` | éléments de `code_stats.by_component` |
| Bloc `BREAKING_ITEM` | éléments de `breaking_changes` |
| Bloc `DEPENDENCY_ROW` | éléments de `dependencies` |
| Bloc `ARTIFACT_ITEM` | éléments de `artifacts` |
| `BUILD_TOTAL_RUNS/SUCCESS/FAILED/AVG_DURATION`, `BUILD_FAILED_RATE` (= 100 − success_rate) | `build_stats.*` |
| `PR_MEDIAN_LEAD_TIME`, `PR_AVG_LEAD_TIME` | `pr_stats.median_lead_time_to_approval_hours/avg_lead_time_to_approval_hours` |
| Bloc `PR_ROW` (`PR_NUMBER/TITLE/AUTHOR/LEAD_TIME/AGENT_ASSISTED`, `PR_URL`) | éléments de `pr_stats.prs` — construire `PR_URL` comme `https://github.com/{repo}/pull/{number}` ; afficher `PR_AGENT_ASSISTED` comme "Oui"/"Non" |
| Bloc `ASSUMPTION_ITEM` | éléments de `assumptions` |

## 4. Cas particuliers

- **Liste vide** (ex : aucun breaking change, aucune dépendance modifiée) : supprimer le bloc `REPEAT`/`END` correspondant et le remplacer par le message de repli déjà indiqué en commentaire dans le gabarit (classe `empty-note`), jamais par un tableau ou une liste vide.
- **Première release du dépôt** (pas de release précédente) : remplacer le point "previous" de la frise par une mention explicite ("premier historique") et désactiver les sections qui supposent une comparaison (dépendances, breaking changes) au profit d'un message expliquant l'absence de référence.
- **Donnée non disponible via MCP** : ne jamais laisser `{{...}}` non résolu dans le HTML final ; écrire "non disponible" à la place de la valeur, sans supprimer le libellé qui l'accompagne.

## 5. Checklist avant de livrer le fichier

- Aucun `{{...}}` ni marqueur `REPEAT`/`END` ne subsiste dans le HTML final.
- Le fichier est autonome : CSS entièrement inline dans `<style>`, aucune requête réseau (pas de CDN, pas de police externe, pas de script).
- Tous les liens (`href`) pointent vers de vraies URL récupérées via MCP — jamais de lien inventé.
- Le fichier s'ouvre correctement en local (double-clic / `file://`) et reste lisible sur mobile (le gabarit inclut déjà une règle `@media` pour les petits écrans).
