# Decisions — mycrew

<!-- Every settled choice about the product and the reasoning that closed it, one file for the whole
     product, newest last. The `P`-id is permanent. The heading is the decision; under it short `-`
     points only — why it won, what it was weighed against, where it stops working, what would
     overturn it. Heading and points together stay within 300 chars — what will not fit is two
     decisions. Never prose. A decision that no longer holds is marked superseded, never deleted. -->

## P001 — The product plane is three global files — features, notes, decisions — not one set per repo

- A feature's line and its detail were the same thing written twice.
- Split per repo, one feature was described piecewise in three places.
- Overturned if features.md stops being readable at a glance.

## P002 — docs splits in two: product/ is what the product is, design/ is how it is built

- Technical choices were landing beside product rules, so neither read cleanly.
- The id says which view: F, N and P for the product, T for the technical.
- Overturned if a third view appears that fits under neither.
