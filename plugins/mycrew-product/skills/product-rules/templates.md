# The shapes — the index and the feature's doc

The index is not a file — it is `backlog milestone list`. A unit of work enters it with:

```bash
backlog milestone add "<Name>"          # ≤5 words, a feature or a cross-cutting job
```

The feature's doc — opened only when the feature has more to say than its name:

```bash
backlog doc create "<Name>" -t specification -p features
backlog doc update <id> --content "$(cat <<'EOF'
# <Name>

<Two or three sentences: what this feature is and what it gives a person. What is true about it
belongs in the bullets, not here.>

- <One fact per bullet — a rule, a bound, a state, an edge, something it must never do.>
- <…>

## <The part>

<A sentence or two: what this part is.>

- <its own facts, the same way>
EOF
)"
```

A part earns a section when it has a body of its own to state; a feature with none ends after its
bullets. A table stands in place of the bullets where the detail is genuinely a matrix — a set of
kinds, of rules, of values — and nowhere else.
