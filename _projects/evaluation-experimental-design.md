---
layout: project
title: Evaluation and Experimental Design
description: Strategies to evaluate and test GenAI tools in psychiatry and behavioral science.
graphic: evaluation.svg
rank: 3

# Active projects in this area. `summary` and `people` are both optional — an
# entry with neither still renders as a named placeholder. `summary` is
# rendered as Markdown, so it can carry inline [links](https://example.com).
# Add `figure: <file>.png` to show something from images/figures/ alongside one.
projects:
  - name: Uncertainty in LLM psychiatric risk assessments
    people: Shevya Panda, Shinjini Bose
    summary: >-
      LLM outputs vary depending on which clinical details are presented. We
      audit four models across four prompt framings and show that adding
      clinically irrelevant information significantly shifts predicted
      hospitalization risk and output variability, underscoring the need for
      governance around these models before clinical deployment.

  - name: Language drift in LLM responses
    # TODO: originally described as a separate evaluation project, but drift is
    # also central to NAVIGATOR ("tuning process maps even as concepts drift").
    # Fold this in there if it is the same work.
    people: Rosa Jahankhah
    summary: >-
      Detecting drift in the language of LLM responses over time, and what that
      drift implies for evaluating deployed systems.

# Papers are NOT listed here. They live in _data/publications.yml; an entry
# joins this page's "Selected work" by setting
# `area: evaluation-experimental-design`.
---

Generative AI tools are entering psychiatry and behavioral science faster than evaluation practice can keep up. We design strategies to test these systems rigorously, covering validity, reliability, fairness across populations, and fitness for clinical or research use.

Our goal is evaluation methods that help labs and clinics decide when a tool is ready, where it fails, and how to measure improvement over time.
