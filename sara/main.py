# ada.sara.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from browser import html, alert, timer
from random import choice, shuffle
STYLE["width"], STYLE["height"] = 900, "600px"

class Kamui:
    def __init__(self):
        self.pulo = -10
        self.issun_top = 380
        _kamui = "https://i.imgur.com/R3pCA3a.jpg"
        _okami = "https://i.imgur.com/1jSbzEj.png"
        _issun = "https://i.imgur.com/lAYKq3F.png"
        self.kamui = Cena(_kamui)
        self.okami = Elemento(_okami, cena=self.kamui, tit="Essa é a Deusa Amaterasu")
        self.issun = Elemento(
            _issun, cena=self.kamui, style=dict(left=135, top=400, width=20, height="20px"),
            tit="Issun - O artista intinerante")
        self.kamui.vai()
        def pula_issun(_=0, issun_=self.issun.elt.style):
            issun_.top = self.issun_top + self.pulo
            self.pulo = -self.pulo
        self.pula_issun = timer.set_interval(pula_issun, 300)
        def para_issun(_=0):
            Texto(self.kamui, tit="Issun - O artista intinerante", txt="Essa é a história da deusa Amaterasu").vai()
            timer.clear_interval(self.pula_issun)
        self.issun.vai = para_issun

if __name__ == "__main__":
    _ = Kamui()