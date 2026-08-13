# Decisions — mycrew

<!-- Every settled choice about the product and the reasoning that closed it, one file for the whole
     product, newest last. The `D`-id is permanent. The heading is the decision, dated with the day it
     was settled; under it short `-` points only — why it won, what it was weighed against, where it
     stops working, what would overturn it. Never prose. A decision that no longer holds is marked
     superseded, never deleted. -->

## D000 — The product plane is three global files — features, notes and decisions — not one set per sub-project · 2026-08-13

- A feature's line and its detail are the same thing said twice when they live in two files; the
  detail now sits under the feature it belongs to.
- Splitting specs per sub-project meant one feature described piecewise in three places, with nowhere
  holding the whole of it.
- The ceiling: `features.md` grows without bound, which is why a feature is capped at ten points and
  one that needs more is two features.
- Overturned if the file becomes too large to read at once despite the cap.
