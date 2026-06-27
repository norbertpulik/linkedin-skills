# Voice Fingerprint — Preserving the user's voice while scrubbing

The humanizer is destructive by design. Every pass deletes or substitutes tokens. That's fine for AI tells. It's a bug for the user's actual voice.

This file lists the signals to preserve, even when they overlap with rules in `scrub-rules.md`.

---

## Preserve unconditionally (do NOT scrub these)

These are voice signatures, not AI tells. Leave them alone in every tier including `--mode all`.

| Pattern | Why it's voice, not AI |
|---|---|
| Lowercase sentence starts (`closed our seed on a tuesday...`) | Deliberate cadence cue. Capitalizing flattens the voice. |
| `..` as a soft pause | This is the humanizer's officially-blessed alternative to em dash. Removing it has nowhere to go. |
| Sentence fragments (`Worth it.`, `Every time.`, `Not even close.`) | Pass 2 ADDS fragments. Don't remove the ones already there. |
| Contractions (`don't`, `it's`, `you're`, `we're`) | Mandatory for natural rhythm. Scrubbing curly apostrophes is fine; expanding contractions is not. |
| First-person sensory detail (`my hands shook`, `the room went quiet`) | Pass 3 demands these. Never strip. |
| Specific numbers (`$47k`, `9:14am`, `47 days`) | Pass 3 demands these. Never strip. |
| Named entities (`HubSpot`, `Tuesday morning`, brand names) | Pass 3 demands these. Capitalize properly per non-negotiable rule. |
| Self-correction within a paragraph (`actually no`, `correction:`) | Burstiness signal. Real humans circle back. |

## SDET / practitioner terms — preserve unconditionally

These look like candidates for scrubbing but are the author's domain vocabulary. Never strip or substitute.

| Term / pattern | Why it stays |
|---|---|
| Tool names: Playwright, pytest, k6, WireMock, Postman, JUnit, Cypress, TestNG, Locust, Gatling, Vitest, Jest, Pact, Karate | Domain vocabulary. Replacing or dropping breaks credibility with the SDET audience. |
| CI platform names: GitHub Actions, Jenkins, CircleCI, GitLab CI, ArgoCD, Buildkite | Same as above. Never generalize to "the pipeline tool". |
| `flaky` / `flakey` / `flakiness` | Technical term for non-deterministic test failure. Not an AI tell. |
| Test-type adjectives: `e2e`, `unit`, `integration`, `contract`, `smoke`, `regression`, `canary` | Precision terms. Don't replace with "comprehensive" or spell out unless context demands it. |
| Abbreviations: `CI`, `CD`, `CI/CD`, `PR`, `SUT`, `AAA`, `BDD`, `TDD` | Native abbreviations in this author's domain. |
| Numbers with test-specific units: `87ms`, `3.2s`, `71% coverage`, `43 flakes`, `p95`, `p99` | Pass 3 demands these. Never strip; the unit is part of the meaning. |
| `false positive`, `false negative`, `coverage gap`, `test debt`, `test oracle` | SDET-specific concepts. Never flag as AI. |
| `quarantine` (as in quarantine a flaky test) | Domain term. Not the pandemic sense. Never replace with "isolate" or "remove". |

---

## Preserve when sample voice is provided

If the user passes optional `target_voice_samples` (their last 5-10 LinkedIn posts), extract:

1. **Sentence-length distribution.** If they routinely write 4-6 word sentences, don't force 12+ word "minimum lengths" on Pass 2.
2. **Vocabulary fingerprint.** Words they use 3+ times across samples are part of their voice — even if those words appear on the strict blacklist. Flag for user review rather than auto-substituting.
3. **Punctuation habits.** Some users use `...` instead of `..`, or unbroken comma chains. Match the dominant pattern.
4. **Opener patterns.** If they always start with a number (`47 days ago`, `$2M ARR`) or a name (`Jake said`), preserve that template.
5. **Closer patterns.** If they always close with a single fragment + period (no question), don't force a question CTA.

---

## Conflict resolution

When a scrub rule fires on a token that's also in the user's voice fingerprint:

| Tier | Behavior |
|---|---|
| Forensic | Always scrub. Forensic rules catch model leakage; if the user's voice fingerprint contains `oaicite` it's because they pasted AI output. |
| Strict | Flag for user review. Don't auto-substitute. The user gets to decide. |
| Aesthetic | Skip the rule entirely. Aesthetic rules already explicitly tolerate human-writer defenses. |

---

## How to build a voice fingerprint from samples (sketch)

```python
from collections import Counter
import re

def build_voice_fingerprint(samples: list[str]) -> dict:
    text = "\n".join(samples)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    return {
        "sentence_lengths": [len(s.split()) for s in sentences],
        "vocab_freq": Counter(re.findall(r"\b[a-z][a-z']{2,}\b", text.lower())),
        "starts_lowercase_pct": sum(1 for s in sentences if s and s[0].islower()) / max(len(sentences), 1),
        "uses_double_dot": ".." in text,
        "uses_triple_dot": "..." in text,
        "punctuation_freq": Counter(c for c in text if c in ".!?,;:"),
        "fragment_pct": sum(1 for s in sentences if len(s.split()) <= 4) / max(len(sentences), 1),
    }
```

The skill should call this on `target_voice_samples` before running Pass 1.

---

## Examples

### Example 1 — `..` as soft pause (preserve)

Input: `closed our seed.. then everything broke`

Wrong (scrubs the `..`): `closed our seed. then everything broke`

Right (preserve): `closed our seed.. then everything broke`

The `..` is on the explicit preserve list. Period substitution is for `--`, not `..`.

### Example 2 — lowercase start (preserve)

Input: `closed our seed on a tuesday morning at 9:14am`

Wrong (capitalizes): `Closed our seed on a Tuesday morning at 9:14am`

Right (preserve `closed`, capitalize `Tuesday`): `closed our seed on a Tuesday morning at 9:14am`

The non-negotiable rule says capitalize NAMES — Tuesday is a proper noun in date context, but the sentence-initial `closed` stays lowercase per voice rule.

### Example 3. Voice-fingerprint vocabulary collision (flag, don't substitute)

User samples contain `harness` 4 times across 6 posts (clearly part of their voice — they work in horse-training tech).

Strict tier scrub rule says: `harness → use`.

Right behavior: flag for user review. Output: `[VOICE-CONFLICT: 'harness' is in your voice fingerprint (4 uses in past samples) but matches strict-tier scrub. Keep or substitute?]`

---

## Don't fabricate

The non-negotiable rule (SKILL.md line: "Never introduce facts that weren't in the input") overrides voice-fingerprint matching. If a sample contains specific numbers, do NOT carry those numbers into a different post. Only use numbers the current input already supplies.
