---
layout: project
title: Evaluation and Experimental Design
description: Strategies to evaluate and test GenAI tools in psychiatry and behavioral science.
graphic: evaluation.svg
rank: 3

# Active projects in this area. `summary` and `people` are both optional — an
# entry with neither still renders as a named placeholder.
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

  - name: Emotion as a mediator of theory of mind in LLMs
    people: Ivan Chulo
    summary: >-
      Investigating the internal mechanisms by which LLMs infer user beliefs,
      and finding that improvements are driven by patterns matching emotional
      processing rather than logical reasoning. These insights help explain how
      AI systems behave when used in supportive or administrative roles in
      behavioral health.

  - name: Language drift in LLM responses
    # TODO: originally described as a separate evaluation project, but drift is
    # also central to NAVIGATOR ("tuning process maps even as concepts drift").
    # Fold this in there if it is the same work.
    people: Rosa Jahankhah
    summary: >-
      Detecting drift in the language of LLM responses over time, and what that
      drift implies for evaluating deployed systems.

# Papers are listed newest first. `file` points at images/papers/.
papers:
  - title: "Reliability Auditing for Downstream LLM Tasks in Psychiatry: LLM-Generated Hospitalization Risk Scores"
    authors: Shevya Panda, Shinjini Bose, Ananya Joshi
    venue: arXiv, 2026
    file: pandya-arxiv-2026.pdf
---

Generative AI tools are entering psychiatry and behavioral science faster than evaluation practice can keep up. We design strategies to test these systems rigorously, covering validity, reliability, fairness across populations, and fitness for clinical or research use.

Our goal is evaluation methods that help labs and clinics decide when a tool is ready, where it fails, and how to measure improvement over time.
