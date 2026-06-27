# Content Plan

## Context

- Followers at start: 61 (2026-06-27)
- Target cadence: 2-3x per week, Tue/Thu + optional Fri
- Best posting time: 7:30-9:00 AM local time
- 12-month realistic target: 1000-2500 followers

## Daily non-negotiables (primary growth lever until 500 followers)

- 5-10 comments per day on Playwright/QA/AI-testing posts with 50+ likes
- Reply to every comment on your own posts within 30 minutes
- See `engagement-strategy.md` for targeting, quality bar, and daily rhythm

## Profile (do before scaling comments)

- Run `linkedin-profile-optimizer` with goal = "authority + product sales"
- Headline target: `Senior SDET | Playwright/TypeScript | Helping QA teams ship faster with less flake`
- Featured section item 1: Playwright Production Checklist
- Pin Playwright Production Checklist as first comment on every post immediately after publishing

---

## Week 1

| Day | Pillar | Angle | Format | Checklist | Hashtags | Status |
|---|---|---|---|---|---|---|
| Tue | P4 | Claude generated `.toBeVisible()`. test passed. bug shipped. button was disabled for 800ms during async validation. `.toBeEnabled()` would have caught it. one word different. | counterintuitive claim | yes | #Playwright #AI | drafted ✓ |
| Thu | P1 | Playwright trace viewer in CI. when a test fails in CI but passes locally, the trace is your only evidence. most teams open it once and give up. what to look for first. | practitioner observation | yes | #Playwright #SoftwareTesting | not drafted |
| Fri | CONTRARIAN | "80% code coverage is a vanity metric." it tells you which lines ran, not which behaviors were verified. you can hit 80% with assertions that never fail. | F10 contrarian | no | #SoftwareTesting #QualityAssurance | not drafted |

## Week 2

| Day | Pillar | Angle | Format | Checklist | Hashtags | Status |
|---|---|---|---|---|---|---|
| Tue | CONTRARIAN | "your e2e tests are not the problem. your app is." everyone blames the tests for being slow and flaky. the tests are showing you the truth. | F10 contrarian | no | #Playwright #SoftwareTesting | not drafted |
| Thu | P2 | difference between quarantining a flaky test and disabling one. most teams do the second and call it the first. quarantine means: isolated, tracked, owner assigned, deadline to fix or delete. | counterintuitive claim | yes | #Playwright #SoftwareTesting | not drafted |
| Fri (optional) | P5 | how to frame flaky CI to an EM as a productivity cost. "CI was red 23% of runs last sprint. at 20 engineers x 15min investigation per failure, that's X hours of eng time. the fix is 2 days." | number-drop | no | #SoftwareTesting #QualityAssurance | not drafted |

---

## Drafted posts

### Week 1 — Tuesday (P4) — READY TO POST

claude wrote this assertion for our submit button: .toBeVisible()

test passed. bug shipped.

the button was visible. it was also disabled for 800ms while an async validation call resolved. the user clicked during that window. the form never submitted. we found out from a support ticket, not from CI.

the problem: AI generates assertions from what it can observe at generation time. it sees a visible button. it does not know the button has three states across an async lifecycle. it cannot know where the risk lives.

the assertion that would have caught it: .toBeEnabled(). one word different.

this is the gap that doesn't appear in any AI-testing demo: coverage goes up, pass rate stays green, and the bugs that require knowing your system still get through.

I cover more assertion patterns like this in the Playwright Production Checklist — link in featured section.

what's the most important assertion in your suite that Claude would never have written on its own?

#Playwright #AI

**Image:** carbon.now.sh — dark theme, two-column code comparison:
```
// Claude generated                    // what catches the bug
.toBeVisible()  ✅ test passes         .toBeEnabled()  ✅ catches async disable
```
