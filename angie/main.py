# ada.angie.main.py
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
colorPalette = ["#9B2E69", "#D93750", "#E2724F", "#F3DC7B", "#4E9397"]
from _spy.vitollino.main import Cena, STYLE
from browser import svg
STYLE.update(width=1350, height="800px")
class Retangulos:
    def __init__(self):
        self.tela = svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
        self.cena = Cena(OCEANO)
        self.cena.vai()
        self.cena.elt <= self.rubish


    def make_rects(maxX, maxY):
        for rect in range(100):
            r = svg.rect(
            x=randint(0, maxX + 50) - 50,
            y=randint(0, maxY + 50) - 50,
            width=randint(0, 200) + 20,
            height=randint(0, 200) + 20,
            opacity=0.8*randint(0, 10),
            fill=colorPalette[randint(0,5)]
            )
            self.tela <= r

Retangulos().make_rects(1000, 800)