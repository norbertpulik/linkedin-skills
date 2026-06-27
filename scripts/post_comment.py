#!/usr/bin/env python3
"""CLI: draft a LinkedIn comment for copy-pasting.

Usage:
    python scripts/post_comment.py "<POST_URL>" "<COMMENT_TEXT>" [--reaction INTEREST] [--dry-run]

Flow:
    1. Parse URL to URN
    2. Show approval card
    3. Print copy-paste block on confirmation
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# Make repo importable without install
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import parse_linkedin_url, render_approval_card


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("url")
    ap.add_argument("message")
    ap.add_argument("--reaction", default="INTEREST",
                    help="LIKE | PRAISE | EMPATHY | INTEREST | APPRECIATION | ENTERTAINMENT")
    ap.add_argument("--dry-run", action="store_true", help="Preview only")
    ap.add_argument("--reply-to", default=None,
                    help="Parent comment ID for threaded replies (optional)")
    args = ap.parse_args()

    parsed = parse_linkedin_url(args.url)
    if not parsed.get("post_urn"):
        print(f"✗ Could not parse URN from URL: {args.url}", file=sys.stderr)
        return 2

    post_urn = parsed["post_urn"]

    parent_comment_urn = None
    if args.reply_to:
        parent_comment_urn = f"urn:li:comment:({post_urn},{args.reply_to})"

    card = render_approval_card(
        kind="reply" if parent_comment_urn else "comment",
        preview_text=args.message,
        target_url=args.url,
        reaction_type=args.reaction,
        extra_context={
            "post_urn": post_urn,
            "parent_comment": parent_comment_urn or "(top-level)",
        },
    )
    print(card)
    print()

    if args.dry_run:
        print("(dry-run — nothing to do)")
        return 0

    answer = input("Copy text above and paste on LinkedIn? [yes/no]: ").strip().lower()
    if answer not in {"yes", "y", "post"}:
        print("Cancelled.")
        return 0

    print(f"\n✅ Copy the comment text above and paste it at:\n{args.url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
