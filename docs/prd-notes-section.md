# PRD: AI/Data-Science Notes Section + Design Upgrade

## Problem Statement

Joseph Lam-Weil is a Statistics PhD and postdoc whose personal website (jlamweil.github.io) is a static academic homepage built on a 2017 HTML5 UP template. It has not been updated in years: social links are placeholders, the template shows its age with its jQuery-dependent sidebar and dated visual styling, and there is no way to publish the short-form technical notes on AI, data science, and machine learning research that the owner wants to share.

The owner needs a lightweight publishing workflow:
- Write short posts in Markdown with code snippets, tags, and dates
- Publish programmatically from the command line
- The site should feel modern, clean, and professional
- Notes should feel intentionally short — small lessons, not polished essays

## Solution

Add a **Notes** section to the personal website and refresh the site's visual design. The approach:

1. **Keep the existing homepage** but clean it up — remove unused template boilerplate, placeholder social links, stale duplicate assets, and the commented-out demo section. Add a "Notes" link to the sidebar nav and a prominent link from the homepage to the notes section.

2. **Add Jekyll** to the GitHub Pages site. Jekyll is natively supported by GitHub Pages and enables Markdown posts with front matter, templating via Liquid layouts, RSS via plugins, and tag infrastructure — all without a heavy build toolchain.

3. **Design a fresh look for Notes pages** that is visually consistent with the existing site (same Lato typography, same Source Code Pro for code, same `#8ba3cb` accent palette) but feels cleaner and more modern. Pages are standalone (no sidebar) with a top navigation bar.

4. **Create a CLI script** that scaffolds a new post from templates with today's date, slug generation, front matter, and template selection.

5. **Update the README** to document the note-writing workflow.

## User Stories

1. As a site visitor, I want to see a Notes section from the homepage, so that I know the author publishes technical content.
2. As a site visitor, I want to browse a list of all notes with titles, dates, excerpts, and tags, so that I can find content relevant to me.
3. As a site visitor, I want to click on a note and read its full content, so that I can learn from the author's experience.
4. As a site visitor, I want code snippets in notes to be clearly styled and readable, so that I can understand technical examples.
5. As a site visitor, I want to see tags on each note, so that I can quickly gauge the topic.
6. As a site visitor, I want to see the publication date on each note, so that I know how recent the content is.
7. As a site visitor, I want the notes pages to work well on my mobile phone, so that I can read on the go.
8. As a site visitor, I want the reading experience to be clean and distraction-free, so that I focus on the content.
9. As a site visitor, I want to navigate back to the homepage from any notes page, so that I can explore the rest of the site.
10. As a site owner, I want to create a new note by running a single command, so that I publish quickly without manual file scaffolding.
11. As a site owner, I want the new-note command to generate front matter (title, date, slug, tags) automatically, so that I don't have to remember the format.
12. As a site owner, I want the new-note command to refuse to overwrite existing files, so that I don't accidentally lose content.
13. As a site owner, I want to write notes in plain Markdown, so that I don't need to learn a custom format.
14. As a site owner, I want to choose from post archetypes (concept, mistake, pattern, paper-note), so that my posts have consistent structure.
15. As a site owner, I want to write the note, commit, and push to publish, so that the workflow is as simple as possible.
16. As a site owner, I want the site to still build correctly on GitHub Pages after all changes, so that I don't break my existing site.
17. As a site owner, I want duplicate/obsolete asset directories cleaned up, so that the repository is maintainable.
18. As a site visitor, I want the website to have a modern, clean visual design, so that it feels professional and current.
19. As a site owner, I want the README to document how to create and publish notes, so that I remember the workflow months from now.
20. As a site visitor, I want an RSS feed for the notes section, so that I can subscribe and follow new content.
21. As a site visitor, I want Open Graph metadata on note pages, so that sharing links on social media shows a preview card.
22. As a site owner, I want the site to load fast without unnecessary JavaScript dependencies, so that the experience is snappy.
23. As a site owner, I want placeholder social links (Twitter, Facebook, Instagram — all `href="#"`) removed or replaced with actual profiles, so that the site looks maintained.
24. As a site visitor, I want an estimated reading time on each note, so that I know the time commitment before reading.

## Implementation Decisions

### Architecture: Add Jekyll to Existing Static Site

**Decision**: Add Jekyll to the existing GitHub Pages site rather than replacing the entire site or keeping it pure static HTML.

**Rationale**: GitHub Pages natively runs Jekyll on user pages. Adding `_config.yml` and `Gemfile` requires no new infrastructure. Jekyll processes Markdown posts into HTML, handles Liquid templating, and supports RSS via plugins — exactly what this project needs. The existing `index.html` (no front matter) will be copied verbatim by Jekyll with zero disruption.

**Constraints**:
- The existing `index.html` must remain intact and function identically
- Jekyll must not interfere with the existing page
- No heavy CMS, no external build pipeline

### Homepage: Preserve + Clean Up

