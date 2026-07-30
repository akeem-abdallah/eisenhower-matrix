# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a quiz -->

## git-source-control
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

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
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## css-layout
- status: seed
- depends-on: html-structure
- introduced: —
- last-reviewed: —
- evidence: —

## css-color-coding
- status: seed
- depends-on: css-layout
- introduced: —
- last-reviewed: —
- evidence: —

## dom-manipulation
- status: seed
- depends-on: html-structure
- introduced: —
- last-reviewed: —
- evidence: —

## event-listeners
- status: seed
- depends-on: dom-manipulation
- introduced: —
- last-reviewed: —
- evidence: —

## js-functions
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

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
