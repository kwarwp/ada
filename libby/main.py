# ada.libby.main.py
from _spy.vitollino.main  import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
from browser import svg, document
CDD="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cidade_de_Deus.jpg"
FLASH="https://pngriver.com/wp-content/uploads/2018/03/Download-Flash-PNG-Pic-For-Designing-Projects.png"
class sempai():
    cdd= Cena(img=CDD)
    flash= Elemento(img=FLASH)
    flash.entra(cdd)
    cdd.vai()
#sempai()

class Box:
    def __init__(self, box):
        self.box = box
    def paint(self, box):
        self.box = box


class SvgPainter:
    def __init__(self):
        self.shape = dict(b=lambda x, y, w, h, it=self: svg.rect(x=x, y=y, width=w, height=h, fill=it.fill, fill_opacity=it.opacity))
        self.root = root = document["pydiv"]
        root.html = ""
        self.canvas = svg.svg(viewBox="0 0 1200 650", width=1200, height=650)
        root <= self.canvas
        self.fill = "white"
        self.opacity = 1
        self.screen = self.paint("b", x=0, y=0, w=1200, h=650)
        self.fill = "red"
        self.opacity = 0.5
    def paint(self, shape="b", f=None, **kwargs):
        self.fill = f if f else self.fill
        shp = self.shape[shape](**kwargs)
        self.canvas <= shp
        return shp
        #shp.setAttribute("fill-opacity", self.opacity)
    def filler(self, color="red", op=0.5):
        self.fill = color
        self.opacity = op


class SvgMarquee:
    def __init__(self, canvas, stroke="grey", dash="4 1"):
        self.canvas = canvas
        self.origin, self.size = (0,0), (0,0)
        self.go_move = self.no_move
        document.bind("click", self.click)
        rect = self.canvas.canvas.getBoundingClientRect()
        self.ox, self.oy = rect.left, rect.top
        self.fill = None
        self.stroke, self.dash = stroke, dash
        self.opacity = 0.8
        self.shape = lambda x, y, w, h, it=self: svg.rect(x=x, y=y, width=w, height=h, fill=it.fill, fill_opacity=it.opacity,
        stroke=it.stroke, stroke_dasharray=it.dash, stroke_width=2)
        document.bind("mousedown", self.down)
        document.bind("mouseup", self.up)
        document.bind("mousemove", self.move)
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
        #stroke=it.stroke, stroke_width=2)
    def paint(self, f=None, **kwargs):
        self.fill = f if f else self.fill
        shp = self.shape(**kwargs)
        self.canvas.canvas <= shp
        return shp
        #shp.setAttribute("fill-opacity", self.opacity)
    def fill(self, color="red", op=0.5):
        self.fill = color
        self.opacity = op
    def click(self, ev):
        x, y = ev.clientX- self.ox, ev.clientY- self.oy
        rect = ev.target
        self.canvas.filler(color=rect.getAttribute("fill"))
        #self.paint(x=x, y=y, w=20, h=20)
    def down(self, ev):
        self.origin = ev.clientX- self.ox, ev.clientY- self.oy
        self.go_move = self.do_move
        #self.paint(x=x, y=y, w=20, h=20)
    def no_move(self, ev):
        pass
    def move(self, ev):
        self.go_move(ev)
    def do_move(self, ev):
        x, y = self.origin
        w, h = self.size  = ev.clientX- self.ox -x, ev.clientY- self.oy-y
        self.marquee.remove()
        self.marquee = self.paint(x=x, y=y, w=w, h=h)
    def up(self, ev):
        x, y = self.origin
        w, h = self.size  = ev.clientX- self.ox -x, ev.clientY- self.oy-y
        self.go_move = self.no_move
        self.canvas.paint(x=x, y=y, w=w, h=h)
        self.marquee.remove()
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
        
s = SvgPainter()
m = SvgMarquee(s)
s.paint("b", f="yellow", x=10, y=10, w=400, h=200)
s.paint("b", f="green", x=60, y=20, w=80, h=60)
s.paint("b", f="red", x=40, y=40, w=120, h=20)
m.paint(x=40, y=40, w=120, h=20)
        
