# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a quiz -->

## git-source-control
- status: practicing
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-08-02
- evidence: correctly predicted `git init` creates a hidden `.git` folder; ran it in the wrong directory (D:\Claude instead of the project folder), diagnosed and fixed it himself after being shown the mismatch; correctly predicted the untracked-files delete was safe; needed a re-explanation to grasp add-vs-commit ("I don't understand what all of this does") — after the save-game analogy, completed add → commit → git config → commit successfully; afterward asked "what's git for" twice (mechanics landed before purpose did) — after a "what problem does it solve" reframe, correctly explained in his own words that git lets you revert to a past checkpoint when something breaks; second add+commit cycle (index.html) run cleanly and independently, correctly explained why `add` must precede `commit` ("otherwise we would be committing an empty list"). 2026-08-02: created `.gitignore` correctly from a described spec (`.vs/` and `tasks.db`), then independently verified it worked by re-running `git status` himself before being asked to. 2026-08-05: asked what `-A` meant rather than running an unfamiliar flag blindly (good instinct, worth keeping); then, told only that `-A` stages *everything that changed*, correctly reasoned unprompted that `tasks.db` would still be skipped because it's in `.gitignore` — connected two separately-learned pieces on his own. Correctly predicted that `git push` to an empty remote sends the entire history, not just the newest commit. Weak spot: wrote the commit message "Section 8" for a commit containing section 6's work — message described the calendar, not the change

## github-concept
- status: practicing
- depends-on: git-source-control
- introduced: 2026-07-30
- last-reviewed: 2026-08-05
- evidence: asked what GitHub is, unprompted; explained as a hosting service for git history (backup + sharing), separate from git itself — not yet checked in his own words. 2026-08-05 (6 days later, cold): asked for the git-vs-GitHub distinction in his own words and got the core of it right first try — "git is on my pc and github is online storage for it" — a real retrieval after days away, though he didn't mention collaboration/deployment (both supplied to him). Same day: created the repo through the GitHub UI himself (correctly leaving README/.gitignore/license uninitialized, after being warned why), added the `origin` remote, and pushed — first actual use of GitHub, done with step-by-step guidance

## frontend-concept
- status: introduced
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: correctly explained "frontend means the UI and everything you can see"

## backend-concept
- status: introduced
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: initially thought backend = "just accounts"; corrected to "anything that needs to persist data" — first contact, capped at introduced

## database-concept
- status: seed
- depends-on: backend-concept
- introduced: —
- last-reviewed: —
- evidence: —

## api-concept
- status: seed
- depends-on: frontend-concept, backend-concept
- introduced: —
- last-reviewed: —
- evidence: —

## deployment-concept
- status: practicing
- depends-on: backend-concept
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: recalled unprompted, days after the original heads-up in the same session, that Render's free tier "wipes the tasks eventually when I restart it"; correctly predicted a manual restart would wipe an added task, and confirmed it firsthand rather than taking it on faith. Judged the trade-off himself when asked whether it mattered right now — "just a thing worth knowing for now," correctly weighing that a to-do demo app has no real data at stake yet

## local-dev-environment
- status: practicing
- depends-on: none
- introduced: 2026-08-02
- last-reviewed: 2026-08-05
- evidence: chose a global pip install over a virtual environment after the trade-off (version conflicts across future projects) was explained — an informed, deliberate choice, not a gap; installed the wrong package by typo ("flash" instead of "flask"), self-recovered via `pip uninstall` then the correct install without prompting; verified the install worked via `python -c "import flask; print(...)"`; asked what pip is himself and, once told it's Python's package manager (parallel to npm), correctly extended the analogy to ask where git fits — and after being told git is version control (a different category), correctly recalled in his own words why git matters ("you can revert to older commits"). 2026-08-05: the cost of the global-install choice became concrete — `pip freeze` returned ~200 packages from unrelated projects, which he had predicted in advance; the decision still stands, but he has now seen its downside firsthand → [[dependency-management]]

