---
name: linkedin-engagement-monitor
description: Read-side LinkedIn analytics. (1) Detect which of your comments earned author replies (6-24h warm-reply window). (2) Pull likers/commenters on any post, segment by ICP and seniority for outbound. Uses Apify, no login. Triggers on "who liked my post", "author replied", "engagers report". Detects only; draft the reply with linkedin-reply-handler.
---

# LinkedIn Engagement Monitor

Two read-side workflows, one skill.

1. **Thread monitoring.** Track which of your comments earned author replies, draft timely follow-ups, flag the 6-24h warm-reply window where thread momentum is highest.
2. **Engager analytics.** Pull every liker and commenter on any post, group them by ICP fit, surface peer / aspirational / prospect tiers, and feed the result into your DM or outreach queue.

Both workflows depend on `APIFY_TOKEN`. Without it, fall back to user-paste.

## When to use

- Daily: "What threads need follow-up today?"
- After posting a batch of comments: "Check back in 6 hours"
- When an author replied personally: "Draft the response"
- After publishing a post: "Who actually engaged? Are they ICP?"
- Before a campaign: "Pull the last 5 viral posts in my niche, group their commenters by company size"

## Input

- Mode 1 (thread monitoring): your LinkedIn handle (last path segment of profile URL).
- Mode 2 (engager analytics): one or more LinkedIn post URLs.
- Optional for both: ICP definition (target titles, company size, industry).

## Mode 1. Thread monitoring

Output: see `references/mode1-thread-monitoring.md` for the daily report table, warm-thread preview shape, weekly roll-up, and a sample run.

### Steps (Mode 1)

1. **Fetch user's recent comments.** If `APIFY_TOKEN` is set, call `lib.ApifyClient.fetch_user_recent_comments(username=<your-handle>, result_limit=30)`. Each item already includes the parent post body, post URL, post author, and reaction stats. If `APIFY_TOKEN` is not set, ask the user to list (or paste) the URLs of comments they've posted in the last 72h.
2. **For each comment posted in last 72h:** check the parent post's comment tree (use `fetch_post_comments(post_id=..., scrape_replies=True)`) for:
   - Replies to the user's comment
   - Whether the author posted any of those replies
   - Timestamps (time since user's comment, time since latest reply)
3. **Classify stage:**
   - Hot (<6h): author just replied. Respond within 90 min for max thread momentum
   - Warm (6-24h): the warm-reply window. Author replies most happen here
   - Cool (24-72h): still respondable but lower velocity
   - Dormant (>72h): don't reply in thread. Consider DM
4. **Draft responses** for warm threads using `linkedin-reply-handler`.
5. **Flag suspicious patterns:**
   - Author replied but also deleted someone else's comment (author is actively moderating, tread carefully)
   - Commenter is in thread self-promoting (your reply shouldn't engage them)
6. **DM routing:** if thread is dormant but the author engaged meaningfully, draft a DM that references the thread specifically.

### warm-reply window

Named after the 2026-04 data point: a CEO replied to Serge's comment 22h after the original post. Reply-rate distribution: 0-6h 70%, 6-24h 25% (higher quality), >24h rare. Follow-up timing: 0-6h reply respond within 90 min; 6-24h within 2h; >24h within 4h before it goes cold. See `references/thread-timing.md` for the full matrix.

## Mode 2. Engager analytics

Output: see `references/mode2-engager-analytics.md` for the engager roster, tier breakdown, action lists, and a sample run.

### Steps (Mode 2)

1. **Fetch engagers.** Call `lib.ApifyClient.fetch_post_engagers(post_url=<url>, max_items=100)`. Returns a list of dicts with `type` ("commenters" | "likers"), `name`, `subtitle` (job title + company), `url_profile`, `content` (comment text if commenter), `datetime`. Cost is roughly $0.005 per engager-record.
2. **Parse subtitle into structured fields.** The `subtitle` typically reads "Director at Acme Corp" or "Founder & CEO at a SaaS company". Extract: title, company, seniority bucket (IC / Manager / Director / VP / C-suite / Founder).
3. **Score ICP fit.** Use the user's supplied ICP rules:
   - Title match (regex or keyword list)
   - Company size proxy (look up via the user's CRM if integrated, else mark Unknown)
   - Industry match (parse company name + subtitle keywords)
4. **Assign tier.**
   - Peer: founder / operator at similar-stage company in same niche
   - Aspirational: senior leader (Director+) at larger company in adjacent niche
   - Prospect: title in ICP target list AND company in ICP target list
   - Other: no match
5. **Produce action lists.**
   - Follow back: peers with active posting (heuristic: appears as author in `fetch_user_recent_comments` of any team member)
   - Comment-drop targets: aspirational tier
   - DM-able: prospect tier, with a one-line DM opener referencing the specific post they engaged with ("Saw you reacted to <post angle>. Curious. Are you currently <ICP problem>?")
6. **Optional cross-post analysis.** If the user supplied multiple post URLs, deduplicate engagers and flag people who engaged with 2+ posts (highest-intent signal).

## Inbound-quality signals (apply to both modes)

High-quality = follow up: founder/operator title, company in ICP, active posting history, >10 mutual 2nd-degree connections, prior thoughtful comments on user's posts.

Low-quality = skip: generic praise, template language ("I'd love to hop on a quick call"), sales/agency profile with no operator history, same comment copy-pasted across many creators.

## Hard rules

- Never reply to a reply later than 72h after the thread's last turn. Switch to DM.
- Never chain 3+ replies under one comment (thread spam).
- If the author deleted their reply, do not reply. They reconsidered.
- Don't DM a warm thread before first replying publicly (skips a step).
- Don't DM a prospect on the same day they engaged with your post. Wait 24-72h to avoid the "thirsty" pattern.
- Don't run engager analytics on posts you didn't write or aren't tracking with permission. The data is technically public but high-volume scraping of someone else's audience reads as creepy.

## Cost accounting

| Action | Apify call | Cost (free tier) |
|---|---|---|
| Daily thread sweep (1 user, ~30 comments) | `fetch_user_recent_comments` once | $0.005 |
| Per-warm-thread context | `fetch_post_comments(scrape_replies=True)` | $0.005 each |
| Engager analytics on one post (50 engagers) | `fetch_post_engagers(max_items=50)` | $0.25 |
| Engager analytics on one post (200 engagers) | `fetch_post_engagers(max_items=200)` | $1.00 |

A typical creator running this skill 5 days/week with 1 engager-analytics run/week stays well under the $5 free monthly credit.

## Files

- `SKILL.md` — this file
- `references/mode1-thread-monitoring.md` — Mode 1 output spec and sample run
- `references/mode2-engager-analytics.md` — Mode 2 output spec and sample run
- `references/thread-timing.md` — the timing matrix with examples (Mode 1)

## Related skills

- `linkedin-reply-handler` — drafts the actual follow-up message for warm threads
- `linkedin-comment-drafter` — drafts the initial comment that starts threads
