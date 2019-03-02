# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html, alert
from random import choice, shuffle
W, H = 800, 600
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
    colonia = {}
    VIZ = [(i, j) for i in (-1,0,1) for j in (-1,0,1) if (i or j) !=0]
    def __init__(self, loc, color):
        self.color = color
        self.lugar = loc
        if self.lugar not in self.colonia:
            self.colonia[self.lugar] = self

    def create(self, loc, color=None):
        return Agro(loc, color or self.color)
            
    def match(self, other):
        return 1 if self.color == other.color else -1
            
    def vizinhos(self):
        x, y = self.lugar
        return [((i+x) % W, (j+y) % H) for i, j in self.VIZ]

    def procria(self):
        size = min(4,sum(loc.match(self) for loc in self.vizinhos() if loc in self.colonia)) + 1
        if size < 0 :
            del self.colonia[self.lugar]
            return
        viz = shuffle(list(self.VIZ))[:size]
        self.colonia.update({loc: self.create(loc) for loc in viz if loc not in self.colonia})
        

class AgroBatalha(Agro):
    arena = None

    def create(self, loc, color=None):
        if len(self.colonia) > 100:
            return
        self.arena.pinta(loc, color)
        return AgroBatalha(loc, color or self.color)

class Batalha:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        cena.vai()
        self.canvas = canvas = Canvas()
        canvas.entra(cena)
        canvas.paint(10, 10, 200, 50, 50)
        a0 = AgroBatalha([20, 20],[200, 50, 50])
        
    def pinta(self,loc, color):
        loc.extend(color)
        self.canvas.paint(*loc)


if __name__ == "__main__":
    _ = Batalha()