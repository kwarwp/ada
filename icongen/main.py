# ada.icongen.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" gerador de icone em svg a partir de uma frase.

.. codeauthor:: Carlo Oliveira <mail@local.tipo>

Changelog
---------
.. versionadded::    23.08
        Primeiro desenho.

"""
from browser import document, html, svg


class Icon:
    def __init__(self):        
        dc = document["pydiv"]
        self.panel = panel = svg.svg(200,200)
        dc.html=""
        dc <= panel
        self.r("0", "0", "200", "200", "white")
    def r(self, x, y, width, height, fill="black", border=0):
        self.panel <= svg.rect(x=x, y=y, width=width, height=height, style=dict(fill=fill, stroke=border))
    def t(self, text, x, y, size, fill="black", text_anchor="middle",border=1):
        self.panel <= svg.text(text, x=x, y=y, font_size=size, text_anchor=text_anchor, style=dict(fill=fill, stroke=border))

i = Icon()
i.r(0,0, 10, 10, 'red')

