# Joseph Lam-Weil

Personal website built with [HTML5 UP](https://html5up.net/) "Read Only" template and [Jekyll](https://jekyllrb.com/) (via GitHub Pages).

## Writing lessons

The site supports a short-form lessons section at `/lessons/` for AI, data science, and machine learning content.

### Create a new lesson

```bash
python scripts/new_note.py "Your lesson title" --tags tag1 tag2
```

Optional flags:
- `--type concept|mistake|pattern|paper-note` — selects a template structure (default: concept)
- `--dry-run` — preview the file that would be created without writing

This creates a Markdown file in `_posts/` with today's date and a derived slug. The script refuses to overwrite existing files.

### Publish a lesson

```bash
git add .
git commit -m "Add note on your note title"
git push
```

GitHub Pages builds and deploys automatically on push to `master`.

### Where posts live

| Directory | Purpose |
|---|---|
| `_posts/` | Published lessons (filename: `YYYY-MM-DD-slug.md`) |
| `_drafts/` | Draft lessons (not published on GitHub Pages) |
| `_templates/` | Archetype templates for different lesson types |

### Front matter fields

| Field | Required | Description |
|---|---|---|
| `title` | yes | Post title |
| `date` | yes | Publication date (`YYYY-MM-DD`) |
| `slug` | yes | URL slug (lowercase, hyphenated) |
| `tags` | yes | List of topic tags |
| `excerpt` | no | Short description for listings |

### Template types

- `concept` — for explaining a useful idea
- `mistake` — for documenting a common error
- `pattern` — for reusable techniques
- `paper-note` — for research paper takeaways

## Development

To build locally:

```bash
docker run --rm -v $(pwd):/site -w /site jekyll/jekyll:latest jekyll build
```

The site outputs to `_site/`.

## License

Template: [CC BY 3.0](https://html5up.net/license) — HTML5 UP
Content: © Joseph Lam-Weil
