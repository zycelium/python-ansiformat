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
