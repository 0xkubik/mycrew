# Keep marketplace and plugin descriptions short — a two-sentence pitch, not a feature tour

The `description` in `marketplace.json` and in each `plugin.json` is the single line a person
reads in the plugin browser before installing. Left unchecked it swells into a paragraph that
walks every command, every layer relation and every design flourish — so someone scanning the
list can't tell at a glance what the plugin is for, and every rename rots the text.

- **One or two sentences, then stop.** A third sentence is the sign the rest belongs in the
  plugin's README.
- **Say what it does and who reaches for it.** Plain statement of the job — not how it is wired
  together, not the internal cast, not a walkthrough of the mechanism.
- **Don't enumerate the commands.** They are discoverable from the plugin itself, and a list of
  them dates on the next rename. Name the one or two that define it, at most.
- **No lore.** "each layer drives the one beneath", "the eyes that hunt are never the author's" —
  rationale like this reads well in docs and only clutters a one-line pitch.
- **The pitch is not the manual.** Anything that needs more than two sentences goes where there
  is room — the plugin's README or its skills' own descriptions — never the `description` field.