## flask-choice
- status: introduced
- depends-on: backend-concept
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: explained the fit himself — "I don't have to learn a new language" (already knows Python from NeetCode)

## vanilla-js-frontend-choice
- status: introduced
- depends-on: frontend-concept
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: was genuinely uncertain vs React; decision made via explained trade-off (DOM fundamentals before frameworks), not a confident self-explanation — worth a real review question next time it comes up

## sqlite-choice
- status: introduced
- depends-on: database-concept
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: explained clearly — "postgres is for bigger companies... this is just my first project"

## render-choice
- status: introduced
- depends-on: deployment-concept
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: explained clearly — "Render is way simpler and I don't need AWS's complexity yet"

## html-structure
- status: practicing
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: filled in title/heading blanks in a scaffolded index.html correctly; correctly predicted that the `<title>` shows in the browser tab while `<h1>` shows on the visible page; added a `placeholder` attribute by writing only the raw value with no `name=` or quotes (correctly predicted "something's wrong" but needed the pattern spelled out — `name="value"` — before self-correcting and verifying it worked

## css-layout
- status: practicing
- depends-on: html-structure
- introduced: 2026-07-30
- last-reviewed: 2026-08-01
- evidence: first attempt at grid-template-columns omitted the property name and semicolon (wrote just the value); correctly predicted it wouldn't work before checking, self-identified the missing semicolon, needed a nudge to spot the missing property name, then correctly predicted the resulting 2x2 layout and confirmed it in the browser. 2026-08-01: after being taught display:flex as a sibling of display:grid, correctly predicted the checkbox would land beside the text and confirmed it in the browser; needed inline-vs-block explained to him to understand why an unstyled checkbox+div landed on separate lines

## css-class-selectors
- status: practicing
- depends-on: css-layout, html-structure
- introduced: 2026-07-30
- last-reviewed: 2026-08-01
- evidence: explained that a shared `class="quadrant"` avoids repeating the same style 4 times ("similar to classes in python" — noted as a surface analogy, not an accurate one); after being taught the leading-dot selector syntax, correctly answered that a class shared by 4 elements applies the CSS rule to all 4. 2026-08-01: wrote `.task { display:flex }` instead of `.entry`, missing that the selector must match the className set in JS — self-corrected once pointed at the mismatch

## css-color-coding
- status: practicing
- depends-on: css-layout, css-class-selectors
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: correctly filled in 4 valid CSS color values (pink, orange, lightblue, lightgreen) across 4 new per-quadrant classes; correctly predicted that the border/padding from the shared `.quadrant` class and the new background-color would both apply at once, not overwrite each other

## dom-manipulation
- status: practicing
- depends-on: html-structure
- introduced: 2026-07-30
- last-reviewed: 2026-08-01
- evidence: wrote createElement + textContent correctly on first try; initially didn't grasp building a dynamic querySelector string ("I didn't understand the third step"), needed a concrete worked example (entryQuadrant.value = "q3" walkthrough) before writing it correctly himself; recalled and applied appendChild unprompted; correctly predicted and then verified the entry lands in whichever quadrant was selected, across multiple quadrants; proactively removed the now-redundant alert() for cleanliness once asked. 2026-08-01: created a checkbox + wrapper div (newEntry) to group checkbox and text via appendChild, correctly predicting the resulting layout each time; needed the inline-vs-block explanation given to him (didn't derive it himself) before he could explain why the checkbox first appeared next to the quadrant label instead of the task text; confused `.type` with `.className` when first asked to set a CSS class from JS ("newEntry.type = 'flex'")

## event-listeners
- status: understood
- depends-on: dom-manipulation
- introduced: 2026-07-30
- last-reviewed: 2026-08-01
- evidence: first attached the listener to the wrong element (input instead of button) and self-corrected after being pointed at the mismatch; correctly predicted "nothing happens" both when the handler was empty and when it targeted the wrong id — showed real understanding that a listener only fires on the exact element it's attached to. 2026-08-01: correctly chose newCheckbox as the listener target and explained why unprompted ("the status is updated only through the checkbox"); wrote `newCheckbox.addEventListener("change", newText.classList.toggle("completed"))` which runs the toggle immediately instead of on change — self-diagnosed the bug correctly when asked to predict the outcome ("it will happen right away, so I always add the function") and fixed it by wrapping in a function, transferring the pattern from the click handler unprompted

## js-functions
- status: practicing
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-08-01
- evidence: wrote a full click-handler function from a plain-language spec (no code skeleton given, per his own request for less scaffolding). Made and fixed several real mistakes along the way: used raw ids as if they were variables (`entry-text.value` — also hit the hyphen issue), passed two arguments to `alert()` instead of one concatenated string, and initially read the element instead of `.value` off it. Needed an extra explicit hint partway through, but the final code was self-written and tested working end-to-end. 2026-08-01: independently found and diagnosed a shared-variable bug in his own click handler (see variable-scope). 2026-08-01: initiated and mostly self-drove an unprompted refactor extracting entry-creation into a named `createEntry(text)` function — correctly reasoned that an unused `quadrant` parameter should be removed ("why did we need the quadrant parameter?" after noticing it wasn't referenced in the body), got `if`-statement syntax wrong twice (`if x then { return }`, `if (x) then { return }`) before writing valid JS on the third try

## in-memory-data
- status: practicing
- depends-on: js-functions
- introduced: 2026-08-01
- last-reviewed: 2026-08-02
- evidence: correctly predicted and confirmed that refreshing wipes all added tasks; initial explanation was surface-level ("they're not getting saved"/"living somewhere idk"), but after being told DOM elements live only in the browser's temporary memory until refresh, confirmed understanding in his own words ("I get it now, its the browsers memory"). 2026-08-02: correctly predicted a task added via the "Add" button wouldn't survive a refresh once the app also had a fetched, server-backed list ("its not there because its not getting saved into the api/tasks"); after one correction (mistakenly called the hardcoded Python list a "database"), correctly explained the real distinction unprompted ("the list isn't altered and its sitting in my pc... the button tasks are just being created in the browser")

## variable-scope
- status: practicing
- depends-on: js-functions
- introduced: 2026-08-01
- last-reviewed: 2026-08-01
- evidence: discovered unprompted that checking an older task's checkbox crossed out the newest task's text instead; correctly reasoned that `newText = ...` without `let` is "the same one being overwritten" each click, and correctly predicted that an old checkbox's listener would reference "the latest newText" at the moment it fires — strong self-driven diagnosis. Needed to be told the `let` fix itself and which 4 lines to apply it to (two "idk"s), but verified the fix worked correctly across multiple out-of-order checkboxes. Later the same day: while extracting `createEntry` into its own function, correctly identified that variables declared inside it (`newCheckbox`/`newText`) wouldn't be visible in the click handler ("they live in the createEntry function" → correctly predicted "it doesn't work now"), then independently fixed it by moving the `change` listener inside `createEntry` next to its declarations

## what-is-a-server
- status: introduced
- depends-on: backend-concept
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: after being told a server listens for requests and sends responses, correctly restated the core idea unprompted ("app.py will be the server and when the browser asks for the website it sends it through my network") — reasonably solid first-contact grasp, not yet checked against a harder case

## flask-routes
- status: practicing
- depends-on: what-is-a-server, flask-choice
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: didn't yet have an intuition for what a "route" is when asked cold ("Idk"); wrote the `@app.route("/")` decorator and handler function correctly from a described spec, no errors — mechanical execution is solid, conceptual grasp not yet self-demonstrated. Same day, after seeing `/` work: correctly predicted that requesting an undefined route (`/tasks`) would error ("it would do nothing or an error"), then confirmed the actual 404 in the browser — real conceptual grasp shown, but still same-day so capped at practicing. Same day: correctly predicted that swapping the route's return value to `send_file("index.html")` would serve the actual matrix page, then confirmed it in the browser. Same day: after two rounds of clarification, correctly restated a route as "making a line towards a specific page," and correctly described the `app` object as "an object with properties" (built-in abilities like `.route()`/`.run()`) rather than "a bunch of functions" once corrected — needed real back-and-forth to get there, not first-pass. 2026-08-02 (later): implemented a dynamic route (`<int:task_id>`) correctly from a description

## http-basics
- status: practicing
- depends-on: what-is-a-server
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly predicted opening `index.html` directly vs. via Flask would behave identically for now, correctly reasoning it's the same file either way; after being told the difference is delivery mechanism (disk read vs. HTTP request/response), asked a clarifying follow-up unprompted ("what do you mean 'how it gets to the browser'") rather than nodding along

## local-dev-server
- status: practicing
- depends-on: local-dev-environment, what-is-a-server
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly predicted `python app.py` would start the server on `127.0.0.1:5000` and not return the terminal prompt; ran it, viewed `/` at that address, and confirmed the response in his own browser

## rest-apis
- status: practicing
- depends-on: api-concept, http-basics
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly predicted, before running, that naming a Flask route function `tasks()` (same name as the global `tasks` list) would overwrite the list reference ("oh it gets reassigned to the function") — transferred the variable-scope/shared-name lesson from earlier sections unprompted; renamed it to `get_tasks` correctly and confirmed `/api/tasks` returned the right JSON

## fetch-api
- status: practicing
- depends-on: rest-apis, dom-manipulation
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: confirmed the "Promise/IOU" framing made sense as a reason `fetch()` can't be used synchronously; wrote the `fetch().then().then()` skeleton correctly from a description, confirmed the logged data in the console; when the `createEntry` param mismatch was surfaced (a plain string doesn't have `.value`), first proposed an unrelated fix (a separate JS list) before landing on the correct one (drop `.value` in `createEntry`, pass `entryText.value` at the call site) once walked through it; wrote the `.forEach` loop correctly from a description and confirmed real fetched tasks rendering in the correct quadrants. Same day: wrote a POST `fetch()` call with a `method`/`headers`/`body` options object and `JSON.stringify(...)` correctly from a description, and confirmed a task added via the button survived both a refresh and a full server restart. Same day (later, unplanned Q&A): initially unclear on why `.then()` appears twice and what `response.json()` actually does ("I just don't get whats going on"); after a two-envelope walkthrough (response arrives → its body gets parsed, each step its own Promise), correctly concluded the `data`/`result` variable names are arbitrary labels with no effect on what value flows through the chain ("its always the same thing but we pick the name depending on the context") — real conceptual gap closed, not just pattern-matching syntax anymore

## json
- status: practicing
- depends-on: none
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: when asked what a task-list route should send back, unprompted named all three needed fields correctly ("taskText, the quadrant its in, and whether its completed or not"); wrote a matching Python list-of-dicts (`tasks = [{"text":..., "quadrant":..., "completed": False}, ...]`) correctly on first try; confirmed the resulting JSON output in the browser matched the structure. Same day: correctly explained the `[ ]`/`{ }` structure in his own words ("[ ] is a list and { } is a dictionary")

## request-response-cycle
- status: introduced
- depends-on: http-basics
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: saw the real request/response pair happen end to end via `fetch("/api/tasks")` — the Network tab showing a 200 status, then the parsed JSON response used to render entries; not yet asked to explain the cycle in his own words

## python-main-guard
- status: practicing
- depends-on: none
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: initially said "I don't get it" to the abstract explanation of `if __name__ == "__main__":`; after a concrete worked example (a hypothetical `test_app.py` importing `app.py` and accidentally starting a real server without the guard), confirmed understanding ("yes I get it")

## sql-basics
- status: practicing
- depends-on: database-concept, sqlite-choice
- introduced: 2026-08-02
- last-reviewed: 2026-08-05
- evidence: correctly predicted, before running, that `python app.py` would produce no visible output but create a new `tasks.db` file — confirmed correct in the browser folder; wrote/adapted the `CREATE TABLE IF NOT EXISTS` statement correctly from a described spec. 2026-08-05: asked cold whether adding a column to the `CREATE TABLE IF NOT EXISTS` statement would alter the already-existing table, answered correctly and immediately with the right reason ("no it won't get added because the table exists") — first-try, unprompted, no hint given; then correctly predicted that deleting `tasks.db` and re-running `python app.py` would recreate it, and confirmed it

## schema-design
- status: practicing
- depends-on: sql-basics
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly named all four needed columns unprompted (`id, text, quadrant, completed`) by extending the already-designed JSON task shape plus a unique identifier

## insert-select
- status: practicing
- depends-on: sql-basics
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly identified the row-to-dict conversion step needed before `jsonify` unprompted; struggled to write the actual conversion loop from just a description ("Idk how", asked "where do I write it") and needed the exact lines given — mechanical execution needed real scaffolding this time, unlike the earlier `.forEach` equivalent in JS. Correctly predicted `/api/tasks` would return `[]` on an empty table and confirmed it; identified and removed the now-dead hardcoded `tasks` list unprompted once pointed at it. Same day: wired up the `POST /api/tasks` route and matching `INSERT` statement from a described spec, then correctly predicted a task would survive both a page refresh and a full server restart, and confirmed both

## full-crud
- status: seed
- depends-on: rest-apis, insert-select
- introduced: —
- last-reviewed: —
- evidence: —

## put-delete-requests
- status: practicing
- depends-on: rest-apis
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: implemented the `POST` half (registering a second route at the same address via `methods=["POST"]`, sending JSON via `fetch`'s options object) correctly from a description. Same day: correctly caught, unprompted, that two call sites (`createEntry(task.text)` and later the "Add" handler) needed updating after `createEntry`'s signature changed to take a full task object, correctly predicting the resulting "undefined" bug before running it; implemented the full `PUT` round trip (dynamic Flask route, `cursor.lastrowid`, waiting for the POST response before building the entry, `checkbox.dataset.id`) from descriptions and correctly predicted/confirmed a checked task survives a refresh. Same day: attempted the `DELETE` route by copying the PUT pattern but initially read an unnecessary JSON body instead of using the already-available `task_id` — self-corrected once asked whether a body was actually needed; hit a real Python gotcha (`(task_id)` vs `(task_id,)` — parens vs. a one-item tuple) and needed the fix given directly; wired the delete button and `entry.remove()` correctly from a description, confirmed deleted tasks stay gone after refresh

## task-vs-habit-modeling
- status: introduced
- depends-on: schema-design
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: asked cold for one concrete behavioral difference between a task and a habit, answered in his own words unprompted — "a habit repeats every day, a task means when you complete it, it disappears the next day" — and brought his own reference point (the iOS app Eva), noting Eva doesn't let you put habits in an Eisenhower matrix. The modeling itself was **not built**: a `kind` column was added and then reverted the same session when the feature was cut from MVP scope. Concept understood at the product level, never implemented — see the plan's parking lot

## mvp-scope-cutting
- status: introduced
- depends-on: none
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: raised doubt about the project unprompted ("I'm skeptical about all of this, I don't know why", then "maybe I should make another project") — the doubt was well-aimed: it landed exactly on a task that would have stored the *label* "habit" without any of the behavior he'd just described. After the trade-off was named (starting fresh = redoing HTML/CSS he already knows, and still never having deployed anything), chose to cut the feature and keep the project rather than abandon it. First contact with scope-cutting as a deliberate move; he made the call but did not yet articulate the reasoning back in his own words

## automated-testing
- status: seed
- depends-on: full-crud
- introduced: —
- last-reviewed: —
- evidence: —

## input-validation
- status: practicing
- depends-on: full-crud
- introduced: 2026-08-01
- last-reviewed: 2026-08-01
- evidence: proposed the guard-clause approach himself ("check if the text is either empty or spaces only, then just use return at the top of the click event listener"); wrote the `.trim() === ""` condition correctly, needed two attempts to get `if` statement syntax right (JS doesn't use `then`)

## error-handling
- status: seed
- depends-on: request-response-cycle
- introduced: —
- last-reviewed: —
- evidence: —

## dependency-management
- status: practicing
- depends-on: local-dev-environment
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: asked what happens when a fresh machine with no Flask hits `from flask import Flask`, answered correctly and immediately ("it would error because flask isnt installed there"); correctly predicted `pip freeze` would list far more than Flask, reasoning from his own earlier decision to install globally rather than into a virtual environment — then saw the ~200-line reality. Asked how many of Flask's eight `pip freeze` lines belong in `requirements.txt`, answered "just flask because pip installs the rest" unprompted — the direct-vs-transitive distinction, with the correct mechanism. Authored `requirements.txt` himself; correctly predicted `pip install -r requirements.txt` would report the requirement already satisfied. First contact, so capped at practicing despite a clean run

## production-vs-dev-server
- status: practicing
- depends-on: local-dev-server
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: had noticed Flask's dev-server warning all week but read it as an error rather than a purpose distinction ("I don't like seeing red in there") — corrected: dev server is single-request, built for convenience during coding, not load. First guess at the concrete failure mode ("it would crash") was wrong but reasonable; corrected to "queues and waits" rather than crashing. Transferred the install→pin-in-requirements.txt pattern from Flask to gunicorn unprompted, predicting the install command correctly before running it. Told plainly that gunicorn cannot run on Windows at all and verification would have to wait for Render — not yet demonstrated, since nothing has deployed yet

## environment-variables
- status: practicing
- depends-on: deployment-concept
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: after being told Render assigns the network port dynamically via a `PORT` variable, correctly predicted the failure mode of deploying without `--bind 0.0.0.0:$PORT` ("it starts fine but nobody can reach it") — close enough to the real mechanism (gunicorn binds to its own default port; Render's health check just can't find it) that the correction was a refinement, not a reversal. Added `--bind 0.0.0.0:$PORT` to the Start Command himself and it deployed successfully

## github-based-deploy-flow
- status: practicing
- depends-on: git-based-deploy, github-concept
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: connected the GitHub repo to a new Render Web Service, correctly reasoned (unprompted, when asked to choose between Static Site and Web Service) that a static site can't run Python and his app needs a live process, choosing Web Service correctly. Encountered a real mismatch — opened a URL that turned out to belong to someone else's identically-named Eisenhower Matrix project — and correctly diagnosed it himself by comparing the address bar against the dashboard's actual URL once asked to check, rather than assuming the app was broken. Verified the deployed app for real: added a task through the live URL, refreshed, confirmed persistence on Render's Linux machine running gunicorn

## git-based-deploy
- status: practicing
- depends-on: git-source-control, deployment-concept, render-choice
- introduced: 2026-08-05
- last-reviewed: 2026-08-05
- evidence: connected GitHub repo to Render, correctly chose Web Service over Static Site reasoning that Python needs a live process; deployed successfully after fixing the Start Command to bind `$PORT`; verified the live app for real (added a task, refreshed, confirmed persistence) — see [[github-based-deploy-flow]] for the full blow-by-blow

## mvp-review
- status: seed
- depends-on: full-crud
- introduced: —
- last-reviewed: —
- evidence: —

## readme-portfolio-framing
- status: seed
- depends-on: mvp-review
- introduced: —
- last-reviewed: —
- evidence: —

## demo-practice
- status: seed
- depends-on: readme-portfolio-framing
- introduced: —
- last-reviewed: —
- evidence: —
