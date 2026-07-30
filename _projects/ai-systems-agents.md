---
layout: project
title: AI Systems and Agents for Psychiatry
description: Developing the theory and building multi-agent systems related to improving clinical processes for patients, clinicians, and hospitals.
graphic: agents.svg
rank: 2

# Active projects in this area. `summary` and `people` are both optional — an
# entry with neither still renders as a named placeholder.
# Add `figure: <file>.png` to show something from images/figures/ alongside one.
projects:
  - name: PhippsBot
    people: Synthia Wang, King Shi, Amanda Li, Ariel Kim, Jonathan Ivey, Michelle Lu
    figure: phippsbot.png
    summary: >-
      An agentic workflow for psychiatric intake. A preregistered pilot study
      compares how psychiatrists and LLMs conduct intake interviews with
      simulated patients, measuring clinical information gathering, safety
      concern detection, and empathic communication. Clinicians complete a
      20-minute text-based intake; LLM interviews are time-matched to the mean
      clinician duration so the two can be compared fairly.

  - name: Caregiver
    people: Arushi Acharya, Peiyong Lin
    summary: >-
      How AI and LLMs can help caregivers and clinicians make safer,
      patient-specific medication decisions for older adults, focusing on
      polypharmacy, mental health, and data gaps in geriatric psychiatric care.

  - name: Synthetic patient interactions for clinician training
    people: Guan Gui, Amanda Li, with Jacob Taylor and Peter Zandi
    summary: >-
      Psychiatric intake practices vary widely, which complicates efforts to
      compare interviews or evaluate training. We build a structured
      synthetic-patient framework that produces repeatable, controlled intake
      interactions, and pair it with a question-selection benchmark drawn from a
      bank of 655 clinician-authored questions.

  - name: Visual context scaling for clinical language models
    # TODO: Rahul Gorijavolu is listed on this project in the End-of-Year
    # snapshot but has no entry in _people/. Add one and his name will link up
    # with the rest of the team.
    people: Rahul Gorijavolu, Jay Pratap
    summary: >-
      Visual context scaling offers a path to reducing inference-time costs in
      clinical GenAI. Across clinical vignettes, early results show roughly 3x
      token compression while maintaining accuracy on an operative-note
      extraction task.

# Papers are listed newest first. `file` points at images/papers/.
papers:
  - title: Adaptive Question Selection from a Large Question Bank for Field Recovery in Conversational Psychiatric Intake
    authors: Guan Gui, Peter Zandi, Jacob Taylor, Ananya Joshi
    venue: arXiv, 2026
    file: gui-arxiv-2026.pdf
---

Psychiatry involves complex, multi-step processes across patients, clinicians, and institutions. We develop theory and systems for multi-agent and generative AI workflows that can support those processes while remaining constrained, auditable, and aligned with clinical goals.

This includes agent architectures, process maps, and system designs that make AI assistance safer and more useful in psychiatric and behavioral health settings.
