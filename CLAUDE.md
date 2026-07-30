# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Jekyll 4.3 static site for the PALS Research Lab (Johns Hopkins, AI for Psychiatry). Deployed via GitHub Pages at the custom domain in `CNAME` (`pals-lab.org`). There is no test suite, no linter, and no build step beyond Jekyll.

## Commands

```bash
bundle install                    # first-time / after Gemfile changes
bundle exec jekyll serve          # dev server with live reload at http://localhost:4000
bundle exec jekyll build          # one-off build into _site/
python app.py                     # optional: Flask preview of an existing _site/ on :5000
```

`app.py` is a small Flask wrapper that serves the already-built `_site/` and resolves pretty URLs (`/people` → `people/index.html`). It does **not** build the site — run `jekyll build` first. It exists because `_config.yml` sets no `url`/`baseurl` and all asset/nav links are absolute (`/style.css`, `/research`), so previews must be served from the site root.

Every request path goes through `_resolve()`, which gates on `werkzeug.utils.safe_join` plus a `realpath` containment check against `_site/`. Keep new routes behind it — a hand-rolled `startswith("..")` check does **not** stop absolute paths (`GET /C:/Windows/win.ini` read arbitrary files before this was fixed). The Werkzeug debugger is off unless `FLASK_DEBUG=1`, since it exposes an interactive code-execution console.

## Architecture

**Content model.** Three content sources, all rendered through `_layouts/default.html`:

- `_people/*.md` — one file per person, front matter only (no body). Fields: `name`, `role`, `photo` (bare filename resolved against `/images/people/`), `website` (bare host, no scheme — the template prepends `https://`), `tier`, `rank`. `output: false` in `_config.yml`, so these render only inside `people.html`.
- `_projects/*.md` — research areas. `output: true`, permalink `/research/:name/`, layout `project`. `rank` controls ordering; `description` is reused on the home page, `/research`, and the detail page header. `graphic` names an SVG in `images/research/`. A `projects:` list holds the individual projects running under that area — each entry takes `name` (required), plus optional `people`, `summary`, and `figure` (a file in `images/figures/`). Every optional field is guarded in `_layouts/project.html`, so a `name`-only entry renders as a clean placeholder rather than an empty paragraph.

**Media folders.** `images/papers/` (papers, posters, PDFs) and `images/figures/` (figures, plots, diagrams) are drop targets for lab content; each has a README describing naming. Nothing in them is rendered automatically — a file only appears once it is referenced from a `projects:` entry, a post, or a person.

Both READMEs are listed in `exclude:`. That only works because `README.md` was removed from `include:` — Jekyll's `include` overrides `exclude`, so while it was listed there the contributor READMEs were published no matter what `exclude` said. Don't add it back.
- `_posts/YYYY-MM-DD-slug.md` — news and blog entries. Permalink is pinned to `/:year/:month/:day/:title/` in `_config.yml` specifically so that adding a `category` does not change post URLs.

**Person routing in `people.html`.** People are partitioned by `tier` front matter, not by directory: `pi` becomes the featured PI block (`role == "PI"` is still honoured for older entries), `postdoc` gets its own section, `alumni` goes to the Alumni section, and everyone else lands in the student/collaborator grid. Each section auto-hides when empty. Cards render through `_includes/person-card.html`, which handles the initials fallback for a missing `photo` and the optional `topics` (research interests) and `now` (alumni destination) lines.

Both grids are sorted with `sort_natural: "name"` — that is, by first name as displayed. They used to be shuffled twice (Liquid `shuffle` at build time, then again client-side in `default.html`); both were removed when the lab asked for a stable alphabetical order, so re-adding a shuffle anywhere would silently undo it.

**News vs. blog split.** Both live in `_posts`. Posts set `category: news` or `category: blog`; `news.html`, `blog.html`, `index.html`, and `_layouts/post.html` all branch on `post.categories contains '...'`. A post with neither category appears nowhere in the archives, and `post.html` treats anything not tagged `blog` as News for its breadcrumb/back-link. Existing posts are all `news`.

Post `date:` front matter must be ISO `YYYY-MM-DD` and must match the date in the filename. A front-matter `date` overrides the filename for both permalink and ordering, so a mismatch silently publishes the post at the wrong URL — this happened once with a copy-pasted `DD/MM/YYYY` date and is why the convention is now enforced by hand at review time.

**Nav highlighting.** Each top-level page sets `nav:` in its front matter (`home`, `research`, `news`, `blog`, `people`, `contact`); `default.html` compares it against the link list. Project detail pages have no `nav`, so `default.html` special-cases `page.collection == "projects"` to light up Research.

**Sponsor band.** `_data/sponsors.yml` drives the "Supported By" strip that `default.html` renders directly above the footer, so adding a funder is a data edit, not a template edit. Two constraints are easy to break:

- The band's background is **white on purpose**. Several of these logos ship as opaque white canvases rather than transparent PNGs, so any tinted background renders them as visible rectangles. For the same reason the dark footer cannot host them — `IBM.png` is pure black and disappears against `--hopkins-blue`.
- Logo files are **pre-trimmed to their ink bounds**, and `height` in the YAML is a per-logo optical size, not a uniform one. Aspect ratios run from 6.2:1 (Allegheny County) to 1.3:1 (NVIDIA); a single shared height would make the wide wordmarks dominate. New logos should be trimmed of their transparent/white padding first (several originals were 65–87% padding), then sized with `height ≈ sqrt(3000 / aspect_ratio)`. The grid is a fixed 4-up (2-up under 720px) because 8 logos left to `flex-wrap` orphan one on a second row.

`url` is blank for every entry — the template only wraps a logo in a link when it is set, so filling one in activates the link.

**Styling and JS.** A single hand-written `style.css` (no Sass pipeline despite the `.sass-cache` gitignore entry), with Hopkins brand colors as CSS custom properties in `:root`. All page JS lives inline at the bottom of `_layouts/default.html`: Lenis smooth scroll (CDN), the team shuffle, and an IntersectionObserver that adds `.is-visible` to `.reveal` elements. Any new section that should animate in needs the `reveal` class — without it the section still renders, but content inside a `.reveal` that never intersects stays hidden, so verify scroll behavior after adding sections. Everything is gated behind `prefers-reduced-motion`.

**Scratch files.** `design-candidates.html` and `og-candidates.html` are standalone mockups with no front matter — Jekyll copies them verbatim. They are not part of the site's navigation; don't treat them as templates.
