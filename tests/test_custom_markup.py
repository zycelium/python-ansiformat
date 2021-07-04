from zycelium.ansiformat import AnsiFormat

af = AnsiFormat(term_colors=256)


class Theme:
    p = lambda _, t: af().black(t)
    info = lambda _, t: af().blue(t)
    note = lambda _, t: af().b.darkgreen("Note:").rs_all(" ")(t)
    alert = lambda _, t: af().b.red.on.yellow("Alert:").rs_all(" ")(t)
    h1 = lambda _, t: af().b.black.on.gold("# ")(t)
    h2 = lambda _, t: af().b.black.on.violet("## ")(t)
    h3 = lambda _, t: af().b.black.on.skyblue("### ")(t)
    h4 = lambda _, t: af().b("#### ")(t)
    h5 = lambda _, t: af().b("##### ")(t)
    h6 = lambda _, t: af().b("###### ")(t)


t = Theme()


def test_theme():
    assert t.p("Have a paragraph").raw == r"'\x1b[38;5;0mHave a paragraph\x1b[0m'"
    assert (
        t.note("This is important").raw
        == r"'\x1b[1m\x1b[38;5;2mNote:\x1b[0m This is important\x1b[0m'"
    )
    assert (
        t.alert("This is urgent").raw
        == r"'\x1b[1m\x1b[38;5;9m\x1b[48;5;11mAlert:\x1b[0m This is urgent\x1b[0m'"
    )
    assert (
        t.h1("Heading level one").raw
        == r"'\x1b[1m\x1b[38;5;0m\x1b[48;5;11m# Heading level one\x1b[0m'"
    )
    assert (
        t.h2("Heading level two").raw
        == r"'\x1b[1m\x1b[38;5;0m\x1b[48;5;201m## Heading level two\x1b[0m'"
    )
    assert (
        t.h3("Heading level three").raw
        == r"'\x1b[1m\x1b[38;5;0m\x1b[48;5;116m### Heading level three\x1b[0m'"
    )
    assert t.h4("Heading level four").raw == r"'\x1b[1m#### Heading level four\x1b[0m'"
    assert t.h5("Heading level five").raw == r"'\x1b[1m##### Heading level five\x1b[0m'"
    assert t.h6("Heading level six").raw == r"'\x1b[1m###### Heading level six\x1b[0m'"


def test_calling_multiple_times():
    assert t.info("This is FYI").raw == r"'\x1b[38;5;12mThis is FYI\x1b[0m'"
    assert t.info("This is FYI").raw == r"'\x1b[38;5;12mThis is FYI\x1b[0m'"
    assert t.info("This is FYI").raw == r"'\x1b[38;5;12mThis is FYI\x1b[0m'"
    assert t.info("This is FYI").raw == r"'\x1b[38;5;12mThis is FYI\x1b[0m'"
