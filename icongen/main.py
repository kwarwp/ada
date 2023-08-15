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
        bk = svg.rect(x=0, y=0, width="200", height="200", style=dict(fill="white"))
        dc.html=""
        dc <= panel
    def r(x, y, width, height, fill, border)
legend = None
#print(svg.text)
title = svg.text("alo", x=150, y=25,
    font_size=22, text_anchor="middle",
    style={"stroke": "black"})
panel <= title
panel <=bk

paths = {}

