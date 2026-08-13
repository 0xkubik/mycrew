---
name: design-view
description: "Use for anything about the product's technical view — the shape of the system and the choices it is built on. Not WHAT the product does (that's product-view / what-to-do) but HOW it is built: one living LikeC4 tree in docs/design/model.c4 at the product root, and beside it docs/design/decisions.md, the settled technical choices with the reasoning that closed them. The human and the chief own both; workers build to them. Rules and concepts, not a fixed procedure."
user-invocable: false
---

# design-view — how the product is built

`docs/design/` holds **how the product is built**. Two files, and nothing else belongs in either:

| File | Holds | Ids |
| --- | --- | --- |
| `docs/design/model.c4` | the shape — what talks to what at run time | — |
| `docs/design/decisions.md` | the settled technical choices, and why | `T001` |

**Never what the product is.** That is the **product view** — `docs/product/` beside it, by
`mycrew-product:product-view`: `features.md`, `notes.md` and `decisions.md`. **The line between them:**
a product decision is one a person outside could notice — what the product does, offers, forbids or
charges for. A technical decision is one about the machinery — the language, the store, the protocol,
the library, the thing deliberately not used. Nobody reading the product would ever see it.

**The human and the chief own both — a worker never writes to either.** A worker reads them and builds to them; when the
work needs the shape to move or shows a choice is wrong, it says so in its report and you make the
move here, then re-dispatch.

# The tree — `docs/design/model.c4`

**One living tree** at the product root, spanning every sub-project. LikeC4 syntax is in
**`mycrew-tools:likec4`** — load it before editing.

## Rules & concepts — non-negotiable
- **One axis: runtime interaction.** The tree answers a single question — *what talks to, calls, or
  depends on what, at run time.* A node is whatever independently **exists and interacts when the system
  runs**: a running service or process, a deployed contract, a datastore, an external system. An edge is
  a runtime interaction (calls, reads, publishes, forwards). Anything else does not belong.
- **Code structure is a different axis — OUT.** Inheritance / `extends` / `is`, interface and ABI files,
  helper and math libraries, mixins, abstract bases, individual functions, source groupings (folders,
  `src/*` dirs, packages) describe *how the source is organized to be reused* — never nodes, never edges.
  **Litmus:** an edge you'd label `extends` / `inherits` / `is`, or a node that is *abstract, not
  deployed, or a stateless helper lib* — leave it OUT. codegraph already maps the code; a code-structure
  picture is a **separate generated diagram**, never hand-carved into this tree. A significant
  implementation *fact* (an RNG source, a standard like ERC-7535, a gasless path) lives as a component's
  **description or a relationship** — never as its own node.
- **One file, its own LikeC4 project.** The whole product's model lives in that **one** `model.c4` — never
  scatter `.c4` files across the sub-projects or write architecture anywhere else. Beside it sits a
  `likec4.config.json` with a unique `name` (e.g. `{ "name": "<product>", "title": "…" }`) — create it if
  missing. Without it LikeC4 merges every config-less `.c4` in the workspace into one default project, and
  a sibling product's model bleeds into your index.
- **A tree, root → leaves.** The root is a high-level overview of the **whole product**; the
  **sub-projects are its first level**, one node per repo. Each node nests the finer *interacting* parts
  inside it (LikeC4 component nesting), down to the finest interacting unit that still matters for
  reasoning. Deeper means a smaller unit of the **same** axis — never a jump to another (code structure,
  type hierarchy, deployment topology). Structure, not a flat list.
- **Place before you add.** Find whose child a component is and nest it there; never dump new nodes at the
  root. Stop at the component level by default — drill a branch deeper only where a specific design
  genuinely needs it to be reasoned about, and even then as finer components, never a code dump.
- **Everything reachable from the index.** Every component and every view must be reachable by navigation
  from the **index** — through drill-down (nesting) or an explicit `navigateTo`. What you can't reach is
  orphaned and doesn't exist for the reader; a standalone view (a dynamic flow, a cross-cutting one)
  especially needs a `navigateTo` pointing at it.
- **One altitude per view.** A scoped view shows one zoom-level — a parent and the interacting units one
  level inside it. Mixed altitudes — a deployed unit beside its abstract base, a service beside another
  store's internals — are what make a diagram read as half architecture, half code.
- **Living, not carved.** Nodes are added, expanded, corrected, and pruned as the system's *shape* changes
  and is understood better; whether the source is the user's design or the actual code, the job is the
  same — keep the tree **true** and let it grow. It is never "done", but it moves with the
  **architecture**, not with every code edit.
- **Significant only, and short.** Only architecturally-significant components and their real
  relationships belong — quantity ≠ quality, and when in doubt it stays **OUT**. Inside a node, a crisp
  title and a minimal description: meaning comes from the tree's **structure**, not prose stuffed in the
  nodes.
- **English.** Identifiers, titles, descriptions — all English.

# The technical decisions — `docs/design/decisions.md`

A technical decision records a choice about the machinery that is closed — a language, a framework, a
store, a protocol, a library, a way of running it, something deliberately not used — together with the
reasoning that closed it. Written down, it stops being re-argued every few months, and a later reader
can tell a decision from an accident. It is the counterpart of the tree: the tree says what the shape
**is**, a decision says **why it is that and not the other thing**.

## Rules & concepts — non-negotiable
- **One file, beside the tree.** Every technical choice for the whole product lives in
  `docs/design/decisions.md`. Never one per sub-project, and never one inside a sub-project's own
  repo — a repo's own `CLAUDE.md` says how its code is written, not what the product is built on.
- **Every decision carries a permanent id.** `T` and a zero-padded three-digit number, running in order
  from the highest already taken. **Never reused and never renumbered**.
- **The heading is the decision itself.** One line naming what was chosen and — where there was a real
  alternative — what it was chosen over: `## T004 — The job queue is a Postgres table, not Redis`. A
  heading that names a topic instead of a choice is a decision not yet made.
- **Beneath it, only the reasoning and its ceiling.** Short `-` points: why this won, what it was
  weighed against and what that would have cost, the known limit where it stops working, what would
  overturn it. A paragraph under a heading is a decision written wrong.
- **Never the product's content.** Not what the product does or offers (that's `docs/product/features.md`), not
  a rule of the product a person could notice (that's `docs/product/decisions.md`), not the shape itself
  (that's `model.c4` — point at a node instead of redrawing it).
- **Name the feature only when the decision serves one.** Its heading then ends `(F004)`. Most serve
  the whole system and name none.
- **An entry is ≤300 chars — the heading and every point under it together.** Ids and bullet marks
  don't count. What will not fit is **two decisions**, never one written longer.
- **Superseded, never deleted.** A decision that no longer holds stays, its heading marked
  `— superseded by T0NN`, and the choice replacing it is a new entry with a new id.
- **The file carries its entries and nothing else.** No header block explaining what it is for, no
  restatement of these rules inside it — that is written **here**, once. Check what you are about to
  write against these rules *first*: a choice a person outside could notice is a **product** decision
  and does not belong here.
- **Strictly the template shape.** The file is the `example.decisions.md` shape shipped beside this
  skill — a title and its entries, nothing else.
