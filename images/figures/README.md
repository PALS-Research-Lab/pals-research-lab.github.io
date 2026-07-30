# Figures

Drop figures, plots, system diagrams, and screenshots from the lab's work here.
Jekyll copies this folder verbatim, so anything placed here is reachable at
`/images/figures/<filename>`.

## What works well

These are meant to be shown at roughly 600–900px wide on a light background:

- **Prefer** PNG or SVG for diagrams and plots — they stay crisp when scaled.
- **Trim whitespace** around the content first. Several sponsor logos in this
  repo arrived with 65–87% padding, which made them render tiny next to
  properly-cropped neighbours.
- **Avoid figures with baked-in captions** where possible; captions are better
  as page text so they stay searchable and translatable.

## Naming

Use `project-what-it-shows.<ext>`, lowercase, hyphenated, no spaces:

```
navigator-inference-pipeline.png
caregiver-polypharmacy-flow.svg
phippsbot-architecture.png
```

## How these get used

Nothing here is displayed automatically. Tell Claude which project a figure
belongs to and it will place it on that research area's page.
