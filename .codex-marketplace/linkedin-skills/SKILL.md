---
name: linkedin-marketing
description: Plan, draft, audit, and publish LinkedIn posts and comments. Use when the user wants to write a viral LinkedIn post, draft a comment or reply on any LinkedIn post URL, audit a draft against 2026 algorithm heuristics, remove AI tells, extract hook formulas from viral posts, or plan a week of content. User provides post/comment URLs, skill drafts content, user approves, then returns a copy-paste block.
---

# LinkedIn Marketing Skills

A bundle of 10 focused skills for LinkedIn content ops in 2026. Each skill is single-purpose, follows the draft → approval → copy-paste pattern.

## When to use this bundle

- **Writing a viral post** → use `linkedin-post-writer`
- **Commenting on someone else's post** → use `linkedin-comment-drafter`
- **Replying to a comment** (yours or someone else's) → use `linkedin-reply-handler`
- **Reviewing a draft before publishing, removing AI tells, scoring AI emoji density, defending a flagged rule, or running 5 AI detectors in parallel** → use `linkedin-humanizer` (rewrite + `--mode audit` pre-publish review; folds in the former post-audit, emoji-detector, rules-explainer, and detector-tester sub-tools)
- **Extracting a hook formula from a viral post** → use `linkedin-hook-extractor`
- **Planning a week of LinkedIn content** → use `linkedin-content-planner`
- **Tracking which of your comments got author replies** → use `linkedin-thread-monitor`
- **Analyzing who liked / commented on any post (audience segmentation)** → use `linkedin-engager-analytics`
- **Auditing / rewriting a LinkedIn profile** → use `linkedin-profile-optimizer`
- **Running an employee advocacy program across a marketing team** → use `linkedin-employee-advocacy`

## Core pattern

Every action-taking skill follows three steps:

1. **Parse the input.** User provides a LinkedIn URL (post or comment). The skill uses `lib/url_parser.py` to extract the post URN and any comment ID.
2. **Draft the content.** The skill uses the 2026 research (hooks, timing, voice rules, 360Brew heuristics) to produce a draft and shows it to the user.
3. **Wait for approval.** The user replies with "post", "yes", or suggests edits. Only after explicit approval does the skill return the content as a copy-paste block with the target URL.

## Prerequisites

**Two tiers — pick one.**

### 🟢 Tier 0 — Draft only (default, no setup)

The skills work out of the box. No API keys, no signup. Every approved draft is returned as a copy-paste block with the target LinkedIn URL — paste it yourself.

### ⚫ Tier 2 — Build your own poster (advanced)

Prefer to auto-post? Ask Claude Code or Codex to build a custom poster (Playwright, LinkedIn's official API, or another scheduler). Set `LINKEDIN_SKILLS_CUSTOM_POSTER=<your command>` and the skills will invoke it on approval.

### Optional: Apify (read-side LinkedIn fetching)

Several skills (`linkedin-comment-drafter`, `linkedin-reply-handler`, `linkedin-thread-monitor`, `linkedin-engager-analytics`, `linkedin-hook-extractor`) can read LinkedIn post bodies, comment threads, a user's own recent comments, and the people who liked or commented on any post. They use the Apify platform when an `APIFY_TOKEN` is set; otherwise they ask you to paste the relevant text.

1. Sign up free: **https://console.apify.com/sign-up** (free tier ships with $5/month of credit, enough for ~1,000 post fetches or ~1,000 comment-thread fetches).
2. Generate a token: Console → Settings → Integrations.
3. Drop into `.env`:
   ```
   APIFY_TOKEN=apify_api_...
   ```

Actors used (all no-cookies, public, no LinkedIn login required):

| Use case | Actor | Approx cost |
|---|---|---|
| Post body by URL | `supreme_coder/linkedin-post` | $1 / 1,000 |
| Comments + replies on a post | `apimaestro/linkedin-post-comments-replies-engagements-scraper-no-cookies` | $5 / 1,000 |
| Your own recent comments | `apimaestro/linkedin-profile-comments` | $5 / 1,000 |
| Likers + commenters on any post | `scraping_solutions/linkedin-posts-engagers-likers-and-commenters-no-cookies` | $5 / 1,000 |

The thin client lives at `lib/apify_client.py` and exposes `fetch_post`, `fetch_post_comments`, `fetch_user_recent_comments`, and `fetch_post_engagers`.

## Voice rules (baked into every skill)

1. No em dashes (`—`), en dashes, or double dashes. Biggest AI tell.
2. Use `..` as soft pause when mid-sentence rhythm calls for it.
3. Capitalize personal names, company names, product names, and tool names (Playwright, pytest, GitHub Actions). Lowercase tools read as unfamiliar with the space.
4. Sentence starts can be lowercase (natural practitioner voice), but names and tools inside are always capitalized.
5. Avoid AI vocabulary: `leverage`, `fundamentally`, `streamline`, `harness`, `delve`, `unlock`, `foster`.
6. Avoid hollow SDET phrases: "ensure quality", "comprehensive test coverage", "quality culture", "robust test suite", "shift-left" without specifics.
7. Name the tool, the metric, or the failure mode. "we added tests" is noise. "we added 40 Playwright specs covering the checkout flow" is a comment worth reading.
8. Specific numbers beat adjectives — `71% coverage` beats `significant improvement`.
9. For comments on third-party posts, don't name-drop your own product — describe the capability instead.
10. LinkedIn posts: 900–1,300 chars sweet spot. Comments: 200–350 chars.
11. Hook lives in the first 210 chars (before "… see more" on mobile).

(Canonical reference: `references/voice-rules.md`. See also `references/hook-formulas.md` and `references/algorithm-heuristics.md`.)

## How URLs map to URNs

LinkedIn ships three post URN types (the library handles all three):

| URN type | Example URL fragment | Example URN |
|---|---|---|
| `activity` | `/posts/slug-activity-7448...-XX` | `urn:li:activity:7448...` |
| `share` | `/posts/slug-share-7449...-XX` | `urn:li:share:7449...` |
| `ugcPost` | `/feed/update/urn:li:ugcPost:7447...` | `urn:li:ugcPost:7447...` |

Comment URLs:
```
/feed/update/urn:li:activity:POST_ID?commentUrn=urn%3Ali%3Acomment%3A%28activity%3APOST_ID%2CCOMMENT_ID%29
```
The library decodes the commentUrn fragment and returns both `post_urn` and `comment_id`.

## Known gotchas

- LinkedIn flattens reply threads to 2 levels. When replying to a reply, pass the **top-level** comment URN as `parentComment`, not the reply's URN.
- A post URN returned by `url_parser` may be `activity` when the canonical URN is actually `ugcPost`. Resolve via `lib.ApifyClient.fetch_post_comments(post_id=...)` and read the canonical URN from any existing comment's `comment_url`.

## Resources

- [Apify console](https://console.apify.com) — manage actors, tokens, and usage for the read layer
- `lib/apify_client.py` — thin Python client used by every skill

## Acknowledgments

Algorithm insights via arXiv 2501.16450 (360Brew) and AuthoredUp 2026 reach data.
