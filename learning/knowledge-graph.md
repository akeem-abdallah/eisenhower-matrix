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
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

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
- last-reviewed: 2026-07-30
- evidence: first attempt at grid-template-columns omitted the property name and semicolon (wrote just the value); correctly predicted it wouldn't work before checking, self-identified the missing semicolon, needed a nudge to spot the missing property name, then correctly predicted the resulting 2x2 layout and confirmed it in the browser

## css-class-selectors
- status: practicing
- depends-on: css-layout, html-structure
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: explained that a shared `class="quadrant"` avoids repeating the same style 4 times ("similar to classes in python" — noted as a surface analogy, not an accurate one); after being taught the leading-dot selector syntax, correctly answered that a class shared by 4 elements applies the CSS rule to all 4

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
- last-reviewed: 2026-07-30
- evidence: wrote createElement + textContent correctly on first try; initially didn't grasp building a dynamic querySelector string ("I didn't understand the third step"), needed a concrete worked example (entryQuadrant.value = "q3" walkthrough) before writing it correctly himself; recalled and applied appendChild unprompted; correctly predicted and then verified the entry lands in whichever quadrant was selected, across multiple quadrants; proactively removed the now-redundant alert() for cleanliness once asked

## event-listeners
- status: practicing
- depends-on: dom-manipulation
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: first attached the listener to the wrong element (input instead of button) and self-corrected after being pointed at the mismatch; correctly predicted "nothing happens" both when the handler was empty and when it targeted the wrong id — showed real understanding that a listener only fires on the exact element it's attached to

## js-functions
- status: practicing
- depends-on: none
- introduced: 2026-07-30
- last-reviewed: 2026-07-30
- evidence: wrote a full click-handler function from a plain-language spec (no code skeleton given, per his own request for less scaffolding). Made and fixed several real mistakes along the way: used raw ids as if they were variables (`entry-text.value` — also hit the hyphen issue), passed two arguments to `alert()` instead of one concatenated string, and initially read the element instead of `.value` off it. Needed an extra explicit hint partway through, but the final code was self-written and tested working end-to-end

## in-memory-data
- status: seed
- depends-on: js-functions
- introduced: —
- last-reviewed: —
- evidence: —

## what-is-a-server
- status: seed
- depends-on: backend-concept
- introduced: —
- last-reviewed: —
- evidence: —

## flask-routes
- status: seed
- depends-on: what-is-a-server, flask-choice
- introduced: —
- last-reviewed: —
- evidence: —

## http-basics
- status: seed
- depends-on: what-is-a-server
- introduced: —
- last-reviewed: —
- evidence: —

## local-dev-server
- status: seed
- depends-on: local-dev-environment, what-is-a-server
- introduced: —
- last-reviewed: —
- evidence: —

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
- status: seed
- depends-on: full-crud
- introduced: —
- last-reviewed: —
- evidence: —

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
