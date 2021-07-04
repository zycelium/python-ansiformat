from collections import defaultdict
from typing import Optional, Union

import sty

from .color import Color, terminal_colors
from .string import AnsiString


class AnsiFormat(object):
    def __init__(
        self, palette: Optional[list] = None, term_colors: Optional[int] = None
    ):
        self._terminal_colors = (
            term_colors if term_colors is not None else terminal_colors()
        )
        self._custom_palette = palette

    def __call__(self, text=""):
        return AnsiString(text, self._terminal_colors, self._custom_palette)
