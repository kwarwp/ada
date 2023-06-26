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
STYLE['width'] = 740
#STYLE['height'] = "100%"

A_NORTE = "https://i.imgur.com/aLEjWgB.png"
FARMACIA = "https://i.imgur.com/9GeVtsf.jpg"
REMEDIOS = "https://i.imgur.com/2gMnd3Y.jpg"

class Remedios:
    def __init__(self):
        self.cena = Cena(FARMACIA)
        self.remedio = Elemento(REMEDIOS, cena=self.cena)
def _main():
    document['pydiv'].html = ""
    a_norte = Cena(img=A_NORTE)
    a_norte.vai()
Remedios()
