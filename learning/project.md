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
- Model recommendation for this build: Sonnet 5, medium effort (bump to high if the agent starts skipping the teaching rules — dumping big code blocks, skipping predict-before-run).
