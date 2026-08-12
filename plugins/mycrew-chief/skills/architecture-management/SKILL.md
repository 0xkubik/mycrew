---
name: architecture-management
description: "Use for anything about the product's architecture model — shaping, growing, or correcting the structure. Not WHAT to build (that's feature-management / what-to-do) but HOW the system is shaped: one living LikeC4 tree in docs/architecture/model.c4 at the product root, spanning every sub-project, down to the finest component that matters — never a mirror of the code. The chief owns it; workers build to it. Rules and concepts, not a fixed procedure."
user-invocable: false
---

# architecture-management — the architecture, as a living tree

You describe the product's **structure** — not *what* to build (feature-management / what-to-do), but
*how* it's shaped. It lives as **one living tree** in `docs/architecture/model.c4` **at the product
root**, spanning every sub-project. LikeC4 syntax is in **`mycrew-tools:likec4`** — load it before editing.

**You own it — a worker never reshapes it.** A worker reads this tree and builds to it; when the work
needs the shape to move, it says so in its report and you make the move here, then re-dispatch.

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
