# Content Plan

## Context

- Followers at start: 61 (2026-06-27)
- Target cadence: 2-3x per week, Tue/Thu + optional Fri
- Best posting time: 7:30-9:00 AM local time
- 12-month realistic target: 1000-2500 followers
- Goal: employer attractiveness (Swiss market) + audience growth. No product pitch in posts.

## Daily non-negotiables (primary growth lever until 500 followers)

- 5-10 comments per day on Playwright/QA/AI-testing posts with 50+ likes
- Reply to every comment on your own posts within 30 minutes
- See `engagement-strategy.md` for targeting, quality bar, and daily rhythm

## Profile (do before scaling comments)

- Headline and About: see `linkedin-profile.md`
- Featured section: Authority OS project link

---

## Week 1 (Jun 30 – Jul 4)

| Day | Pillar | Angle | Format | Hashtags | Status |
|---|---|---|---|---|---|
| Tue Jul 1 | P4 | Claude generated `.toBeVisible()`. test passed. bug shipped. `.toBeEnabled()` would have caught it. one word different. | counterintuitive claim | #Playwright #AI | drafted ✓ |
| Thu Jul 3 | P1 | Playwright trace viewer in CI. when a test fails in CI but passes locally, the trace is your only evidence. what to look for first. | practitioner observation | #Playwright #SoftwareTesting | drafted ✓ |
| Fri Jul 4 | CONTRARIAN | "80% code coverage is a vanity metric." it tells you which lines ran, not which behaviors were verified. | F10 contrarian | #SoftwareTesting #QualityAssurance | drafted ✓ |

## Week 2 (Jul 7 – Jul 11)

| Day | Pillar | Angle | Format | Hashtags | Status |
|---|---|---|---|---|---|
| Tue Jul 8 | P6 | does it make sense to start with QA in 2026? yes — but skip manual testing entirely. learn Playwright and CI from day one. the manual-first path is the one AI is replacing. | counterintuitive claim | #SoftwareTesting #QualityAssurance | not drafted |
| Thu Jul 10 | P2 | difference between quarantining a flaky test and disabling one. most teams do the second and call it the first. quarantine means: isolated, tracked, owner assigned, deadline to fix or delete. | counterintuitive claim | #Playwright #SoftwareTesting | not drafted |
| Fri Jul 11 | CONTRARIAN | "your e2e tests are not the problem. your app is." everyone blames the tests for being slow and flaky. the tests are showing you the truth. | F10 contrarian | #Playwright #SoftwareTesting | not drafted |

---

## Drafted posts

### Week 1 — Tuesday Jul 1 (P4) — READY TO POST

claude wrote this assertion for our submit button: .toBeVisible()

test passed. bug shipped.

the button was visible. it was also disabled for 800ms while an async validation call resolved. the user clicked during that window. the form never submitted. we found out from a support ticket, not from CI.

the problem: AI generates assertions from what it can observe at generation time. it sees a visible button. it does not know the button has three states across an async lifecycle. it cannot know where the risk lives.

the assertion that would have caught it: .toBeEnabled(). one word different.

this is the gap that doesn't appear in any AI-testing demo: coverage goes up, pass rate stays green, and the bugs that require knowing your system still get through.

what's the most important assertion in your suite that Claude would never have written on its own?

#Playwright #AI

**Image:** carbon.now.sh — dark theme, two-column code comparison:
```
// Claude generated                    // what catches the bug
.toBeVisible()  ✅ test passes         .toBeEnabled()  ✅ catches async disable
```

---

### Week 1 — Thursday Jul 3 (P1) — READY TO POST

when a Playwright test fails in CI but passes locally, the trace file is your only evidence.

most teams download it, open it once, get overwhelmed, and fall back to console.log.

three things to check first:

the last screenshot before the failure. is the page in the state you expected? if the element isn't there, it's a timing problem, not a selector problem.

the network tab. did an API call return 500 or time out around the failure? if yes, it's not a Playwright issue.

the action timeline. how long did the failing action take versus your passing runs? if it's 10x slower, you have a race condition, not a flaky test.

the trace won't tell you why it failed. it shows you what the browser saw at the exact moment it failed. that's the difference between a 2-minute fix and a 2-hour debugging session.

what do you check first when a CI test fails locally?

#Playwright #SoftwareTesting

**Image:** screenshot of Playwright trace viewer — network tab and timeline visible. use a real failing test from your own CI if you have one.

---

### Week 1 — Friday Jul 4 (CONTRARIAN) — READY TO POST

80% code coverage is a vanity metric.

it tells you which lines ran during your test suite. it does not tell you whether anything meaningful was verified.

you can hit 80% with assertions that only check the page title. the metric is green. the build passes. nothing real was tested.

the problem: coverage tools measure execution, not verification. a line is "covered" if it ran without throwing an exception. that's a very low bar. it has nothing to do with whether the behavior is correct.

we ran a coverage audit last year. [X]% of our covered code had no meaningful behavioral assertion attached. the tests executed the lines and verified nothing. coverage number: high. actual confidence: fake.

coverage % is not useless. it tells you where you're definitely not testing. use it as a floor, not a ceiling. the ceiling should be something that reflects actual risk.

the metric that matters: how many of your last [N] production bugs would your current suite have caught before they shipped? run that audit once. 80% will never feel the same.

is your team tracking coverage because it's useful, or because it's measurable?

#SoftwareTesting #QualityAssurance

**Note:** replace [X] and [N] with real numbers before posting.
