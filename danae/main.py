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
from _spy.vitollino.main import Cena, STYLE, Elemento, Salao, NADA, Labirinto, NDCT #, INVENTARIO
STYLE['width'] = 1350
W, H = 1350, 650
IMGSIZE, IMGHEIGHT = f"{4*W}px", f"{4*H}px"
ANICONS = "https://i.imgur.com/A2pPOED.png"
SNOWY = "https://i.imgur.com/KxcqKpJ.gif"
SNOW = "https://i.imgur.com/mpOU7Ca.gif"
HSNOW = "https://i.imgur.com/i5dLK8G.gif"
BSNOW = "https://i.imgur.com/4B1xuMw.gif"
SUICONS = "https://i.imgur.com/cM95ybG.jpg"
ANICONS = "https://i.imgur.com/bmUoCIb.png"

class Sprite(Elemento):
    def __init__(self, img="", vai=None, style=NDCT, tit="", alt="",
                 x=0, y=0, w=100, h=100, o=1, texto='', foi=None, index=0, sw=100, sh=100, cx=1, b=0,
                 cena="", score=NDCT, drag=False, drop={}, tipo="100% 100%", **kwargs):
        style=dict(left=x, top=x, width=f"{w}px", height=f"{h}px", overflow="hidden", filter= f"blur({b}px)")
        position = f"-{index % cx * w}px -{index // cx * w}px"
        style.update({"max-width": f"{sw}px", "max-height": f"{sh}px", "background-position": position})

        super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                 x=x, y=y, w=w, h=h, o=o, texto=texto, foi=foi,
                 cena=cena, score=NDCT, drag=drag, drop=drop, tipo=f"{sw}px {sh}px", 
                 style=style,
                 **kwargs)
        #self.style.update(style)
        #self.elt = html.DIV(Id=tit, title=tit, style=self.style)
        # self.elt.style.backgroundPosition=  "-64px -64px"
        # self.elt.style.backgroundPosition=  "-64p -64"
        # self.elt.style.update({"background-position": "-64 -64"})
        #style = dict(position="relative", left=f"-{index % cx * w}px", top=f"-{index // cx * w}px", width=f"{w}px",
        #             height=f"{h}px")
        #style.update({"min-width": f"{sw}px", "min-height": f"{sh}px"})
        # self.img.style = style

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
#Elemento(BSNOW, w=W, h=H, o=0.7, cena=sl[0].norte)
a = Sprite(ANICONS, w=64, h=64, o=0.3, index=4, sw=320, sh=256, cx=5, cena=sl[0].norte, b=2, tipo="320px 256px")


sl[0].norte.vai()
#print(a.style)
