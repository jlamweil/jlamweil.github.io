# Joseph Lam-Weil

Personal website built with [HTML5 UP](https://html5up.net/) "Read Only" template and [Jekyll](https://jekyllrb.com/) (via GitHub Pages).

## Repository structure

This public repo contains the website machinery only. Lesson content lives in a private repository.

| Repo | Visibility | Contents |
|---|---|---|
| `jlamweil.github.io` | **Public** | Layouts, CSS, config, homepage, scripts, templates |
| `lessons-content` | **Private** | `_posts/` and `_drafts/` with lesson Markdown files |

A GitHub Action merges content from the private repo during each build, then deploys to GitHub Pages.

## Writing lessons

The site supports a short-form lessons section at `/lessons/` for AI, data science, and machine learning content.

### Clone both repos for local work

```bash
git clone git@github.com:jlamweil/jlamweil.github.io
git clone git@github.com:jlamweil/lessons-content
ln -s ../lessons-content/_posts _posts
```

### Create a new lesson

```bash
python scripts/new_note.py "Your lesson title" --tags tag1 tag2
```

Optional flags:
- `--type concept\|mistake\|pattern\|paper-note` — selects a template structure (default: concept)
- `--level human\|deep\|full` — scaffolds only human intuition, AI/deep detail, or both (default: full)
- `--dry-run` — preview the file that would be created without writing

This creates a Markdown file in `_posts/` with today's date and a derived slug. The script refuses to overwrite existing files.

### Publish a lesson

Content goes through the private repo:

```bash
# From the lessons-content repo:
cd ../lessons-content
git add _posts/
git commit -m "Add lesson on validation leakage"
git push
```

The GitHub Action picks up the change and deploys within ~2 minutes.

### Where posts live

| Directory | Purpose |
|---|---|
| `_posts/` (in lessons-content) | Published lessons (filename: `YYYY-MM-DD-slug.md`) |
| `_drafts/` (in lessons-content) | Draft lessons |
| `_templates/` (in this repo) | Archetype templates for different lesson types |

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

### Reading depth

Each lesson has two layers in a single page:

| Layer | Audience | Content |
|---|---|---|
| **Human** (top) | Casual reader | Intuition, experience, rule of thumb |
| **Deep dive** (below divider) | Technical reader | Formal details, implementation, edge cases |

Scaffold with `--level human` or `--level deep` to focus on one layer.

## Development

To build locally:

```bash
docker run --rm -v $(pwd):/site -w /site jekyll/jekyll:latest jekyll build
```

The site outputs to `_site/`.

## License

Template: [CC BY 3.0](https://html5up.net/license) — HTML5 UP
Content: © Joseph Lam-Weil
