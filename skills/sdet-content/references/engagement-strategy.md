# Engagement Strategy — Audience Building Phase

At under 500 followers, commenting on other people's posts drives more growth than posting. LinkedIn shows your comments to the post author's audience. One sharp comment on a post with 500 likes can bring 20-50 new followers in 24 hours. Posting to 61 followers cannot.

**Rule:** 5-10 targeted comments per day, every day. This is the primary growth lever until 500 followers.

---

## Who to target

### Tier 1 — Playwright / test automation niche (highest conversion)

Comment on posts from these account types — their audience is your exact buyer:

- **Playwright team and contributors** — Microsoft DevTools team members, Playwright GitHub contributors who post on LinkedIn
- **Popular QA/automation creators** — anyone in test automation with 2k+ followers posting about Playwright, Selenium, Cypress, WebdriverIO (competing tools = same audience)
- **SDET/QA conference speakers** — SeleniumConf, QA Global Summit, TestCon, EuroSTAR speakers who are active on LinkedIn
- **"QA tips" creators** — accounts that post daily automation tips, even if surface-level. Their audience wants depth you provide.

### Tier 2 — AI in testing (high engagement, growing niche)

- Creators posting about Copilot, Claude, or AI code generation for developers
- DevOps/platform engineers posting about CI/CD quality
- Engineering managers posting about test automation ROI or quality investment decisions

### Tier 3 — Broad software engineering (reach, lower conversion)

Use sparingly. High impressions but followers convert at lower rate.

---

## Finding target posts

Daily: search LinkedIn for these terms and filter by "Past 24 hours":
- `Playwright`
- `test automation`
- `flaky tests`
- `CI/CD quality`
- `AI testing`

Sort by Top posts. Comment on anything with 50+ likes in your niche.

---

## What makes a comment grow your audience

A comment that brings followers does three things:
1. Adds a specific detail not in the original post (tool name, number, failure mode)
2. Demonstrates you know more than the author about a specific subtopic
3. Ends with a question that makes the author want to reply

When the author replies to your comment, LinkedIn notifies their followers. That's a second push from their audience to yours.

**Use `linkedin-comment-drafter` for every Tier 1 comment.** Apply full SDET voice rules. A mediocre comment on a high-reach post is worse than no comment — it signals low quality to new profile visitors.

### Comment quality bar

| Good | Bad |
|---|---|
| `Playwright's toBeEnabled() would have caught this. the button was visible but disabled during async validation. one assertion different.` | `Great post! This is so true about testing.` |
| `we hit the same issue in our Jenkins pipeline. the fix was isolating the Docker network per worker, not per run.` | `I agree, flaky tests are a real problem in CI.` |
| `interesting — are you running contract tests at the API boundary, or only e2e?` | `Thanks for sharing!` |

---

## Daily rhythm

**Morning (before 9 AM):**
- Post your own content on Tue/Thu (7:30-9:00 AM)
- Comment on 3-5 Tier 1 posts from the last 24 hours

**Midday:**
- Reply to every comment on your own posts (see first-hour protocol)
- Comment on 2-3 more Tier 1/2 posts

**Evening (optional):**
- 2-3 more comments on posts that are gaining traction

**Weekly:**
- Run `linkedin-hook-extractor` on the top 2-3 performing posts in your niche — learn what hooks are working
- Run `linkedin-engager-analytics` on your own best post — see who engaged and follow/comment on their content

---

## First-hour protocol (when you publish a post)

The first 60 minutes after posting determine whether LinkedIn pushes the post further.

1. **Reply to every comment within 30 minutes.** Even a one-line reply counts as engagement.
2. **Pin a comment yourself** immediately after posting: add the Playwright Production Checklist link as the first comment, not in the post body.
3. **Go comment on 3-5 other posts** right after publishing. This keeps you active in the algorithm's eyes during the push window.
4. **Do not edit the post** after publishing. LinkedIn resets the push when you edit.

---

## Profile: convert visitors to followers

Every comment you leave sends traffic to your profile. The profile must convert that visit to a follow.

Run `linkedin-profile-optimizer` before scaling comments. Priority fixes for your goal:

1. **Headline** must say what you do + who you help + what result. Not just your job title.
   - Target format: `Senior SDET | Playwright/TypeScript | Helping QA teams ship faster with less flake`
2. **Featured section** must have the Playwright Production Checklist as item 1. This is the funnel entry point.
3. **About section** hook (first 265 chars before "see more") must speak directly to the SDET audience.
4. **Custom URL** — claim `linkedin.com/in/norbert-pulik` now if not already done.

---

## Growth checkpoints

| Followers | What changes |
|---|---|
| 61 → 200 | Comments are your primary lever. Post quality matters but reach is limited. |
| 200 → 500 | Algorithm starts recognising your content type. Post reach improves. Keep commenting. |
| 500 → 1000 | Posts start pulling in followers on their own. Comments become reinforcement, not primary. |
| 1000+ | Product launch window. Audience is large enough to convert to buyers. |
