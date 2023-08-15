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

ray = 100
values = [20,10,30,15,25]

colors = ["C8E0A2", "A6BED1", "E4CC85", "D7D7D7", "90AF97", "698EA8",
        "BFA166", "A8ADB0", "FF6600"]

panel = document["pydiv"]
legend = None
print(svg.text)
title = svg.text("", x=150, y=25,
    font_size=22, text_anchor="middle",
    style={"stroke": "black"})
panel <= title

paths = {}

