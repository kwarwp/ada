# ada.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import html, alert

class Canvas(Elemento):
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
        d  = self.pixd
        alert(d[0],d[1],d[2], d[3], d[4])
        return
        d[0]   = r
        d[1]   = g
        d[2]   = b
        d[3]   = a
        self.ctx.putImageData(self.pix, x, y)     
    

class Batalha:
    def __init__(self):
        STYLE["width"] = 900
        STYLE["height"] = 600
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        cena.vai()
        canvas = Canvas()
        canvas.entra(cena)
        canvas.paint(10, 10, 200, 50, 50)


if __name__ == "__main__":
    _ = Batalha()