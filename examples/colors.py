from zycelium.ansiformat import AnsiFormat

af = AnsiFormat()

print(af("Red text on default background").red)
print(af("Default text on lime background").on.lime)
print(af("Black text on yellow background").black.on.yellow)
print(af("Black text on cyan background").black.on.color("#00ffff"))
print(af("Red text on yellow background").color("#ff0000").on.color("#ffff00"))

