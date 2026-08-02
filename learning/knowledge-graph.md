# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a quiz -->

## git-source-control
- status: practicing
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: correctly predicted `git init` creates a hidden `.git` folder; ran it in the wrong directory (D:\Claude instead of the project folder), diagnosed and fixed it himself after being shown the mismatch; correctly predicted the untracked-files delete was safe; needed a re-explanation to grasp add-vs-commit ("I don't understand what all of this does") — after the save-game analogy, completed add → commit → git config → commit successfully; afterward asked "what's git for" twice (mechanics landed before purpose did) — after a "what problem does it solve" reframe, correctly explained in his own words that git lets you revert to a past checkpoint when something breaks; second add+commit cycle (index.html) run cleanly and independently, correctly explained why `add` must precede `commit` ("otherwise we would be committing an empty list")

## github-concept
- status: introduced
- depends-on: git-source-control
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: asked what GitHub is, unprompted; explained as a hosting service for git history (backup + sharing), separate from git itself — not yet checked in his own words

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
- status: seed
- depends-on: backend-concept
- introduced: —
- last-reviewed: —
- evidence: —

## local-dev-environment
- status: practicing
- depends-on: none
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: chose a global pip install over a virtual environment after the trade-off (version conflicts across future projects) was explained — an informed, deliberate choice, not a gap; installed the wrong package by typo ("flash" instead of "flask"), self-recovered via `pip uninstall` then the correct install without prompting; verified the install worked via `python -c "import flask; print(...)"`; asked what pip is himself and, once told it's Python's package manager (parallel to npm), correctly extended the analogy to ask where git fits — and after being told git is version control (a different category), correctly recalled in his own words why git matters ("you can revert to older commits")

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
- last-reviewed: 2026-08-01
- evidence: correctly predicted and confirmed that refreshing wipes all added tasks; initial explanation was surface-level ("they're not getting saved"/"living somewhere idk"), but after being told DOM elements live only in the browser's temporary memory until refresh, confirmed understanding in his own words ("I get it now, its the browsers memory")

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
- evidence: didn't yet have an intuition for what a "route" is when asked cold ("Idk"); wrote the `@app.route("/")` decorator and handler function correctly from a described spec, no errors — mechanical execution is solid, conceptual grasp not yet self-demonstrated. Same day, after seeing `/` work: correctly predicted that requesting an undefined route (`/tasks`) would error ("it would do nothing or an error"), then confirmed the actual 404 in the browser — real conceptual grasp shown, but still same-day so capped at practicing

## http-basics
- status: seed
- depends-on: what-is-a-server
- introduced: —
- last-reviewed: —
- evidence: —

## local-dev-server
- status: practicing
- depends-on: local-dev-environment, what-is-a-server
- introduced: 2026-08-02
- last-reviewed: 2026-08-02
- evidence: correctly predicted `python app.py` would start the server on `127.0.0.1:5000` and not return the terminal prompt; ran it, viewed `/` at that address, and confirmed the response in his own browser

## rest-apis
- status: seed
- depends-on: api-concept, http-basics
- introduced: —
- last-reviewed: —
- evidence: —

## fetch-api
- status: seed
- depends-on: rest-apis, dom-manipulation
- introduced: —
- last-reviewed: —
- evidence: —

## json
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## request-response-cycle
- status: seed
- depends-on: http-basics
- introduced: —
- last-reviewed: —
- evidence: —

## sql-basics
- status: seed
- depends-on: database-concept, sqlite-choice
- introduced: —
- last-reviewed: —
- evidence: —

## schema-design
- status: seed
- depends-on: sql-basics
- introduced: —
- last-reviewed: —
- evidence: —

## insert-select
- status: seed
- depends-on: sql-basics
- introduced: —
- last-reviewed: —
- evidence: —

## full-crud
- status: seed
- depends-on: rest-apis, insert-select
- introduced: —
- last-reviewed: —
- evidence: —

## put-delete-requests
- status: seed
- depends-on: rest-apis
- introduced: —
- last-reviewed: —
- evidence: —

## task-vs-habit-modeling
- status: seed
- depends-on: schema-design
- introduced: —
- last-reviewed: —
- evidence: —

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

## environment-variables
- status: seed
- depends-on: deployment-concept
- introduced: —
- last-reviewed: —
- evidence: —

## git-based-deploy
- status: seed
- depends-on: git-source-control, deployment-concept, render-choice
- introduced: —
- last-reviewed: —
- evidence: —

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
