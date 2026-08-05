# File map

<!-- Every file/folder is either explained or parked — no mystery boxes. -->
<!-- known: explained in the learner's own words | parked: honest one-liner for now, deep dive scheduled | generated: machine-made, never edit, always rebuildable -->

## /
- learning/project.md — known (2026-07-30) — your project, MVP, and trunk
- learning/plan.md — known (2026-07-30) — the build plan and locked decisions
- learning/knowledge-graph.md — known (2026-07-30) — the living map of what you actually know
- learning/file-map.md — known (2026-07-30) — this file: why every file in the repo exists
- .git/ — generated (2026-07-30) — git's own tracking data → [[git-source-control]], never edit directly, always rebuildable from history. As of 2026-08-05 it also stores the `origin` remote pointing at github.com/blech0/eisenhower-matrix → [[github-concept]]
- .vs/ — parked (2026-07-30) — Visual Studio's own cache/config folder, machine-generated
- .gitignore — known (2026-08-02) — tells git to never track `.vs/`, `tasks.db`, and (as of 2026-08-05) `__pycache__/` → [[git-source-control]]
- __pycache__/ — generated (2026-08-05) — Python's compiled-bytecode cache, created automatically whenever code runs; untracked and gitignored after being accidentally committed once → [[git-source-control]]
- index.html — known (2026-07-30) — the app's page: 4-quadrant grid with colors, entry controls, and a click handler that creates a new entry and inserts it into the correct quadrant → [[html-structure]], [[css-layout]], [[css-class-selectors]], [[css-color-coding]], [[event-listeners]], [[js-functions]], [[dom-manipulation]]
- app.py — known (2026-08-02) — the Flask server: serves the page at `/`, tasks as JSON at `/api/tasks`, and sets up the SQLite database on startup. As of 2026-08-05, `POST /api/tasks` validates required fields before touching the database → [[what-is-a-server]], [[flask-routes]], [[flask-choice]], [[sql-basics]], [[error-handling]]
- README.md — known (2026-08-05) — the repo's front door on GitHub: what the app is, the live URL, tech stack, features, and how to run it locally → [[readme-portfolio-framing]]
- requirements.txt — known (2026-08-05) — the note you leave for a machine that has never seen your project: the packages it must install before `app.py` will run. Lists both direct dependencies, `Flask==3.1.3` and `gunicorn==26.0.0` (the production server Render will actually run); pip resolves the rest → [[dependency-management]], [[production-vs-dev-server]]
- test_app.py — known (2026-08-05) — automated tests run by `pytest`: a sanity check, a `GET /api/tasks` check, a `POST /api/tasks` check that verifies the task actually persisted and cleans up via `DELETE`, and a check that a malformed POST gets a `400`, not a crash → [[automated-testing]], [[error-handling]]
- tasks.db — generated (2026-08-02) — the actual SQLite database file, created automatically by `app.py`'s `CREATE TABLE IF NOT EXISTS` on startup; never edit directly → [[sql-basics]], [[schema-design]]. Tour check 2026-08-05: guessed "it contains sensitive data" (reasonable instinct, wrong reason) — corrected to: it's excluded because it's generated/rebuildable, not because it's secret
