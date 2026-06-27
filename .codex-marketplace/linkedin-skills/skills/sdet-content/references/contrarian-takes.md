# Contrarian Takes — SDET Edition

Controversy on LinkedIn works when the take is "true but uncomfortable" — something practitioners secretly agree with but nobody says out loud. It generates comments from people who disagree (good) AND people who finally feel validated (better).

Rule: every contrarian post must be defensible in comments with a real example or number. If you can't back it up, it reads as rage-bait.

Use hook formula F10 (Contrarian + Historical Receipts) from `../../references/hook-formulas.md`.

---

## High-engagement contrarian positions

### On test coverage

> **"80% code coverage is a vanity metric."**
> it tells you which lines ran. it does not tell you which behaviors were verified. you can hit 80% coverage with assertions that never fail. most teams have done exactly this.

> **"we deleted 400 unit tests last quarter. CI got faster. we caught more bugs."**
> the tests we deleted were asserting on implementation details, not behavior. every refactor broke them. they were slowing us down without protecting anything.

### On the test pyramid

> **"the test pyramid is wrong for microservices."**
> the pyramid assumes a monolith where unit tests are cheap and e2e tests are expensive. in a distributed system, the integration boundaries are where everything fails. the pyramid sends you in the wrong direction.

> **"your e2e tests are not the problem. your app is."**
> everyone says e2e tests are too slow and too flaky. actually they're slow because the app is slow and flaky because the app is flaky. the tests are showing you the truth. you're blaming the messenger.

### On AI in testing

> **"AI won't replace QA engineers. it will replace QA engineers who use AI to write the same tests they wrote before."**
> the engineers who survive are the ones using AI to test things that couldn't be tested before. not the ones generating 200 unit tests that pass by testing the mock.

> **"AI-generated test suites are coverage theater."**
> the coverage number goes up. the pass rate stays green. the bugs that require understanding your system still ship. the metric improved. the risk didn't.

### On Playwright and tooling

> **"Page Object Model is 2012 thinking."**
> if you're still wrapping every UI component in a Page Object class with Playwright in 2026, your test architecture is the problem, not your flake rate.

> **"Cypress users switching to Playwright aren't switching because Playwright is better."**
> they're switching because their Cypress tests were badly designed. they'll have the same problems in 6 months with different syntax.

### On CI and process

> **"a green CI build is not evidence of quality. it's evidence that your tests ran."**
> there's a difference. most engineering teams have not made this distinction and their incident rate reflects it.

> **"shift-left failed at most companies."**
> they moved testing earlier in the sprint without moving the test infrastructure. same problems, different standup. if your environments aren't stable and your test data isn't controlled, shifting left just means you find the same bugs faster and fix nothing.

### On the SDET role

> **"the SDET role is a symptom, not a solution."**
> it exists because developers write untestable code. the right fix is testability by design. most companies hire an SDET instead.

> **"hiring more SDETs won't fix your quality problem."**
> if the architecture makes tests expensive to write and maintain, adding people to write expensive tests scales the problem. the bottleneck is design, not headcount.

---

## How to frame a contrarian post

Structure that works:

1. **The claim** (1-2 sentences, blunt, specific) — this is the hook
2. **Why most people believe the opposite** (1 sentence) — shows you understand the mainstream view
3. **The real-world evidence** (2-3 sentences with a specific number or example)
4. **The nuance** (1-2 sentences — not a full retraction, but an acknowledgment of edge cases) — makes you look fair, not reckless
5. **The question** (1 sentence, specific, invites the disagreement you want)

The nuance section is what separates a defensible contrarian post from rage-bait. Include it every time.

---

## Cadence

One contrarian post per week maximum. Two in a row signals you're chasing engagement rather than sharing real views. Mix with P1/P2 practitioner posts to maintain credibility.

Contrarian posts work best on Tuesday (peak SDET audience). Save Thursday for the more practical/instructional content.
