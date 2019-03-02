# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE

class Canvas(Elemento):
    def __init__(self):
        super().__init__(style=dict(left=0, top=0, width=900, height="600px"))


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