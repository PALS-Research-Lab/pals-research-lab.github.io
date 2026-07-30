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

  - name: Detecting drift in chatbot input
    people: Rosa Jahankhah
    summary: >-
      The people talking to a mental-health chatbot do not all talk the same
      way: teenagers and older adults use different words and phrasing for the
      same concerns, and the input a deployed system sees shifts over time. We
      are working on detecting that shift and on mathematical models that
      quantify how much drift has occurred.

  - name: How mental health providers use chatbots
    people: Ariel Kim
    summary: >-
      A survey of mental health providers on whether and how they use chatbots
      in practice, and how they feel about them, to ground evaluation criteria
      in what clinicians actually need from these tools.

# Papers are NOT listed here. They live in _data/publications.yml; an entry
# joins this page's "Selected work" by setting
# `area: evaluation-experimental-design`.
---

Generative AI tools are entering psychiatry and behavioral science faster than evaluation practice can keep up. We design strategies to test these systems rigorously, covering validity, reliability, fairness across populations, and fitness for clinical or research use.

Our goal is evaluation methods that help labs and clinics decide when a tool is ready, where it fails, and how to measure improvement over time.
