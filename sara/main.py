# ada.sara.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html, alert, timer
from random import choice, shuffle
STYLE["width"], STYLE["height"] = 900, "600px"

class Kamui:
    def __init__(self):
        _kamui = "https://i.imgur.com/R3pCA3a.jpg"
        self.kamui = Cena(_kamui)
        self.kamui.vai()

if __name__ == "__main__":
    _ = Kamui()