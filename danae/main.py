# ada.danae.main.py
""" Aventura Antartica.

Changelog
---------

.. versionadded::    23.06

    |br| Spike da Antartica (28)

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from browser import document, alert, html
from _spy.vitollino.main import Cena, STYLE, Elemento
STYLE['width'] = 1000
IMGSIZE = "3400px"
W, H = 800, 600


class CenaSprite(Cena):
    def __init__(self,image, **kwargs):
        super().__init__(image, index,  **kwargs)
        # style=dict(left=x, top=x, width="80px", height="80px", overflow="hidden")
        style = dict(position="relative", left=f"-{index % 4 * W}px", top=f"-{index // 4 * H}px", width=IMGSIZE,
                     height=IMGSIZE)
        style.update({"max-width": IMGSIZE, "max-height": IMGSIZE})
        self.elt = html.DIV(style=STYLE)
        self.img = html.IMG(src=self.img, width=width, style=style, title=nome)
        self.elt <= self.img

#STYLE['height'] = "100%"
LAND = "https://i.imgur.com/Cmyq9vd.jpg"
c=Cena(LAND, index=6)
#c.elt.width="800px"
#c.elt.style=dict(left="-800px", width="800px", minWidth="6400px")
c.vai()
