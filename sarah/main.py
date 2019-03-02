# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html, alert
from random import choice, shuffle

class Canvas(Elemento):
    PIX = 2
    def __init__(self):
        super().__init__(style=dict(left=0, top=0, width=900, height="600px"))
        canvas = html.CANVAS()
        canvas.id     = "CursorLayer";
        canvas.width  = 800;
        canvas.height = 600;
        #canvas.style.zIndex   = 8;
        canvas.style.position = "absolute";
        canvas.style.border   = "1px solid";
        self.elt <= canvas
        self.ctx = canvas.getContext('2d')
        self.pix = self.ctx.createImageData(1,1)
        self.pixd = self.pix.data
        
    def paint(self, x, y, r, g, b, a=255):
        self.ctx.fillStyle = f"rgba({r},{g},{b},{a/255})"
        self.ctx.fillRect( x*self.PIX, y*self.PIX, self.PIX, self.PIX );
    

class Agro:
    VIZ = [(i, j) for i in (-1,0,1) for j in (-1,0,1) if (i or j) !=0]
    def __init__(self, x, y, colonia=None):
        self.colonia = colonia or {}
        self.lugar = (x, y)
        if self.lugar not in self.colonia:
            self.colonia[self.lugar] = self
            
    def vizinhos(self):
        x, y = self.lugar
        return [(i+x, j+y) for i, j in self.VIZ]

    def procria(self):
        size = sum(1 for loc in self.VIZ if loc in self.colonia
        viz = shuffle(list(self.VIZ)
        
    

class Batalha:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        cena.vai()
        canvas = Canvas()
        canvas.entra(cena)
        canvas.paint(10, 10, 200, 50, 50)


if __name__ == "__main__":
    _ = Batalha()