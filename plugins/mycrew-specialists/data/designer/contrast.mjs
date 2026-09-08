#!/usr/bin/env node
/*
 * The palette's own check — copy this in beside the kit on first use.
 *
 * It reads tokens.css, resolves every colour token, and measures the
 * combinations the kit ACTUALLY PUTS ON SCREEN, in every theme, in one run.
 * Touch a hex, run it: `node design/contrast.mjs`. A kit is not handed over
 * while one pair sits under its floor.
 *
 * Two things to do to this file before it is worth anything:
 *   1. Make it read your tokens. It understands two shapes and nothing else —
 *      `--name: light-dark(#aabbcc, #ddeeff);` for a token that differs by
 *      theme, and `--name: var(--other);` for an alias. If your kit declares
 *      colour some other way, teach the two regexes below that shape rather
 *      than declaring colour twice.
 *   2. Replace PAIRS wholesale. What ships here is a starter, not a spec:
 *      every kit puts different things on top of different things, and a pair
 *      the kit never draws is noise, while one it draws and this file does not
 *      list is exactly the failure this file exists to catch. Walk the kit and
 *      list what you actually see.
 */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const css = readFileSync(join(here, 'tokens.css'), 'utf8');

const themes = { light: {}, dark: {} };
for (const [, name, light, dark] of css.matchAll(
	/--([\w-]+):\s*light-dark\(\s*(#[0-9a-f]{6})\s*,\s*(#[0-9a-f]{6})\s*\)/gi
)) {
	themes.light[name] = light;
	themes.dark[name] = dark;
}
/* A token that does not change with the theme: one hex, both sides. */
for (const [, name, hex] of css.matchAll(/--([\w-]+):\s*(#[0-9a-f]{6})\s*;/gi)) {
	for (const theme of Object.values(themes)) if (!theme[name]) theme[name] = hex;
}
/* --vote-up: var(--accent); — an alias resolves to whatever it points at. */
for (const [, name, target] of css.matchAll(/--([\w-]+):\s*var\(--([\w-]+)\);/g)) {
	for (const theme of Object.values(themes)) if (theme[target]) theme[name] = theme[target];
}

const channel = (v) => (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4);

function luminance(hex) {
	const [r, g, b] = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255);
	return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

function ratio(a, b) {
	const [x, y] = [luminance(a), luminance(b)].sort((m, n) => n - m);
	return (x + 0.05) / (y + 0.05);
}

/* Three floors, because three different jobs.
 *   TEXT   4.5 — anything carrying words. Small text is normal text under 1.4.3.
 *   OBJECT 3.0 — the part of a control that says the control is there: a
 *                field's edge, a toggle's track, the focus ring (1.4.11).
 *   SEEN   1.3 — a hairline organising content, or the unfilled half of a
 *                gauge whose value is also stated in words. 1.4.11 does not
 *                reach these; this floor only catches one that has gone
 *                invisible. Never move a pair down here to make it pass.
 */
const TEXT = 4.5;
const OBJECT = 3;
const SEEN = 1.3;

/* [foreground, background, floor, what it is]
 *
 * A STARTER. Replace it with the pairs your kit really draws — and every one
 * of them, including the ones you assume are fine. Rename these tokens to
 * yours; the names below are the roles the kit template starts from.
 */
const PAIRS = [
	/* Ink on every ground it ever lands on — including the hovered and the
	   inset ones, which is where these quietly fail. */
	['ink', 'surface', TEXT, 'body text on a surface'],
	['muted', 'surface', TEXT, 'secondary text on a surface'],
	/* The accent, wherever it carries a word. */
	['accent', 'surface', TEXT, 'a link'],
	['on-accent', 'accent', TEXT, 'a primary button'],
	/* What goes wrong, wherever it is said. */
	['danger', 'surface', TEXT, 'an error'],
	/* A control's own edge, and the focus ring: seen, not read, and the only
	   thing telling a person the control is there. */
	['border', 'surface', OBJECT, 'a field on a surface'],
	['accent', 'surface', OBJECT, 'the focus ring'],
	/* Hairlines organising content: seen, never read, never a control. */
	['border', 'surface', SEEN, 'a divider']
];

let failures = 0;
for (const theme of Object.keys(themes)) {
	const rows = [];
	for (const [fg, bg, floor, what] of PAIRS) {
		const a = themes[theme][fg];
		const b = themes[theme][bg];
		if (!a || !b) {
			rows.push(`  MISSING  --${fg} / --${bg}   ${what}`);
			failures++;
			continue;
		}
		const r = ratio(a, b);
		const ok = r >= floor;
		if (!ok) failures++;
		rows.push(
			`  ${ok ? 'ok  ' : 'FAIL'}  ${r.toFixed(2).padStart(5)} : 1  (needs ${floor})  ` +
				`--${fg} on --${bg}${' '.repeat(Math.max(0, 34 - fg.length - bg.length))}${what}`
		);
	}
	console.log(`\n${theme.toUpperCase()}\n${rows.join('\n')}`);
}

console.log(
	failures === 0
		? '\nEvery pair the kit puts on screen clears AA, in every theme.\n'
		: `\n${failures} pair(s) below the floor.\n`
);
process.exit(failures === 0 ? 0 : 1);
