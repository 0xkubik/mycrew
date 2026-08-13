# Decisions — mycrew

<!-- DECISIONS — what is settled about the product itself: the rules, constraints and ways of
     existing that give everything else its context. Not a capability and not a task — the frame the
     features are built inside, and the reasoning that closed each one.

     WHAT GOES HERE: a closed choice about the PRODUCT — one a person outside could notice: what it
     does, offers, forbids, charges for, or will never do. It belongs to no single feature and will
     still bind in a year.

     WHAT DOES NOT: a choice about the machinery — a language, a store, a protocol, a library, a way
     of running it — is technical and lives in ../design/decisions.md. A capability goes to
     features.md, work to be done to notes.md.

     SHAPE: `## P001 — <what was chosen, and over what where there was a real alternative>`. A
     heading that names a topic instead of a choice is a decision not yet made. Under it short `-`
     points only: why it won, what it was weighed against and what that would have cost, the known
     limit where it stops working, what would overturn it. Never prose. Heading and points together
     stay within 300 chars; what will not fit is two decisions.

     THE ID: `P` and three padded digits, running from the highest already taken. Permanent — never
     reused, never renumbered.

     NEVER DELETED: a decision that no longer holds stays, its heading marked `— superseded by P0NN`,
     and the choice replacing it is a new entry. The record of a wrong turn is worth more than a
     clean file. -->

## P001 — The product plane is three global files — features, notes, decisions — not one set per repo

- A feature's line and its detail were the same thing written twice.
- Split per repo, one feature was described piecewise in three places.
- Overturned if features.md stops being readable at a glance.

## P002 — docs splits in two: product/ is what the product is, design/ is how it is built

- Technical choices were landing beside product rules, so neither read cleanly.
- The id says which view: F, N and P for the product, T for the technical.
- Overturned if a third view appears that fits under neither.
