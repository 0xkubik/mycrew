---
name: ask-me
description: "Use when the product's recorded features need to be drawn out to clarity — the loop at the product root: work through features from most to least significant, asking a batch of questions per feature and its existing gaps. Their answers settle and file the feature, then you move on. You ask, they decide; you never answer for them, never pitch. Ends only when they stop."
argument-hint: "[a feature to start on — or nothing to work through the whole product]"
---

# ask-me — bring recorded features to clarity

The human knows the product; features are recorded but under-thought and under-written. You work through
them **most significant first**, asking a batch per feature, and file what they affirm in that feature's
home. Run at the **product root**. Nothing here is filed per repo.

## Step 1 — load what governs the plane

Load the product rules (`rules/working-with-backlog.md`) — they decide where an affirmed answer lands
and in what shape. Then read what is already captured: `backlog milestone list`, `backlog doc list`, and
the product `CLAUDE.md`. No backlog yet → send the human to `/product-init`. Context comes from the
human's words, never from scanning the code.

## Step 2 — order the features

Sort the recorded features from **most to least significant**: weigh how central each is to the product's
value and how far it is from done, against how **under-documented** it is. A significant feature with an
empty or thin spec ranks highest — that is where the human's words matter most. Present the order and
start on the top of the list.

## Step 3 — question one feature in a batch

For the current feature, read its recorded spec, then ask **several questions at once** through
`AskUserQuestion` — each one closing a real gap in that feature: what it does, its limits and edges,
its mechanics, what it must never do. Each option is a real position this human could hold, put in their
language, never one obvious answer beside three made to be rejected. Every answer that adds or alters
the feature is filed in its doc, in their words, that turn; what changes nothing is filed nowhere.

**Include in this same batch, every time, the routing question:** move on to the next feature, or
continue with this one?

## Loop

Repeat step 3. If they say **continue**, go deeper on the same feature the next batch. If **move on**,
take the next feature in the ranked order. A picked option is their answer and it is theirs — take it,
file what it changes, and don't make them re-say it. Never offer a way out of deciding; never pitch
(that is `propose-idea`'s job); never wrap up — the loop ends only when the human stops it.
