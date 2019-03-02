# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html

class Canvas(Elemento):
    def __init__(self):
        super().__init__(style=dict(left=0, top=0, width=900, height="600px"))
        canvas = html.CANVAS()
        canvas.id     = "CursorLayer";
        canvas.width  = 800;
        canvas.height = 600;
        canvas.style.zIndex   = 8;
        canvas.style.position = "absolute";
        canvas.style.border   = "1px solid";
        self.elt <= canvas
    

class Batalha:
    def __init__(self):
        STYLE["width"] = 900
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        cena.vai()
        canvas = Canvas()
        canvas.entra(cena)


if __name__ == "__main__":
    _ = Batalha()