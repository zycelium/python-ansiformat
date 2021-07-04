from collections import defaultdict
from typing import Optional, Union

import sty

from .color import Color, terminal_colors

SHORTCUTS = {
    "b": "ef_bold",
    "bold": "ef_bold",
    "dim": "ef_dim",
    "blink": "ef_blink",
    "hidden": "ef_hidden",
    "inverse": "ef_inverse",
    "strike": "ef_strike",
    "i": "ef_italic",
    "italic": "ef_italic",
    "u": "ef_underl",
    "underline": "ef_underl",
}


class AnsiString(str):
    def __new__(
        cls, text: str, terminal_colors: int = 0, custom_palette: Optional[list] = None
    ):
        return super().__new__(cls, text)

    def __init__(
        self, text: str, terminal_colors: int = 0, custom_palette: Optional[list] = None
    ):
        self._text = text
        self._terminal_colors = terminal_colors
        self._custom_palette = custom_palette
        self._buffer = []
        self._fg_is_set = False

    def __str__(self):
        if self._buffer:
            text = "".join(self._buffer) + self._text
            if self._terminal_colors > 0:
                text += sty.rs.all
            return text
        else:
            return self._text

    def __call__(self, text: str):
        if self._text:
            self._buffer.append(self._text)
        self._text = text
        self._fg_is_set = False
        return self

    def __getattr__(self, name):
        if name.startswith("fg_"):
            return self.fg(name[3:])
        elif name.startswith("bg_"):
            return self.bg(name[3:])
        elif name.startswith("rs_"):
            return self.rs(name[3:])
        elif name.startswith("ef_"):
            return self.ef(name[3:])
        elif name in SHORTCUTS:
            return getattr(self, SHORTCUTS[name])
        elif name == "color":
            return self.color
        else:
            if self._fg_is_set:
                return self.bg(name)
            else:
                return self.fg(name)

    def color(self, name: str):
        if self._fg_is_set:
            return self.bg(name)
        else:
            return self.fg(name)

    def render_color(self, color: Color):
        if self._terminal_colors <= 0:
            return None
        if isinstance(color, str):
            color = Color(color)
        else:
            color = Color(*color)
        if self._terminal_colors == 8:
            return color.ansi8
        elif self._terminal_colors == 16:
            return color.ansi16
        elif self._terminal_colors == 256:
            return color.ansi256
        else:
            if self._custom_palette:
                return color.match_palette(self._custom_palette)
            else:
                return color.RGB

    def fg(self, color: Union[str, list, tuple]):
        if self._terminal_colors == 0:
            return self
        color = self.render_color(color)
        if color is None:
            return self
        self._buffer.append(sty.fg(*color))
        return self

    def bg(self, color: Union[str, list, tuple]):
        if self._terminal_colors == 0:
            return self
        color = self.render_color(color)
        if color is None:
            return self
        self._buffer.append(sty.bg(*color))
        return self

    def rs(self, name: str):
        if self._terminal_colors == 0:
            return self
        ansi = getattr(sty.rs, name)
        self._buffer.append(self._text)
        self._text = ""
        self._buffer.append(ansi)
        return self

    def ef(self, name: str):
        if self._terminal_colors == 0:
            return self
        ansi = getattr(sty.ef, name)
        self._buffer.append(ansi)
        return self

    @property
    def on(self):
        self._fg_is_set = True
        return self

    @property
    def raw(self):
        return repr(str(self))
