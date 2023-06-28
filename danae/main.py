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
from _spy.vitollino.main import Cena, STYLE, Elemento, Salao, NADA, Labirinto
STYLE['width'] = 1350
W, H = 1350, 650
IMGSIZE, IMGHEIGHT = f"{4*W}px", f"{4*H}px"



class CenaSprite(Cena):
    def __init__(self,image, index, **kwargs):
        super().__init__(image,  **kwargs)
        # style=dict(left=x, top=x, width="80px", height="80px", overflow="hidden")
        style = dict(position="relative", left=f"-{index % 4 * W}px", top=f"-{index // 4 * H}px", width=f"{W}px",
                     height=f"{H}px", overflow="hidden")
        style.update({"min-width": IMGSIZE, "min-height": IMGHEIGHT})
        divsty = dict(STYLE)
        divsty.update({"max-width": f"{W}px", "max-height": f"{H}px", "overflow": "hidden"})
        self.elt = html.DIV(style=divsty)
        self.img = html.IMG(src=image, width=W, height=H, style=style)
        self.elt <= self.img
        self._cria_divs(W)
        
class SpriteSala(Salao):
    def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
        self.cenas = [n, l, s, o]
        self.nome = nome
        # Sala.c(**kwargs)
        self.p()

LAND = "https://i.imgur.com/Cmyq9vd.jpg"
MAPA = [{k:CenaSprite(LAND, index=v) for k, v in zip("nlso", range(l,l+4))} for l in range(0,16,4)]
#MAPA = [{k:v for k, v in zip("nlso", range(l,l+4))} for l in range(0,16,4)]
# print(MAPA)
sl = [SpriteSala(**sl) for sl in MAPA]
LABS = [{k: v for k, v in zip("cnlso", [sl[int(s)] for s in cruz])} for cruz in "03131 12020 21313 30202".split()]
lb = [Labirinto(**salas) for salas in LABS]
#c=CenaSprite(LAND, index=6)
#c.vai()
sl[0].norte.vai()
