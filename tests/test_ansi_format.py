from zycelium.ansiformat import AnsiFormat


def test_no_formatting():
    af = AnsiFormat()
    astr = af("hello")
    assert "'hello'" == astr.raw


def test_no_color():
    af = AnsiFormat(term_colors=0)
    astr = af("hello")
    assert isinstance(astr, str)
    assert r"'hello'" == astr.raw


def test_foreground_color_ansi8():
    af = AnsiFormat(term_colors=8)
    astr = af("hello").fg("red")
    assert r"'\x1b[38;5;1mhello\x1b[0m'" == astr.raw


def test_foreground_color_ansi8_via_property():
    af = AnsiFormat(term_colors=8)
    astr = af("hello").fg_red
    assert r"'\x1b[38;5;1mhello\x1b[0m'" == astr.raw


def test_background_color_ansi8_via_property():
    af = AnsiFormat(term_colors=8)
    astr = af("hello").bg_red
    assert r"'\x1b[48;5;1mhello\x1b[0m'" == astr.raw


def test_effect_bold_ansi8_via_property():
    af = AnsiFormat(term_colors=8)
    astr = af("hello").ef_bold
    assert r"'\x1b[1mhello\x1b[0m'" == astr.raw


def test_effect_bold_ansi8_via_shortcut():
    af = AnsiFormat(term_colors=8)
    astr = af("hello").b
    assert r"'\x1b[1mhello\x1b[0m'" == astr.raw
