"""Detect which publishing backend is configured and format user-facing messages.

The skills support two tiers:

  TIER 0 — manual (default, zero setup)
    No credentials in env. Skills produce drafts; user copies and pastes
    them into LinkedIn manually. Works for anyone, any setup.

  TIER 2 — diy (advanced)
    `LINKEDIN_SKILLS_CUSTOM_POSTER` set to a command or module path the
    user has built themselves (e.g. via Claude Code or Codex). Skills delegate
    publishing to that custom tool.

`active_backend()` picks the highest-privilege available. `manual_mode_message()`
is what skills show the user when no backend auto-posts.

`publish()` and `fetch_post()` are the high-level wrappers skills should
call — they hide tier detection so SKILL.md files don't need to repeat
the two-branch dispatch.
"""
from __future__ import annotations
import json
import os
import shlex
import subprocess
from typing import Any, Literal, Optional

BackendName = Literal["manual", "diy"]
PublishKind = Literal["comment", "reply", "post"]


def active_backend() -> BackendName:
    """Return the active publishing backend.

    Priority: diy > manual.
    """
    if os.getenv("LINKEDIN_SKILLS_CUSTOM_POSTER"):
        return "diy"
    return "manual"


def manual_mode_message(draft_text: str, target_url: str, kind: str = "comment") -> str:
    """Format the copy-paste output for the draft-only tier."""
    return f"""✅ Draft approved. Copy the text below and paste it as a {kind} on LinkedIn:

```
{draft_text}
```

**Target URL:** {target_url}
"""


def publish(
    kind: PublishKind,
    draft_text: str,
    target_url: str,
    **kwargs: Any,
) -> Optional[dict]:
    """Dispatch a draft to the active backend.

    Routes to manual (copy-paste) or diy (custom poster) based on
    `active_backend()`. The Publora tier has been removed; publishing
    is intentionally manual-only by default.

    Args:
        kind: "comment" | "reply" | "post".
        draft_text: The approved draft body.
        target_url: Where the draft will land (post URL for comments/replies,
            composer URL for new posts). Used in manual-mode copy-paste output.
        **kwargs: Backend-specific payload for the diy tier.

    Returns:
        - manual:  dict with `{"mode": "manual", "message": <copy-paste block>}`.
        - diy:     dict with `{"mode": "diy", "returncode": int, "stdout": str, "stderr": str}`.
        Returns None only if the chosen backend cannot run.
    """
    backend = active_backend()

    if backend == "manual":
        return {
            "mode": "manual",
            "message": manual_mode_message(draft_text, target_url, kind=kind),
        }

    if backend == "diy":
        cmd = os.getenv("LINKEDIN_SKILLS_CUSTOM_POSTER")
        if not cmd:
            return None
        payload = {
            "kind": kind,
            "draft_text": draft_text,
            "target_url": target_url,
            **kwargs,
        }
        argv = shlex.split(cmd) + [kind, target_url]
        proc = subprocess.run(
            argv,
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            timeout=120,
        )
        return {
            "mode": "diy",
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }

    raise RuntimeError(f"unknown backend: {backend!r}")


def fetch_post(url: str, **kwargs: Any) -> Optional[dict]:
    """Fetch a LinkedIn post body via Apify, or return None if unavailable.

    Skills should treat `None` as "ask the user to paste the post text".
    This keeps every skill's fetch path a single line:

        post = lib.fetch_post(url) or ask_user_to_paste(url)

    Args:
        url: Any LinkedIn post URL shape (activity / ugcPost / share).
        **kwargs: Forwarded to `ApifyClient.fetch_post` (e.g. `force_refresh`).

    Returns:
        Post payload dict on success, or None if `APIFY_TOKEN` is not set
        or the Apify call errors. Callers should fall back to user-paste.
    """
    if not os.getenv("APIFY_TOKEN"):
        return None
    try:
        from .apify_client import ApifyClient, ApifyError

        client = ApifyClient()
        return client.fetch_post(url, **kwargs)
    except Exception:
        return None


if __name__ == "__main__":
    print(f"Active backend: {active_backend()}")
    if active_backend() == "manual":
        print("\nExample manual message:")
        print("-" * 60)
        print(manual_mode_message(
            draft_text="This is a great draft for LinkedIn.",
            target_url="https://www.linkedin.com/posts/someone-activity-123",
            kind="comment",
        ))
