"""LaTeX -> native Word equations (OMML), with a Unicode fallback.

Pipeline: LaTeX -> MathML (latex2mathml) -> OMML (Microsoft's mathml2omml.xsl, which ships inside
Word.app on macOS; set MATHML2OMML_XSL to point at a copy elsewhere). Without the XSL or the
libraries, formulas fall back to italic Unicode text; status() says which engine is active.

Set FONT, SIZE_PT and the two tab stops from the build script to match the template.
"""

import os
import re
import sys

from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

FONT = 'Times New Roman'
SIZE_PT = 10
TAB_CENTER_CM = 7.0      # where a numbered display formula is centred
TAB_RIGHT_CM = 14.0      # where its (N) number sits

_M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
_XSL_PATHS = [
    os.environ.get('MATHML2OMML_XSL', ''),
    '/Applications/Microsoft Word.app/Contents/Resources/mathml2omml.xsl',
    '/Applications/Microsoft Office/Microsoft Word.app/Contents/Resources/mathml2omml.xsl',
]

_l2m = _etree = _xslt = None
try:
    import latex2mathml.converter as _l2m
    from lxml import etree as _etree
    for _p in _XSL_PATHS:
        if _p and os.path.isfile(_p):
            _xslt = _etree.XSLT(_etree.parse(_p))
            break
except ImportError:
    pass


def status():
    """Which engine is active: 'omml' (native Word equations) or 'unicode-fallback'."""
    return 'omml' if _xslt is not None else 'unicode-fallback'


LATEX_SYMBOLS = {
    r'\cdot': '·', r'\to': '→', r'\leftarrow': '←', r'\Rightarrow': '⇒', r'\Leftrightarrow': '⟺',
    r'\leftrightarrow': '↔', r'\pi': 'π', r'\lambda': 'λ', r'\alpha': 'α', r'\beta': 'β',
    r'\gamma': 'γ', r'\delta': 'δ', r'\epsilon': 'ε', r'\varepsilon': 'ε', r'\sigma': 'σ',
    r'\omega': 'ω', r'\mu': 'μ', r'\nu': 'ν', r'\phi': 'φ', r'\varphi': 'φ', r'\psi': 'ψ',
    r'\rho': 'ρ', r'\tau': 'τ', r'\theta': 'θ', r'\xi': 'ξ', r'\zeta': 'ζ', r'\eta': 'η',
    r'\kappa': 'κ', r'\chi': 'χ', r'\leq': '≤', r'\geq': '≥', r'\neq': '≠', r'\approx': '≈',
    r'\infty': '∞', r'\sum': 'Σ', r'\prod': 'Π', r'\in': '∈', r'\notin': '∉', r'\subset': '⊂',
    r'\cup': '∪', r'\cap': '∩', r'\forall': '∀', r'\exists': '∃', r'\nabla': '∇',
    r'\partial': '∂', r'\oplus': '⊕', r'\times': '×', r'\div': '÷', r'\pm': '±',
    r'\lfloor': '⌊', r'\rfloor': '⌋', r'\lceil': '⌈', r'\rceil': '⌉', r'\langle': '⟨',
    r'\rangle': '⟩', r'\cdots': '···', r'\ldots': '…', r'\vdots': '⋮', r'\ddots': '⋱',
    r'\sim': '∼', r'\cong': '≅', r'\equiv': '≡', r'\mathbb{R}': 'ℝ', r'\mathbb{Z}': 'ℤ',
    r'\mathbb{N}': 'ℕ', r'\mathbb{C}': 'ℂ', r'\mathbb{F}': '𝔽', r'\circ': '∘', r'\bullet': '•',
    r'\star': '★', r'\mathbf': '', r'\boldsymbol': '',
}
_SUP = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()n',
                     '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𝒒ʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿˢᵀᵁᵛᵂˣʸᶻ⁺⁻⁼⁽⁾ⁿ')
_SUB = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyz+-=()aeiou',
                     '₀₁₂₃₄₅₆₇₈₉ₐᵦ꜀ᵈₑ𝒻ᵍₕᵢⱼₖₗₘₙₒₚ𝒒ᵣₛₜᵤᵥ𝓌ₓᵧ𝓏₊₋₌₍₎ₐₑᵢₒᵤ')


