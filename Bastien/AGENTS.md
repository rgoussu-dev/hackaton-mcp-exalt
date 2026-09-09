# AGENTS.md

> Ce fichier définit les conventions du dépôt à destination des agents IA (Claude, Copilot, Codex, Cursor, etc.), y compris l'agent **Release Report** qui génère le rapport de comparaison entre deux releases (voir `agent-github-release-report.md`).

## 1. Aperçu du projet
- Dépôt : `<owner>/<repo>`
- Description : `<une phrase décrivant le projet>`
- Stack principale : `<ex: TypeScript + Node.js, ou Python>`
- Branche principale : `main`

## 2. Commandes (setup, build, test)

| Action | Commande |
|---|---|
| Installer les dépendances | `<ex: npm ci>` |
| Lancer les tests | `<ex: npm test>` |
| Build | `<ex: npm run build>` |
| Lint | `<ex: npm run lint>` |

## 3. Convention de commits / PR

- Les commits suivent la convention **Conventional Commits** (`feat:`, `fix:`, `chore:`, `refactor:`, etc.).
- Un breaking change **doit** être signalé par l'une de ces deux formes :
  - un `!` après le type/scope : `feat(api)!: ...`
  - un footer `BREAKING CHANGE: <description>` dans le corps du commit
- Toute PR introduisant un breaking change doit porter le label `breaking-change`.

> Utilisé par l'agent Release Report (heuristique 5.1) pour détecter les breaking changes — cette définition prime sur l'heuristique par défaut.

## 4. Mapping des composants

Utilisé par l'agent Release Report pour ventiler les stats de code par composant (heuristique 5.4).

| Composant | Chemin(s) |
|---|---|
| API | `src/api/**` |
| UI | `src/ui/**`, `apps/web/**` |
| Core / domaine | `src/core/**` |
| Infra / CI | `.github/**`, `infra/**` |
| Documentation | `docs/**` |

> Adapter cette table à l'arborescence réelle du dépôt. Tout fichier non couvert est classé dans « Autres ».

## 5. Comptes bots / agents connus

Utilisé par l'agent Release Report pour calculer le pourcentage de PR assistées par un agent (heuristique 5.2).

| Compte / signature | Type |
|---|---|
| `dependabot[bot]` | Mise à jour de dépendances |
| `github-actions[bot]` | Automatisation CI |
| `<nom-bot-interne>[bot]` | `<à préciser>` |
| Trailer `Co-authored-by: Claude <...>` | Assistance Claude Code |

> Compléter avec les comptes d'automatisation propres à l'organisation. Un compte absent de cette liste n'est pas ignoré : les heuristiques par défaut du prompt de l'agent continuent de s'appliquer en complément.

## 6. Fichiers de dépendances surveillés

Par défaut, l'agent surveille les manifestes standards (`package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, etc. — voir section 5.3 du prompt de l'agent). Ajouter ici tout gestionnaire non standard utilisé par ce dépôt :
- `<ex: deps.edn pour Clojure — à ajouter si applicable>`

## 7. Politique de releases

- Les pré-releases (`-rc`, `-beta`, `-alpha`) sont **exclues par défaut** de la comparaison N / N-1.
- `<préciser ici si les pré-releases doivent être incluses, ou toute règle spécifique de tagging/versioning>`

## 8. Workflows CI pertinents pour les stats de build

Utilisé par l'agent Release Report pour les stats de build (succès/échec/durée moyenne).

| Workflow | Fichier | Pertinent pour |
|---|---|---|
| CI principal | `.github/workflows/<ci.yml>` | Build & tests |
| Release | `.github/workflows/<release.yml>` | Publication des artefacts |

> Lister uniquement les workflows à inclure dans les stats ; les autres (ex : workflows de documentation) sont ignorés par défaut.

## 9. Restrictions pour les agents

- Accès **lecture seule** au code source et à l'historique Git.
- Aucun agent ne pousse de commit, ne crée de PR ni ne modifie les réglages du dépôt sans validation humaine explicite.
- Les rapports générés (ex : rapport de release) sont écrits en dehors du dépôt (dossier de sortie local), jamais commités automatiquement.
