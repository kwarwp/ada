# ada.sara.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html, alert, timer
from random import choice, shuffle
STYLE["width"], STYLE["height"] = 900, "600px"

class Kamui:
    def __init__(self):
        self.pulo = 10
        _kamui = "https://i.imgur.com/R3pCA3a.jpg"
        _okami = "https://i.imgur.com/1jSbzEj.png"
        _issun = "https://i.imgur.com/lAYKq3F.png"
        self.kamui = Cena(_kamui)
        self.okami = Elemento(_okami, cena=self.kamui)
        self.issun = Elemento(
            _issun, cena=self.kamui, style=dict(left=135, top=400, width=20, height="20px"))
        self.kamui.vai()
        def pula_issun(_=0, issun_=self.issun.elt.style):
            issun_.top = issun_.top + self.pulo
            self.pulo = -self.pulo
        timer.setinterval(300,pula_issun)

if __name__ == "__main__":
    _ = Kamui()