def _apply_scripts(text):
    text = re.sub(r'\^\{([^}]*)\}', lambda m: m.group(1).translate(_SUP), text)
    text = re.sub(r'_\{([^}]*)\}', lambda m: m.group(1).translate(_SUB), text)
    text = re.sub(r'\^([A-Za-z0-9])', lambda m: m.group(1).translate(_SUP), text)
    return re.sub(r'_([A-Za-z0-9])', lambda m: m.group(1).translate(_SUB), text)


def latex_to_unicode(formula):
    """Readable Unicode for a formula when native equations are unavailable."""
    f = formula.strip()
    f = re.sub(r'\\text\{([^}]*)\}', r'\1', f)
    bb = {'R': 'ℝ', 'Z': 'ℤ', 'N': 'ℕ', 'C': 'ℂ', 'Q': 'ℚ', 'P': 'ℙ'}
    f = re.sub(r'\\mathbb\{([A-Z])\}', lambda m: bb.get(m.group(1), m.group(1)), f)
    f = re.sub(r'\\math(?:cal|rm|sf|tt|bf|it|scr)\{([^}]*)\}', r'\1', f)
    f = re.sub(r'\\operatorname\{([^}]*)\}', r'\1', f)
    f = re.sub(r'\\(?:boldsymbol|mathbf|bm)\{([^}]*)\}', r'\1', f)
    f = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'(\1)/(\2)', f)
    for latex, uni in sorted(LATEX_SYMBOLS.items(), key=lambda x: -len(x[0])):
        f = f.replace(latex, uni)
    f = _apply_scripts(f)
    f = re.sub(r'\\([A-Za-z]+)', r'\1', f)
    f = re.sub(r'\{([^{}]*)\}', r'\1', f)
    return re.sub(r'  +', ' ', f).strip()


def latex_to_omml(latex):
    """A native m:oMath element, or None when the engine is unavailable or the formula fails."""
    if _xslt is None:
        return None
    try:
        mathml = _l2m.convert(latex.strip(), display='block')
        return _xslt(_etree.fromstring(mathml.encode('utf-8'))).getroot()
    except Exception as e:
        print(f"warning: LaTeX->OMML failed for {latex[:60]!r}: {e}", file=sys.stderr)
        return None


_TAG = re.compile(r'\\tag\{([^}]*)\}')


def _insert_number(para, tag):
    """Right-aligned equation number (N) via tab stops; the formula is centred between them."""
    pf = para.paragraph_format
    pf.first_line_indent = Cm(0)
    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.tab_stops.add_tab_stop(Cm(TAB_CENTER_CM), WD_TAB_ALIGNMENT.CENTER)
    pf.tab_stops.add_tab_stop(Cm(TAB_RIGHT_CM), WD_TAB_ALIGNMENT.RIGHT)

    lead = OxmlElement('w:r')
    lead.append(OxmlElement('w:tab'))
    ppr = para._p.find(qn('w:pPr'))
    if ppr is not None:
        ppr.addnext(lead)
    else:
        para._p.insert(0, lead)
    trail = OxmlElement('w:r')
    trail.append(OxmlElement('w:tab'))
    para._p.append(trail)

    run = para.add_run(f'({tag})')
    run.font.name = FONT
    run.font.size = Pt(SIZE_PT)


def insert_formula(para, formula, display=False):
    """Put a formula into para. '\\tag{N}' inside a display formula becomes a right-hand (N)."""
    tag = None
    m = _TAG.search(formula)
    if m:
        tag = m.group(1)
        formula = _TAG.sub('', formula).strip()

    omml = latex_to_omml(formula)
    if omml is not None:
        if display and tag:
            para._p.append(omml)
            _insert_number(para, tag)
        elif display:
            block = _etree.SubElement(para._p, f'{{{_M_NS}}}oMathPara')
            props = _etree.SubElement(block, f'{{{_M_NS}}}oMathParaPr')
            _etree.SubElement(props, f'{{{_M_NS}}}jc').set(f'{{{_M_NS}}}val', 'center')
            block.append(omml)
        else:
            para._p.append(omml)
        return

    run = para.add_run(latex_to_unicode(formula))
    run.italic = True
    run.font.name = FONT
    run.font.size = Pt(SIZE_PT)
    if display and tag:
        _insert_number(para, tag)
