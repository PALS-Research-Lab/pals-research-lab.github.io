---
layout: project
title: Statistical Monitoring and Measurement
description: Developing new metrics, measurements, and methods to monitor for critical events related to psychiatry and mood disorders towards improved patient care.
graphic: monitoring.svg
rank: 1

# Active projects in this area. `summary` and `people` are both optional — an
# entry with neither still renders as a named placeholder.
# Add `figure: <file>.png` to show something from images/figures/ alongside one.
projects:
  - name: NAVIGATOR
    people: Minseo Choi, Rosa Jahankhah, Ronald Deng, with Michael Rudow
    figure: navigatorwebsite.jpg
    link: https://navigator.pals-lab.org
    link_label: navigator.pals-lab.org
    summary: >-
      A public repository that surfaces mental-health benchmark examples where
      AI models show the highest uncertainty or disagreement with compliance
      rules. Behavioral health benchmarks carry erroneous labels and drift over
      time, so NAVIGATOR separates two sources of uncertainty: a multi-agent
      system constrained by a directed acyclic graph simulates an
      organization's process map to surface context-dependent (aleatoric)
      uncertainty, while Monte Carlo simulations at each agent surface model
      gaps (epistemic uncertainty). Internally validated labels feed back into
      the compliance monitoring system, which re-evaluates the datasets to
      identify the next set of high-uncertainty examples. The system now covers
      more than 60 open-source datasets, improves labeling accuracy by 16%, and
      reduces human review by up to 85x.

  - name: Patient heterogeneity
    people: Rhea Makkuni, Ram Chitti
    summary: >-
      Why individuals sharing a psychiatric diagnosis can differ in their
      underlying pathology and treatment trajectories, and how computational
      systems can be designed to reflect and adapt to that heterogeneity.

  - name: Reliable self-harm risk screening
    people: Meghana Karnam
    summary: >-
      Multi-agent LLM pipelines are being used to assess self-harm risk, but
      common evaluation approaches do not indicate when a decision is reliable
      or how errors accumulate across agents. We give these pipelines a
      statistical footing with agent-level confidence bounds, bandit-based
      adaptive sampling, and regret guarantees, cutting the false positive rate
      by 40% against single-agent models without losing recall.

  - name: Hospitalization forecasting for decision support
    people: Rhea Makkuni
    summary: >-
      Public health experts must make real-time resource decisions, such as
      expanding hospital bed capacity, from projected hospitalization trends.
      We evaluate direct LLM forecasting, classical time-series models, and a
      context-augmented hybrid across 60 US counties, judging them on bias and
      lead-lag alignment rather than error alone, because the goal is
      operational decision-making.

# Papers are listed newest first. `file` points at images/papers/.
papers:
  - title: "Context-Aware Hospitalization Forecasting Evaluations for Decision Support using LLMs"
    authors: Rhea Makkuni, Ananya Joshi
    venue: arXiv, 2026
    file: makkuni-arxiv-2026.pdf

  - title: Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems
    authors: Meghana Karnam, Ananya Joshi
    venue: arXiv, 2026
    file: karnam-arxiv-2026.pdf
---

Clinical psychiatry depends on timely detection of change: relapse risk, treatment response, and other events that matter for patient care. Our work builds measurement frameworks and monitoring methods that can surface these signals reliably from real-world data streams.

We focus on metrics that are statistically sound, clinically interpretable, and practical to deploy alongside existing workflows, so monitoring systems reduce noise rather than add alert fatigue.
