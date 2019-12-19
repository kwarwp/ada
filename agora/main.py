# ada.agora.main.py
# Este aplicativo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Gerência de Recursos Educacionais
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.18"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
from browser import document, html
from random import choice, shuffle

STYLE["width"]=1350
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CENA, RECT, SLATE, FACES = f"{IGR}kH1aOtS.jpg", f"{IGR}92GKogg.png", f"{IGR}pT6cuym.jpg", f"{IGR}utEu3Ib.png"
NOME = """Adriana Ana Maria Sandra Juliana Antônio Carlos Francisco João José Bruna Camila Jéssica
Letícia Amanda Lucas Luiz Mateus Guilherme Pedro"""


class Application:
    def __init__(self):
        # self.contents = document.querySelector("div.container")
        self.contents = document["pydiv"]
        cena = Cena(CENA)
        cena.vai()
        slate = Elemento(SLATE, cena=cena)
        self.calendar()
        
    def calendar(self):
        ihour = "8:00 9:30 10:00 10:05 10:35 10:40 11:10 11:15 11:45 12:00".split()
        
        def tiler(wd, tile):
            nomes = NOMES[:]
            shuffle(nomes)
            tile <= html.BUTTON(wd.upper(), Class="tile is-child is-dark is-outlined is-inverted")
            [tile <= html.BUTTON(f"{hora} - {nome}", Class="tile is-child is-dark is-outlined is-inverted")
            for hora, nome in zip(ihour, nomes)]
        self.contents.html = ""
        self.calendar = html.DIV(Class="tile is-ancestor")
        weekdays = "seg ter qua qui sex".split()
        self.tiles = [(wd, html.DIV(Class="tile is-parent is-vertical", Id=f"weekday-{wd}")) for wd in weekdays]
        [self.calendar <= tile  or tiler(wd, tile) for wd, tile in self.tiles]
        self.contents <= self.calendar
        


if __name__ == "__main__":
    Application()