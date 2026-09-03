---
name: agentmaker
description: "Use when someone wants a custom agent built. Asks for role, character and path, fills the rest from defaults, writes one agent file to the path they name."
argument-hint: "<the agent to build: role, character, path — or a fragment of it>"
---

# agentmaker — build a custom agent by asking

Builds one custom agent as `.claude/agents/<name>.md`. Ask the questions below before writing anything.
The output is one new file at the path the human named — no code, no edit to existing agents, nothing
else.

## Questions

Batch as many as you can into one question — don't ask one at a time. Skip what the ask already
supplies. The file is created **only after every question below has an answer** — never write it while
any block in the template is still unknown.

- **Name** — what is the agent called?
- **Model** — which model?
- **Effort** — how much effort to use?
- **Location** — where does the file go? `.claude/agents/`, a plugin's `agents/`, anywhere.
- **Tools** — which tools are available to it?

Then close with the purpose. Ask this one on its own, always:

- **Role and responsibility** — what is it for, and what responsibility does it carry?

- **Character** — describe in a couple of sentences what its personality should be.

- **Why you were called** — when is it spawned, and for what?
- **Tasks** — what does it carry out?
- **Your tools and scripts** — what tools or scripts does it need, and what does it use each for?
- **Other aspects of work** — any extra duties, limits, or ways of working it must hold?

## Template

```markdown
---
name: <name>
description: "<routing line: who it is + what it carries, for spawning.>"
model: <model>
effort: <effort>
tools: <tools>
---

# <name> — <who you are>

## Who you are

<who the agent is, its name, its essence — one to two sentences>

## Responsibilities

### Yours

- <an action that he can do mechanically>
- <a non-mechanical task is quality control of some aspect>

### Not Yours    

- <an action that he can do mechanically>
- <a non-mechanical task is quality control of some aspect>

## Character

<character traits>
<the way he talks>
<his work speed>

## Your tools

- <skills>
- <mcp>
- <scripts>

## Other aspects of work

### <aspect>

- <bullets>

```

Assemble frontmatter (`name`, `description` routing who+role, `model`, `effort`, `tools`) then fill the
body blocks from the answers. Name the file `<name>.md` at the chosen path. Report the path written,
the spawn name, the character set, anything left open as `[UNRESOLVED]`.
