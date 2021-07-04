# ansiformat

ANSI Formatted Text for Terminals.

## AnsiFormat for Custom Formatting

### Colors

```python
from zycelium.ansiformat import AnsiFormat

af = AnsiFormat()

print(af("Red text on default background").red)
print(af("Default text on lime background").on.lime)
print(af("Black text on yellow background").black.on.yellow)
print(af("Black text on cyan background").black.on.color("#00ffff"))
print(af("Red text on yellow background").color("#ff0000").on.color("#ffff00"))
```

### Effects

```python
from zycelium.ansiformat import AnsiFormat

af = AnsiFormat()

print(af("Bold").bold)
print(af("Dim").dim)
print(af("Italic").italic)
print(af("Underline").underline)
print(af("Blink").blink)
print(af("Inverse").inverse)
print(af("Hidden").hidden)
print(af("Strike").strike)
```

### Using Colors and Effects Together

```python
from zycelium.ansiformat import AnsiFormat

af = AnsiFormat()

print(af("Red text on default background, bold").red.bold)
print(af("Same, but with shortcut (b) for bold").red.b)
print(af("Same, but with shortcut (i) for italic").red.i)
print(af("Default text on lime background, with strike-through").on.lime.strike)
print(af("Black text on yellow background, underlined").black.on.yellow.underline)
print(af("Black text on cyan background, blinking").black.on.color("#00ffff").blink)
print(af("Red text on yellow background, inversed").color("#ff0000").on.color("#ffff00").inverse)
```

## AnsiMarkup for Quick Formatting

```python
from zycelium.ansiformat import AnsiMarkup, palette

m = AnsiMarkup(palette=palette.midnight_ablaze)

print(m.debug("debug"))
print(m.info("info"))
print(m.ok("ok"))
print(m.warning("warning"))
print(m.error("error"))
print(m.critical("critical"))

print(m.p("paragraph"))
print(m.aside("aside"))
print(m.note("note"))
print(m.alert("alert"))

print(m.h1("heading one"))
print(m.h2("heading two"))
print(m.h3("heading three"))
print(m.h4("heading four"))
print(m.h5("heading five"))
print(m.h6("heading six"))

with m.indent():
    print(m.li("list item 1"))
    print(m.li("list item 2"))
    with m.indent():
        print(m.li("list item 2.1"))
        print(m.li("list item 2.2"))
```