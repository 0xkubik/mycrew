# The shapes — one for both lists, none for a feature's own file

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

`docs/product/features/F00N-<slug>.md` — **no template**. One fixed title, then whatever the feature
needs to be understood:

```markdown
# F001 — <Name>

<what this feature concretely is, in their words, however it needs to read>
```
