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
| Fri Jul 4 | CONTRARIAN | 80% code coverage is a vanity metric. it tells you which lines ran, not which behaviors were verified. | F10 contrarian | #SoftwareTesting #QualityAssurance | drafted ✓ |

## Week 2 (Jul 7 – Jul 11)

| Day | Pillar | Angle | Format | Hashtags | Status |
|---|---|---|---|---|---|
| Tue Jul 8 | P6 | does it make sense to start with QA in 2026? yes — but skip manual testing entirely. learn Playwright and CI from day one. | counterintuitive claim | #SoftwareTesting #QualityAssurance | drafted ✓ |
| Thu Jul 10 | P1 | we ran Playwright with --workers=4. 23 tests failed. they all passed alone. 2 days debugging, 4-line fix. shared auth state. | incident | #Playwright #SoftwareTesting | drafted ✓ |
| Fri Jul 11 | P6 | CONTRARIAN: I have no QA certifications. I've reviewed hundreds of CVs. ISTQB has never been the reason someone got hired. | F10 contrarian | #SoftwareTesting #QualityAssurance | drafted ✓ |

## Week 3 (Jul 14 – Jul 18)

| Day | Pillar | Angle | Format | Hashtags | Status |
|---|---|---|---|---|---|
| Tue Jul 15 | P3 | 3 years testing SCADA before web. the skills that transferred: none of the tools, all of the thinking. | practitioner observation | #SoftwareTesting #QualityAssurance | drafted ✓ |
| Thu Jul 17 | P1 | we inherited 200 XPath selectors. 15-30 broke every release. replaced with data-testid in one sprint. zero structure failures in 8 months. | before-after | #Playwright #SoftwareTesting | drafted ✓ |
| Fri Jul 18 | CAROUSEL | how I structure a Playwright project for a Banking CI pipeline. slides: folder layout, fixture design, network layer, CI config, reporting. | carousel (PDF) | #Playwright #SoftwareTesting | not drafted |

**Week 3 note — video test:** record a 60-90 sec screen recording of Playwright trace viewer catching a real failure. post as a standalone video on any day. LinkedIn is pushing video hard. low production value is fine.

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

---

### Week 2 — Tuesday Jul 8 (P6) — READY TO POST

I became a Senior SDET in 6 years without a computer science degree.

not a flex. a data point.

I get asked regularly whether it still makes sense to start a career in QA in 2026. yes — but not the way most people start it.

the traditional path is: manual testing first, automation later. that path made sense 10 years ago. in 2026 it's the path most likely to be automated away. the jobs that are disappearing are the ones that don't require you to write code.

the path I'd take today: skip manual testing entirely. learn Playwright. learn how CI works. understand what a flaky test actually means in a pipeline context. get comfortable reading a failed build before you're comfortable writing a perfect test.

the first job is harder to get this way. every job after that is easier.

if you're switching into QA from a different background, what's the biggest thing slowing you down?

#SoftwareTesting #QualityAssurance

---

### Week 2 — Thursday Jul 10 (P1) — READY TO POST

we ran Playwright with --workers=4 for the first time.

23 tests failed. they all passed when run alone.

the debugging took 2 days. the fix took 4 lines.

the problem: our tests shared a single user account. parallel workers were logging in and out on top of each other. one test's logout was another test's authentication error.

the fix: one unique test user per worker, scoped in a fixture.

this is the most common reason parallel Playwright suites fail silently in CI. if your tests pass locally and break at --workers=4, check shared state first: auth, database records, test data.

where does shared state cause the most pain in your Playwright suite?

#Playwright #SoftwareTesting

---

### Week 2 — Friday Jul 11 (P6 CONTRARIAN) — READY TO POST

I have no QA certifications.

I've reviewed hundreds of CVs and interviewed dozens of QA candidates over 6 years. ISTQB has not once been the reason someone got hired. not once the reason someone was rejected.

the certification industry in QA exists because hiring managers without a technical background need a proxy for skill. the proxy doesn't measure what it claims to measure.

what actually gets a QA candidate hired: a portfolio of tests written against a real codebase. evidence that they understand why something is tested, not just how. one specific example of a bug they caught that wouldn't have been caught otherwise.

I'm not saying certifications are worthless. I'm saying they're worth significantly less than the time and money spent on them implies.

what got you your first QA job?

#SoftwareTesting #QualityAssurance

---

### Week 3 — Tuesday Jul 15 (P3) — READY TO POST

I spent 3 years testing SCADA industrial control systems before moving to web application testing.

the skills that transferred: almost none of the tools. all of the thinking.

in SCADA there is no browser. no DOM. no element locators. you write assertions against register values, state transitions, and timing windows measured in milliseconds. "is this button visible?" is not a concept that exists in a PLC control loop.

what transferred: the discipline of knowing exactly what you're testing and why. SCADA failures don't produce a flaky test. they produce a safety incident. that changes how carefully you think about coverage, determinism, and test isolation.

the thing I notice in web QA that SCADA taught me to avoid: testing what you can see in the UI and calling it done. the behavior that matters is often one layer below what's visible on screen.

what domain has shaped how you think about testing the most?

#SoftwareTesting #QualityAssurance

---

### Week 3 — Thursday Jul 17 (P1) — READY TO POST

we inherited a Playwright suite with 200 XPath selectors.

every release broke between 15 and 30 of them. the fix cycle: CI fails, find the selector, update it, re-run. 2-3 hours per release.

we replaced them all with data-testid attributes over one sprint. not because XPath is wrong — because XPath selectors are coupled to DOM structure. the moment a developer moves a div or wraps a component, the selector breaks.

data-testid survives restructuring because it's tied to behavior, not layout. a developer has to explicitly remove the attribute to break the test.

migration took one sprint. selector maintenance dropped to near zero. we haven't had a structure-related failure in 8 months.

what selector strategy does your team actually use in production?

#Playwright #SoftwareTesting