**Decision**: Keep the existing "Read Only" HTML5 UP template for the homepage but clean it up:
- Remove the commented-out `#five` (Elements) demo section (~330 lines of boilerplate)
- Remove placeholder social links (Twitter, Facebook, Instagram) — keep GitHub and Email
- Remove stale duplicate asset directories (`assets2/`, `images2/`, `index_files2/`)
- Remove unused jQuery scripts (main.js depends on scrolly/scrollex which won't be needed for notes pages)
- Add "Notes" link to the sidebar navigation (without `.scrolly` class — it links to `/notes/`)
- Add a content link on the homepage to the notes section

### Notes Pages: Standalone Clean Layout

**Decision**: Notes pages (both the `/notes/` landing page and individual `/notes/:slug/` pages) use a standalone layout with a simple horizontal navigation bar, NOT the existing sidebar scroll layout. This avoids reproducing the heavy jQuery-dependent sidebar on every note page.

**Design tokens** (matching existing site):
- Font: Lato (body), Source Code Pro (code)
- Colors: `#888` text, `#777` headings, `#8ba3cb` accent
- Container max-width: 45em (~720px) matching the existing `.container` width
- Code blocks: dark `#555` background, white text, `5px` border radius
- No jQuery dependency on notes pages

**Design improvements** (design upgrade):
- Cleaner vertical spacing and typographic hierarchy
- Removing the dated fixed-sidebar layout for notes pages
- Subtle tag styling, clean date display
- Reading time estimate
- Mobile-first responsive (existing breakpoints)
- Reduced visual noise compared to the current template

### URL Structure

**Decision**: Post URLs follow `/notes/:slug/` format.

- `jekyll-permalink: /notes/:slug/` in `_config.yml`
- Post files named `YYYY-MM-DD-slug.md` in `_posts/`

### Post Format

**Decision**: Posts are Markdown files with YAML front matter:

```yaml
---
title: "Validation leakage is often invisible"
date: 2026-05-22
slug: validation-leakage
tags:
  - data-science
  - machine-learning
  - validation
excerpt: "A model that performs suspiciously well may not be good."
---
```

The `slug` field in front matter matches the filename-derived slug (explicit for clarity).

### Post Archetypes

**Decision**: Four archetype templates in `_templates/` — concept, mistake, pattern, paper-note — each with a structured section outline.

The `new_note.py` script accepts `--type concept|mistake|pattern|paper-note` to select the template.

### Script Interface

**Decision**: Single `python scripts/new_note.py` command:

```
python scripts/new_note.py "Title" --tags tag1 tag2 [--type concept]
```

Behavior:
- Generate today's date
- Derive slug from title (lowercase, ASCII-normalized, spaces to hyphens, remove special chars)
- Select template (default: concept)
- Generate front matter
- Write to `_posts/YYYY-MM-DD-slug.md`
- Refuse to overwrite existing file
- Print created file path

This is a deep module — simple, stable interface that rarely changes.

### RSS Feed

**Decision**: Use the `jekyll-feed` plugin (official GitHub Pages-supported plugin) to generate `/feed.xml` automatically. No custom RSS code needed.

### Tag Pages

**Decision**: Postpone full tag pages. Display tags on individual posts and the notes listing. Create tag pages only if they're trivially generated by Jekyll (via `jekyll-archives` or manual). Do not block the core implementation on this.

### Open Graph / SEO

**Decision**: Add Open Graph tags (`og:title`, `og:description`, `og:type`, `og:url`) to the post layout. Use `jekyll-seo-tag` if it's on the GitHub Pages allowlist, otherwise inline the meta tags manually.

## Testing Decisions

- **What makes a good test**: The core script (`scripts/new_note.py`) should be tested for correct front matter generation, file naming, slug derivation, and overwrite prevention. The site's correctness is verified by a successful `jekyll build` producing the expected output.
- **Modules to test**: `scripts/new_note.py` — unit tests for slug generation, date formatting, front matter rendering, and file-not-found/overwrite handling.
- **Prior art**: Standard Python test patterns with `unittest` or `pytest`. No existing tests in the repo.
- **Integration test**: Run `jekyll build` and verify the output directory has the expected `notes/` directory and post HTML files.

## Out of Scope

- **Full site redesign**: The homepage keeps its existing template. Only the notes section gets a new layout. A site-wide redesign is future work.
- **Comment system**: No Disqus, utterances, or other commenting.
- **Search**: No site search.
- **Newsletter signup**: No email collection.
- **Analytics**: No tracking or analytics.
- **Social share buttons**: No share widgets (LinkedIn, Twitter, etc.) unless trivially simple.
- **Custom domain**: No CNAME or DNS configuration.
- **Dark mode**: Not in scope for this iteration.
- **MathJax/LaTeX**: Mathematical notation if already supported; otherwise not in scope for v1.
- **AI-generated content**: Posts are human-written; no AI generation pipeline.

## Further Notes

- The existing `README.txt` should be converted to `README.md` with the documentation additions.
- The `LICENSE.txt` (CC BY 3.0, from the template) should remain.
- The `Gemfile` must use only plugins on the [GitHub Pages dependency list](https://pages.github.com/versions/) to avoid build failures.
- The existing `index_fichiers/` directory stays as the active asset source (it's what `index.html` references).
- All created files should follow the existing no-emoji, no-fluff, professional tone.
- Priority order for implementation: (1) Jekyll setup → (2) Notes pages → (3) Navigation → (4) Styling → (5) Script → (6) Templates → (7) Example posts → (8) README → (9) Nice-to-haves → (10) Verification.
