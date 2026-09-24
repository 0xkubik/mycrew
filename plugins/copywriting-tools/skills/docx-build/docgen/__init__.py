"""docgen: template-independent building blocks for Markdown -> Word converters.

A build script imports what it needs and supplies everything template-specific itself
(style names, title-page phases, captions, header text, table width). See ../SKILL.md.
"""

from .figures import find_mmdc, insert_image, render_mermaid, resolve_image_path
from .inline import add_inline_runs
from .math_omml import insert_formula, status as math_engine
from .md import parse_frontmatter, parse_md
from .ooxml import (add_field_code, add_page_numbers, clear_body, clear_header_highlights,
                    replace_header_text, set_even_odd_headers)
from .tables import add_table, table_rows
