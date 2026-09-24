"""Russian typography for text about to go into a document.

typo(text) ties a label to its number ("Рис. 5", "Табл. 2", "Fig. 5", "Table 2") and an initial to the
next name ("А. С. Антропов") with no-break spaces, so a line never breaks between them. With
short_dash=True the long dash becomes the short one, for venues that ask for it.
"""

import re

_NBSP = ' '


def typo(text, short_dash=False):
    if short_dash:
        text = text.replace('—', '–')
    text = re.sub(r'(?<![\w.])([А-ЯЁ]\.) (?=[А-ЯЁ])', '\\1' + _NBSP, text)
    return re.sub(r'([Рр]ис\.|Fig\.|[Тт]абл(?:ица|\.)|Table) (?=\d)', '\\1' + _NBSP, text)


if __name__ == '__main__':
    assert typo('А. С. Антропов, Рис. 5') == 'А. С. Антропов, Рис. 5'
    assert typo('Табл. 2 — итог', short_dash=True) == 'Табл. 2 – итог'
    assert typo('Table 3 and word 4') == 'Table 3 and word 4'
    print('typo ok')
