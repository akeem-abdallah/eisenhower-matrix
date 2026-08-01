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
- Model recommendation for this build: Sonnet 5, low-medium effort (bump to high if the agent starts skipping the teaching rules — dumping big code blocks, skipping predict-before-run). Confirmed by Akeem 2026-07-30 that low effort is fine for this project's difficulty level.
- **Editor: full Visual Studio 2026, not VS Code.** These are different products — don't suggest "VS Code" again; give Visual Studio-specific instructions (e.g. `Ctrl+K, Ctrl+D` to format, "Open Folder" for full IntelliSense, "ASP.NET and web development" workload if autocomplete is missing).
- **Teaching-style adjustment (2026-07-30, Section 2):** after task 2.1, Akeem said "I feel like I'm not learning, you're just doing stuff for me" — accurate feedback that blanks were sized for `seed`-level concepts even as several had moved to `practicing`. From task 2.2 onward: explain the concept and give the shape/pieces in plain language, but he writes the actual code from scratch — no skeleton file with `TODO(you)` blanks for anything above `seed` level. This worked well (task 2.2/2.3 both fully self-written, with real mistakes made and self-corrected). Keep this as the default going forward, not just for Section 2.
