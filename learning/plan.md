# Learning plan: Eisenhower Matrix (tasks + habits)

## Locked decisions
- Backend language: Python (Flask) — already knows Python from NeetCode, avoids learning a new language while learning web dev
- Frontend approach: Plain HTML/CSS/JavaScript — no framework, builds real DOM/JS fundamentals before adding React-style abstraction later
- Database: SQLite — real relational database, zero server setup, standard first DB for Flask beginners
- Deployment/hosting: Render (or equivalent simple host) — free tier, minimal config, no server management, vs. AWS's much bigger learning curve

## Sections

### 1. Static quadrant page  [ ] not started
**Deliverable:** A page in the browser showing the 4 colored quadrants, hardcoded, no data yet.
**Concepts:** html-structure, css-layout, css-color-coding, git-source-control
**Tasks:**
- [ ] 1.1 Initialize git and make a baseline commit
- [ ] 1.2 Create `index.html` with a basic page structure and a heading
- [ ] 1.3 Lay out the 4 quadrants as a grid using CSS
- [ ] 1.4 Color-code each quadrant
- [ ] 1.5 Commit the finished static page

### 2. Interactive but temporary  [ ] not started
**Deliverable:** Type a task/habit, add it to a quadrant, mark it complete — all in-browser, nothing saved permanently yet.
**Concepts:** dom-manipulation, event-listeners, js-functions, in-memory-data

### 3. A real server  [ ] not started
**Deliverable:** The page loads from a running Flask server (localhost) instead of just opening the file directly.
**Concepts:** what-is-a-server, flask-routes, http-basics, local-dev-server

### 4. Frontend talks to backend  [ ] not started
**Deliverable:** The page fetches its quadrant data from the server instead of having it hardcoded in the JS file.
**Concepts:** rest-apis, fetch-api, json, request-response-cycle

### 5. Remembering things  [ ] not started
**Deliverable:** Add a task, restart the server, refresh the page — it's still there.
**Concepts:** sql-basics, schema-design, insert-select

### 6. Full core feature  [ ] not started
**Deliverable:** Full add/complete/delete for tasks and habits, in any quadrant, all persisted for real.
**Concepts:** full-crud, put-delete-requests, task-vs-habit-modeling

### 7. Tests and safety rails  [ ] not started
**Deliverable:** One command automatically checks that the core API endpoints work.
**Concepts:** automated-testing, input-validation, error-handling

### 8. Going live  [ ] not started
**Deliverable:** A real public URL, usable from any device, anywhere.
**Concepts:** environment-variables, git-based-deploy

### 9. Wrap the MVP  [ ] not started
**Deliverable:** MVP checklist fully checked off; can explain the whole app end to end.
**Concepts:** mvp-review, readme-portfolio-framing, demo-practice
