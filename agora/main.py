# ada.agora.main.py
# Este aplicativo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Gerência de Recursos Educacionais
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.18"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
from browser import document, html

STYLE["width"]=1350
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CENA, RECT, SLATE = f"{IGR}kH1aOtS.jpg", f"{IGR}92GKogg.png", f"{IGR}pT6cuym.jpg"


class Application:
    def __init__(self):
        self.contents = document.querySelector("div.container")
        cena = Cena(CENA)
        cena.vai()
        slate = Elemento(SLATE, cena=cena)
        self.calendar()
        
    def calendar(self):
        self.contents.html = ""
        


if __name__ == "__main__":
    Application()