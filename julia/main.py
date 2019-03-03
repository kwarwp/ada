# ada.julia.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
IMGSIZE = "240px"

class Sprite(Elemento):
    def __init__(self, x, y, image, index=0):
        super().__init__(image, style=dict(left=x,top=x,width="80px",height="80px",overflow="hidden"))
        style = dict(position="relative",left=f"-{index%3*80}px",top=f"-{index//3*80}px", width=IMGSIZE, height=IMGSIZE)
        style.update({"max-width": IMGSIZE, "max-height": IMGSIZE})
        self.img.style=style
        



class Project:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        Buttons = "https://i.imgur.com/v6JS64Y.png"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        b0 = Sprite(10, 10, Buttons, 7)
        b0.entra(cena)
        cena.vai()


if __name__ == "__main__":
    _ = Project()