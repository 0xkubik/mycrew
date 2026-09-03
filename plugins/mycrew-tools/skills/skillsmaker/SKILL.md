---
name: skillsmaker
description: "Use when writing or rewriting a SKILL.md. Asks what the skill should do, picks a template, fills it in."
argument-hint: "<the skill to write or rewrite>"
---

# skillsmaker — build a skill by asking

You are building a skill. Ask the user what it should do, pick the right template, fill it in with
their answers. Don't write anything until you have enough to fill the template.

## Step 1: what does the skill do?

Ask:

- What should this skill do? (one sentence)
- When should it be loaded? (the trigger)
- What does the caller pass in? (arguments, or nothing)

## Step 2: pick a template

Based on the answer, pick one:

- **One-liner** — simple constraint, no steps, no sections. Just a demand and where it stops.
  → `template-oneliner.md`
- **Guide** — standing instructions, bullets organized by topic. For "how to work" skills.
  → `template-guide.md`
- **Pipeline** — ordered steps to carry out. For "do this thing" skills with a clear sequence.
  → `template-pipeline.md`
- **Questionnaire** — asks the user questions before acting. For skills that need input to decide.
  → `template-questionnaire.md`

Ask the user which one fits if it is not obvious.

## Step 3: fill the template

Read the template file. Fill in each `<placeholder>` with the user's answers. Write dry, factual
language — no "leverage", no "ensure", no "it is crucial to". Keep it under 40 lines.

## Step 4: write it

Write the filled skill to `skills/<name>/SKILL.md`. Show the user what you wrote and stop.
