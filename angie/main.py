# ada.angie.main.py
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
colorPalette = ["#9B2E69", "#D93750", "#E2724F", "#F3DC7B", "#4E9397"]
from _spy.vitollino.main import Cena, STYLE, Elemento
from browser import svg
from random import randint
STYLE.update(width=1350, height="800px")
class Retangulos:
    def __init__(self):
        self.tela = svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
        self.cena = Cena(OCEANO)
        self.rects = Elemento('', x=0, y=0, w=1350, h=800, cena=self.cena)
        self.cena.vai()
        self.rects.elt <= self.tela


    def make_rects(self, maxX, maxY):
        for rect in range(1000):
            r = svg.rect(
            x=randint(0, maxX + 50) - 50,
            y=randint(0, maxY + 50) - 50,
            width=randint(0, 200) + 20,
            height=randint(0, 200) + 20,
            opacity=0.8*randint(0, 10),
            fill=colorPalette[randint(0,4)],
            transform=f"rotate({3*randint(0, 30)})"
            )
            self.tela <= r
            transform = svg.animateTransform(
            attributeName="transform",
            begin="0s",
            dur="20s",
            type="rotate",
            from="0 60 60",
            to="360 60 60",
            repeatCount="indefinite")
            r <= transform


Retangulos().make_rects(1300, 800)