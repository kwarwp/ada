# ada.remedios.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Garrafas de remedio.

Changelog
---------

.. versionadded::    23.06

    |br| Spike das garrafinhas (26)

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from browser import document, alert, html
from _spy.vitollino.main import Cena, STYLE, Elemento
STYLE['width'] = 1000
#STYLE['height'] = "100%"

A_NORTE = "https://i.imgur.com/aLEjWgB.png"
FARMACIA = "https://i.imgur.com/9GeVtsf.jpg"
REMEDIOS = "https://i.imgur.com/2gMnd3Y.jpg"
REMEDIOA = "https://imgur.com/YiERY7h.png"
REMEDIOB = "https://i.imgur.com/AzV3ZQK.png"
REMEDIOC = "https://i.imgur.com/f5FjW4L.png"
class Remedios:
    def __init__(self):
        self.cena = Cena(FARMACIA)
        # style = "position:relative; min-width:600px; top:{}px; left:{}px;"
        # style = dict(position="relative", minWidth="600px", top="0px", left="0px", overflow="hidden")
        style = dict(position="absolute", bottom="0px", marginLeft="50px", marginBottom="110px", color="white")
        self.remedio = Elemento(REMEDIOA, x=100, y=100, w=200, h=400, texto="HIPERTENSÃO", cena=self.cena)
        self.remedio.elt <= html.DIV("HIPERTENSÃO", style=style)
        self.remedio = Elemento(REMEDIOB, x=350, y=100, w=200, h=400, cena=self.cena)
        self.remedio.elt <= html.DIV(r"ANEMIA", style=style)
        self.remedio = Elemento(REMEDIOC, x=600, y=100, w=200, h=400, cena=self.cena)
        self.remedio.elt <= html.DIV("DIABETES", style=style)
        self.cena.vai()


def main():
    Remedios()


if __name__ == "__main__":
    main()

