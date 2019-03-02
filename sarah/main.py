# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE


class Batalha:
    def __init__(self):
        STYLE["width"] = 900
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        cena.vai()


if __name__ == "__main__":
    _ = Batalha()