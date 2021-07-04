import logging
import os
import platform
import sys
from math import sqrt
from typing import Optional, Tuple, Union

import sty
from colour import Color as _Color
from colour import COLOR_NAME_TO_RGB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

IntervalValue = Union[int, float]
RGB255Tuple = Tuple[int, ...]
RGBTuple = Tuple[float, ...]

# Constants

CUBE_INTENSITIES = [
    0x80,
    0x5F,
    0x87,
    0xAF,
    0xD7,
    0xFF,
]

ANSI_8_PALETTE = [
    "#000000",  # black
    "#ff0000",  # red
    "#00ff00",  # lime
    "#ffff00",  # yellow
    "#0000ff",  # blue
    "#ff00ff",  # magenta
    "#00ffff",  # cyan
    "#ffffff",  # white
]

ANSI_16_PALETTE = [
    "#000000",  # black
    "#880000",  # darkred
    "#008800",  # darkgreen
    "#888800",  # orange
    "#000088",  # darkblue
    "#880088",  # darkmagenta
    "#008888",  # darkcyan
    "#888888",  # silver
    "#000000",  # gray
    "#ff0000",  # red
    "#00ff00",  # lime
    "#ffff00",  # yellow
    "#0000ff",  # blue
    "#ff00ff",  # magenta
    "#00ffff",  # cyan
    "#ffffff",  # white
]


def generate_256color(index):
    if index < 16:
        return ANSI_16_PALETTE[index]
    elif index < 232:
        q1, _b = divmod(index - 16, 6)
        q2, _g = divmod(q1, 6)
        _, _r = divmod(q2, 6)
        r = CUBE_INTENSITIES[_r]
        g = CUBE_INTENSITIES[_g]
        b = CUBE_INTENSITIES[_b]
        return f"#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}"
    else:
        i = 10 * (index - 232) + 8
        h = hex(i)[2:]
        if len(h) == 1:
            h = "0" + h
        return f"#{h}{h}{h}"


ANSI_256_PALETTE = [generate_256color(i) for i in range(256)]


def map_interval(
    from_start: IntervalValue,
    from_end: IntervalValue,
    to_start: IntervalValue,
    to_end: IntervalValue,
    value: IntervalValue,
) -> IntervalValue:
    """
    Map numbers from an interval to another.

    >>> map_interval(0, 1, 0, 255, 0.5)
    127.5

    >>> map_interval(0, 255, 0, 1, 128)  # doctest: +ELLIPSIS
    0.50...

    :param from_start: lower bound of source interval.
    :param from_end: upper bound of source interval.
    :param to_start: lower bound of target interval.
    :param to_end: upper bound of target interval.
    :param value: source value to map to target interval.
    :return: value in target interval.
    """
    return (value - from_start) * (to_end - to_start) / (
        from_end - from_start
    ) + to_start


def rgb_to_RGB255(rgb: RGBTuple) -> RGB255Tuple:
    """
    Convert from Color.rgb's 0-1 range to ANSI RGB (0-255) range.

    >>> rgb_to_RGB255((1, 0.5, 0))
    (255, 128, 0)
    """
    return tuple([int(round(map_interval(0, 1, 0, 255, c))) for c in rgb])


def color_hex_to_int(color):
    return int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)


def distance(color_1, color_2):
    r1, g1, b1 = color_hex_to_int(color_1)
    r2, g2, b2 = color_hex_to_int(color_2)
    return sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)


def match_index(color, palette):
    min_index = -1
    min_distance = 1000000000
    for i, c in enumerate(palette):
        d = distance(color, c)
        if d < min_distance:
            min_index = i
            min_distance = d
    return min_index


def match_color(color, palette):
    index = match_index(color, palette)
    return palette[index]


def terminal_colors(stream=sys.stdout) -> int:
    """
    Get number of supported ANSI colors for a stream.
    Defaults to sys.stdout.

    >>> terminal_colors(sys.stderr)
    0
    """
    colors = 0
    if stream.isatty():
        if platform.system() == "Windows":
            # colorama supports 8 ANSI colors
            # (and dim is same as normal)
            colors = 8
        elif os.environ.get("NO_COLOR", None) is not None:
            colors = 0
        elif os.environ.get("COLORTERM", "").lower() in {"truecolor", "24bit"}:
            colors = 16_777_216
        elif os.environ.get("TERM", "") in {"vt100", "vt200", "vt220"}:
            colors = 0
        elif os.environ.get("TERM", "") in {"xterm"}:
            colors = 8
        elif os.environ.get("TERM", "") in {"xterm-color", "rxvt", "rxvt-88color"}:
            colors = 16
        elif os.environ.get("TERM", "") in {"ansi", "xterm-256color"}:
            colors = 256
        elif os.environ.get("TERM", "").lower() in {"truecolor", "24bit"}:
            colors = 16_777_216
        else:
            # curses is used to autodetect terminal colors on *nix.
            try:
                from curses import setupterm, tigetnum

                setupterm()
                colors = max(0, tigetnum("colors"))
            except ImportError:
                pass
            except:
                pass
    return colors


class Color(_Color):
    @property
    def RGB(self):
        return rgb_to_RGB255(self.rgb)

    @property
    def ansi8(self):
        return (match_index(self.hex_l, ANSI_8_PALETTE),)

    @property
    def ansi16(self):
        return (match_index(self.hex_l, ANSI_16_PALETTE),)

    @property
    def ansi256(self):
        return (match_index(self.hex_l, ANSI_256_PALETTE),)

    def match_palette(self, palette):
        return Color(match_color(self.hex_l, palette)).RGB
