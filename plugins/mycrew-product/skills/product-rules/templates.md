# The shapes — one for each file the plane holds

`docs/product/features.md`:

```markdown
# Features — <product name>

- [ ] F001 — <Name>
- [x] F002 — <Name>
```

`docs/product/notes.md` — the same shape, its own id space:

```markdown
# Notes — <product name>

- [ ] N001 — <Name>
```

`docs/product/features/F00N-<slug>.md` — an opening that says what the feature is, the bullets that
say what is true about it, then a section for each part big enough to carry its own body:

```markdown
# F001 — <Name>

<Two or three sentences: what this feature is and what it gives a person. What is true about it
belongs in the bullets, not here.>

- <One fact per bullet — a rule, a bound, a state, an edge, something it must never do.>
- <…>

## <The part>

<A sentence or two: what this part is.>

- <its own facts, the same way>
```

A part earns a section when it has a body of its own to state; a feature with none ends after its
bullets. A table stands in place of the bullets where the detail is genuinely a matrix — a set of
kinds, of rules, of values — and nowhere else.
