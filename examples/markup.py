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
