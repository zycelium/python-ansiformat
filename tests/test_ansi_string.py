from zycelium.ansiformat import AnsiString, ANSI_8_PALETTE


def test_no_formatting():
    astr = AnsiString("hello", 8)
    assert isinstance(astr, str)
    assert "'hello'" == astr.raw


def test_no_color():
    astr = AnsiString("hello", 0).fg("red")
    assert isinstance(astr, str)
    assert r"'hello'" == astr.raw


def test_foreground_color_ansi8():
    astr = AnsiString("hello", 8).fg("red")
    assert r"'\x1b[38;5;1mhello\x1b[0m'" == astr.raw


def test_background_color_ansi8():
    astr = AnsiString("hello", 8).bg("red")
    assert r"'\x1b[48;5;1mhello\x1b[0m'" == astr.raw


def test_foreground_color_ansi16():
    astr = AnsiString("hello", 16).fg("red")
    assert r"'\x1b[38;5;9mhello\x1b[0m'" == astr.raw


def test_background_color_ansi16():
    astr = AnsiString("hello", 16).bg("red")
    assert r"'\x1b[48;5;9mhello\x1b[0m'" == astr.raw


def test_foreground_color_ansi256():
    astr = AnsiString("hello", 256).fg("goldenrod")
    assert r"'\x1b[38;5;179mhello\x1b[0m'" == astr.raw


def test_background_color_ansi256():
    astr = AnsiString("hello", 256).bg("goldenrod")
    assert r"'\x1b[48;5;179mhello\x1b[0m'" == astr.raw


def test_foreground_color_ansi_truecolor():
    astr = AnsiString("hello", 300).fg("red")
    assert r"'\x1b[38;2;255;0;0mhello\x1b[0m'" == astr.raw


def test_background_color_ansi_truecolor():
    astr = AnsiString("hello", 300).bg("red")
    assert r"'\x1b[48;2;255;0;0mhello\x1b[0m'" == astr.raw


def test_effect_bold():
    astr = AnsiString("hello", 8).ef("bold")
    assert r"'\x1b[1mhello\x1b[0m'" == astr.raw


def test_effect_underline():
    astr = AnsiString("hello", 8).ef("underl")
    assert r"'\x1b[4mhello\x1b[0m'" == astr.raw


def test_foreground_color_reset():
    astr = AnsiString("hello ", 8).fg("red").rs("fg")("world")
    assert r"'\x1b[38;5;1mhello \x1b[39mworld\x1b[0m'" == astr.raw
