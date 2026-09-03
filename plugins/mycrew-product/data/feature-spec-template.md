# Feature Spec Template

Each feature spec lives at `./backlog/docs/features/<feature-name>.md`. Create it with
`backlog doc create "<title>" -p features -t specification`. The chief writes the spec before work
begins. It stays stable — code is written to it, never the other way around.

## The template

```markdown
# <Feature Name>

## What it does
<One paragraph — what this feature gives the user, in plain language.>

## What it doesn't
<Limits and edge cases explicitly excluded, scope boundaries. Prevents scope creep.>

## Components
<Parts that must all ship for the feature to work. Each is a checkbox.>
- [ ] <Component 1 — one line, what it covers>
- [ ] <Component 2>
- [ ] ...

## Dependencies
<What must exist before this feature can be built — other features, external services, data.>
- [ ] <Dependency 1>
- [ ] <Dependency 2>
- [ ] None

## Done when
<Verification criteria someone other than the builder can check.>
- [ ] All components complete
- [ ] <Specific acceptance criterion>
- [ ] <Another criterion>
```

## Rules for the template

- **Every section must be present.** If one doesn't apply, write "None" — never skip the section.
- **Components are not tasks.** A component is a logical piece of the feature; only the lead turns
  components into tasks on the board. One component may become zero, one, or several tasks.
- **The spec is written for humans.** Keep it brief. Agent-level detail goes in task implementation
  notes, never here.
- **The spec is stable.** Once written, it is not changed to match code — code changes to match it.
- **Classify before creating.** Always decide first: is this a standalone feature, or a component of
  an existing one? If a component, add it to the parent feature's Components section — don't open a
  new document. If unclear, ask the human.
