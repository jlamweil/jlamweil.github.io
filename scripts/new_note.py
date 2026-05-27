#!/usr/bin/env python3
"""Scaffold a new Jekyll Markdown post from an archetype template."""

import argparse
import os
import re
import sys
import unicodedata
from datetime import date


_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_templates")
_POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_posts")

_VALID_TYPES = {"concept", "mistake", "pattern", "paper-note"}


def derive_slug(title: str) -> str:
    """Convert a title string into a URL-safe slug.

    Steps: lowercase → ASCII-normalise → spaces to hyphens →
    remove non-[a-z0-9-] → collapse hyphens → strip edges.
    """
    slug = unicodedata.normalize("NFKD", title.lower())
    slug = slug.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug


def read_template_sections(ptype: str) -> str:
    """Return the body section-headers (everything after front matter) from a template file."""
    template_path = os.path.join(_TEMPLATE_DIR, f"{ptype}.md")
    if not os.path.isfile(template_path):
        print(f"Error: template '{ptype}' not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(template_path, encoding="utf-8") as fh:
        content = fh.read()

    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"Error: template '{ptype}' is missing valid front matter (---)", file=sys.stderr)
        sys.exit(1)

    return parts[2].lstrip("\n")


def build_post_content(title: str, slug: str, today_str: str, tags: list[str], ptype: str) -> str:
    """Assemble the full Markdown content for the new post."""
    body = read_template_sections(ptype)
    tags_yaml = ", ".join(tags) if tags else ""

    front_matter = (
        "---\n"
        f'title: "{title}"\n'
        f"date: {today_str}\n"
        f"slug: {slug}\n"
        f"tags: [{tags_yaml}]\n"
        "excerpt: \n"
        "---\n"
        "\n"
    )
    return front_matter + body


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new Jekyll Markdown post from an archetype template."
    )
    parser.add_argument("title", help="Post title (required)")
    parser.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="Space-separated list of tags (e.g. --tags ai data-science)",
    )
    parser.add_argument(
        "--type",
        dest="ptype",
        default="concept",
        choices=sorted(_VALID_TYPES),
        help="Archetype template to use (default: concept)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing any file",
    )
    args = parser.parse_args()

    title = args.title.strip()
    if not title:
        print("Error: title is required and cannot be empty.", file=sys.stderr)
        sys.exit(1)

    ptype = args.ptype
    if ptype not in _VALID_TYPES:
        print(
            f"Error: invalid type '{ptype}'. Must be one of: {', '.join(sorted(_VALID_TYPES))}",
            file=sys.stderr,
        )
        sys.exit(1)

    slug = derive_slug(title)
    today_str = date.today().isoformat()
    filename = f"{today_str}-{slug}.md"
    filepath = os.path.join(_POSTS_DIR, filename)

    os.makedirs(_POSTS_DIR, exist_ok=True)

    if os.path.exists(filepath):
        print(f"Error: {filepath} already exists — refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        print(f"Would create: {os.path.join('_posts', filename)}")
        print(f"  title: {title}")
        print(f"  slug:  {slug}")
        print(f"  date:  {today_str}")
        print(f"  tags:  {args.tags}")
        print(f"  type:  {ptype}")
        return

    content = build_post_content(title, slug, today_str, args.tags, ptype)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)

    print(f"Created: {os.path.join('_posts', filename)}")


if __name__ == "__main__":
    main()
