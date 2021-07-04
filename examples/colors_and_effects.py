from zycelium.ansiformat import AnsiFormat

af = AnsiFormat()

print(af("Red text on default background, bold").red.bold)
print(af("Same, but with shortcut (b) for bold").red.b)
print(af("Same, but with shortcut (i) for italic").red.i)
print(af("Default text on lime background, with strike-through").on.lime.strike)
print(af("Black text on yellow background, underlined").black.on.yellow.underline)
print(af("Black text on cyan background, blinking").black.on.color("#00ffff").blink)
print(af("Red text on yellow background, inversed").color("#ff0000").on.color("#ffff00").inverse)

