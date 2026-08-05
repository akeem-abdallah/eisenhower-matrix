# Project: Eisenhower Matrix (tasks + habits)

## About me
- Studying B.Sc. Computer Science at AURAK
- Background in DSA (A-level CS, currently working through NeetCode 150)
- Used a terminal before but mostly by pasting fix commands, not driving it directly
- Goal: become an AI/ML engineer; currently pursuing AI consulting work
- 32 days until next semester starts — this is the time budget for the MVP

## The idea
An Eisenhower matrix app where both **tasks and habits** can live in the four quadrants — something existing apps (e.g. "Eva") don't allow. Long-term vision is a full study/work productivity suite, but that's explicitly out of scope for now.

## MVP
### In
- Add an entry (task or habit) into any of the 4 quadrants
- Mark an entry complete
- 4-quadrant view with color coding
- Single user, no login/accounts

### Parking lot (v2+)
- Dark/light mode toggle, deeper visual polish
- Habit-specific logic (streaks, recurring frequency, bad-habit tracking)
- Accounts, friends, groups
- App/screen-time blocking (Screenzen-style)
- AI assistant
- Focus mode — solo and group (Focus To-Do-style)
- Flashcards with spaced repetition (Anki-style)

## The trunk — core components
### Source control (git)
The save-and-undo system professionals use. Every change gets a checkpoint you can go back to. In from day one.

### Frontend
What you see and click: the four quadrants, entries inside them, the "mark complete" button. Runs in the browser.

### Backend
Sits between the frontend and the data. Decides what's allowed to happen and does the actual work. Whether this is a traditional server or a lighter approach is an open design decision for `/plan-journey`.

### Database
Where tasks and habits actually persist. Without some form of this, refreshing the page loses everything.

### API
The "language" the frontend and backend use to talk to each other.

### Local dev environment
How the app runs on your own machine while building, before it's live for anyone else.

### Deployment
How it goes from running on your laptop to a real URL live on the internet.

## Notes
- **Portfolio/career strategy discussion (2026-08-02):** Akeem's goal is AI/ML engineer; wants a portfolio strong enough for general IT/junior roles now. Discussed and settled: finish this matrix app's MVP (Sections 6-9) using the full `/next-lesson` method — slow, predict-before-run, self-written code — since he's still building HTML/CSS/JS/Flask/SQL fundamentals. After this MVP ships and is deployed, switch to faster/normal AI-assisted building for future features and future projects, since the point of the slow method is to reach fluency that makes fast AI-assisted building safe, not to build every future feature this way.
- **Mobile plans:** Akeem wants the app on iPhone/Android eventually, including parking-lot features like Screenzen-style app/screen-time blocking. Screen-time blocking specifically requires real native OS permissions (iOS Screen Time API / Android UsageStats) — impossible from a web app or PWA, so that feature is a genuine trigger for eventually going native. Agreed plan: finish the web MVP → make it responsive/PWA (installable, app-like, covers "usable on my phone" cheaply) → treat a native app (or React Native/Flutter) as a **separate future project #2 or #3** built against this same deployed Flask API, not a rebuild from scratch. Do not suggest abandoning the web app mid-build for a native rewrite.
- **Stack reaffirmed:** Flask/Python + SQLite/SQL is a good fit for the AI/ML career path (ML engineering is largely deploying/serving models via APIs — the exact skills being built here). No reason to switch to PHP/MySQL; SQLite→Postgres later is a small swap since the SQL itself transfers.
- **New project idea surfaced — Lebanese Arabic learning app:** Akeem's other app idea, and a much stronger fit for the AI/ML portfolio goal than the matrix app (real ML surface: fine-tuning ASR like Whisper for Levantine Arabic, pronunciation scoring, MSA↔Lebanese translation; spaced repetition should start as plain SM-2, not ML, until real review data exists). Key open constraint flagged but not yet explored: **data availability** for Levantine Arabic audio/text — the first question to answer before scoping this project for real. Treat as the likely project #2 after this MVP ships; do not start it before the matrix app is deployed.
- **On adding ML to the matrix app itself:** discussed and correctly assessed by Akeem as realistically LLM-API-based auto-categorization (call an LLM to assign a quadrant), not real ML engineering — a nice v2+ feature, not a portfolio ML credential. The Lebanese app is the stronger ML story.
- **Section 6.3 decision was left unresolved mid-session** (type column vs. separate `habits` table) — Akeem paused to have the above strategy discussion, then asked to resume the matrix app. When picking 6.3 back up, re-present the two options briefly (don't assume the earlier framing is remembered) and get an explicit choice before building.
- Model recommendation for this build: Sonnet 5, low-medium effort (bump to high if the agent starts skipping the teaching rules — dumping big code blocks, skipping predict-before-run). Confirmed by Akeem 2026-07-30 that low effort is fine for this project's difficulty level.
- **Editor: full Visual Studio 2026, not VS Code.** These are different products — don't suggest "VS Code" again; give Visual Studio-specific instructions (e.g. `Ctrl+K, Ctrl+D` to format, "Open Folder" for full IntelliSense, "ASP.NET and web development" workload if autocomplete is missing).
- **Teaching-style adjustment (2026-07-30, Section 2):** after task 2.1, Akeem said "I feel like I'm not learning, you're just doing stuff for me" — accurate feedback that blanks were sized for `seed`-level concepts even as several had moved to `practicing`. From task 2.2 onward: explain the concept and give the shape/pieces in plain language, but he writes the actual code from scratch — no skeleton file with `TODO(you)` blanks for anything above `seed` level. This worked well (task 2.2/2.3 both fully self-written, with real mistakes made and self-corrected). Keep this as the default going forward, not just for Section 2.
