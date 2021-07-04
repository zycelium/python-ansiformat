from contextlib import contextmanager
from textwrap import indent
from typing import Optional

from zycelium.ansiformat import AnsiFormat


class AnsiMarkup(object):
    def __init__(self, palette=None, term_colors=None):
        self.af = AnsiFormat(palette=palette, term_colors=term_colors)
        self._indent = 0

    def debug(self, text):
        return self.af().gray(text)

    def info(self, text):
        return self.af().blue(text)

    def ok(self, text):
        return self.af().green(text)

    def warning(self, text):
        return self.af().orange(text)

    def error(self, text):
        return self.af().red(text)

    def critical(self, text):
        return self.af().yellow.on.red(text)

    def p(self, text):
        return self.af().black(text)

    def aside(self, text):
        return self.af("[~]").black.on.lightgray.rs_all(" ")(text)

    def note(self, text):
        return self.af("[>]").black.on.lime.rs_all(" ")(text)

    def alert(self, text):
        return self.af("[!]").black.on.orange.rs_all(" ")(text)

    def h1(self, text):
        return self.af("# ").red.b.u(text)

    def h2(self, text):
        return self.af("## ").darkorange.b.u(text)

    def h3(self, text):
        return self.af("### ").blue.b.u(text)

    def h4(self, text):
        return self.af("#### ").black.b.u(text)

    def h5(self, text):
        return self.af("##### ").black.b.u(text)

    def h6(self, text):
        return self.af("###### ").black.b.u(text)

    def li(self, text):
        _text = str(self.af("- ").blue(text))
        _text = indent(_text, " " * self._indent)
        return _text

    @contextmanager
    def indent(self, text=""):
        self._indent = self._indent + 2
        yield
        self._indent = self._indent - 2
