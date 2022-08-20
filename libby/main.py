# ada.libby.main.py
from _spy.vitollino.main  import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
from browser import svg, document, html, alert
from collections import namedtuple
#import collections as col
#create employee NamedTuple
Boxer = namedtuple('Boxer', ['f','x', 'y', 'w', 'h'])

CDD="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cidade_de_Deus.jpg"
FLASH="https://pngriver.com/wp-content/uploads/2018/03/Download-Flash-PNG-Pic-For-Designing-Projects.png"
#AWESOME = "https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"
"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.2/css/fontawesome.min.css"
AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css"
FAW = html.LINK(rel="stylesheet", href=AWESOME, Type="text/css")
FAW.setAttribute("type", "text/css")
JEPPETO = "https://i.imgur.com/eI50beC.png"
document.head <= FAW
class sempai():
    cdd= Cena(img=CDD)
    flash= Elemento(img=FLASH)
    flash.entra(cdd)
    cdd.vai()
#sempai()

class Box:
    BOX = []
    def __init__(self, box=None):
        self.box = box
        
    def paint(self, f=None, **kwargs):
        self.box = Boxer(f=f, **kwargs)
        Box.BOX.append(self)
    def remove(self, box):
        Box.BOX.remove(box)
    def find(self, x, y):
        for box in Box.BOX:
            if (box.x < x < box.x+w) and (box.y < y < box.y+h) :
                return box
        return None
CW, CH = 1200, 650
Z = 5
PX, PY = 20, 20

class SvgPainter:
    def __init__(self, main):
        self._main= main
        self.shape = dict(b=lambda x, y, w, h, it=self: svg.rect(
            x=x, y=y, width=w, height=h, fill=it.fill, fill_opacity=it.opacity))
        self.root = root = document["pydiv"]
        root.html = ""
        self.canvas = svg.svg(viewBox=f"{PX} {PY} {CW/Z} {CH/Z}", width=1200, height=650)
        root <= self.canvas
        self.fill = "white"
        self.opacity = 1
        self.screen = self.paint("b", x=0, y=0, w=1200, h=650)
        self.fill = "red"
        self.opacity = 0.5
    def paint(self, shape="b", f=None, **kwargs):
        self.fill = f if f else self.fill
        self._main.paint(f=f, **kwargs)
        shp = self.shape[shape](**kwargs)
        self.canvas <= shp
        return shp
        #shp.setAttribute("fill-opacity", self.opacity)
    def filler(self, color="red", op=0.5):
        self.fill = color
        self.opacity = op


class SvgMarquee:
    def __init__(self, main, canvas, stroke="grey", dash="4 1"):
        self.zoom = Z
        self._main = main
        self.px, self.py = PX, PY
        self.canvas = canvas
        self.origin, self.size = (0,0), (0,0)
        self.go_move = self.no_move
        #document.bind("click", self.click)
        rect = self.canvas.canvas.getBoundingClientRect()
        self.ox, self.oy = rect.left, rect.top
        self.vbox = self.canvas.canvas.viewBox
        self.fill = None
        self.stroke, self.dash = stroke, dash
        self.opacity = 0.8
        self.shape = lambda x, y, w, h, it=self: svg.rect(x=x, y=y, width=w, height=h, fill=it.fill, fill_opacity=it.opacity,
        stroke=it.stroke, stroke_dasharray=it.dash, stroke_width=2)
        #stroke=it.stroke, stroke_width=2)
    def main(self):
        document.bind("mousedown", self.down)
        document.bind("mouseup", self.up)
        document.bind("mousemove", self.move)
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
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
        pass #self go_click(ev)
    def down(self, ev):
        #self.origin = ev.clientX- self.ox, ev.clientY- self.oy
        self.origin = (ev.clientX- self.ox)/self.zoom+self.px, (ev.clientY- self.oy)/self.zoom+self.py
        self.go_move = self.do_move
        #self.paint(x=x, y=y, w=20, h=20)
    def no_move(self, ev):
        pass
    def move(self, ev):
        self.go_move(ev)
    def do_move(self, ev):
        x, y = self.origin
        w, h = self.size  = (ev.clientX- self.ox)/self.zoom -x+self.px, (ev.clientY- self.oy)/self.zoom-y+self.py
        self.marquee.remove()
        self.marquee = self.paint(x=x, y=y, w=w, h=h)
    def up(self, ev):
        x, y = self.origin
        w, h = self.size  = (ev.clientX- self.ox)/self.zoom -x+self.px, (ev.clientY- self.oy)/self.zoom-y+self.py
        self.go_move = self.no_move
        if w < 2 or h < 2:
            color = ev.target.getAttribute("fill")
            self.canvas.filler(color=color)
            self._main.filler(color=color)
        self.canvas.paint(x=x, y=y, w=w, h=h)
        self.marquee.remove()
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
        
class Main:
    def __init__(self, marker=None, painter=None):
        self.model = Box()
        self.painter = painter or SvgPainter(self)
        self.marquee = marker or SvgMarquee(self, self.painter)
        vai = Cena(vai=self.main)
        Cena(JEPPETO, esquerda=vai, meio=vai, direita=vai).vai()
    def main(self, _=0):
        self.marquee.main()
        self.menu = html.DIV(style={'position':"absolute", 'left':'10px', 'top':'100px', 'z-index': 10})
        def sty(tp, bg):
            return {'position':"absolute", 'left':'0px', 'top': f'{tp}px',
            'min-height':"30px", 'width':"30px", 'background-color':bg}
        def lay(ev):
            cor = ev.target.style.backgroundColor
            self.filler(color=cor)
            self.painter.filler(color=cor)
        colors = "transparent yellow green red blue black peru".split()
        tools = ["transparent"] * 4
        ncol = len(colors)+1
        style = {}
        off = 40*ncol + 40
        self.colors = [html.DIV(style=sty(tp, bg)) for tp, bg in zip(list(range(80, ncol*40, 40)), colors)]
        self.tools = [html.DIV(style=sty(tp, bg)) for tp, bg in zip(list(range(off, off+4*40, 40)), tools)]
        document <= self.menu
        edit = "fa-solid fa-paintbrush"
        select = "fa-solid fa-object-group"
        zoom = "fa-solid fa-magnifying-glass"
        self.filling = html.SPAN(Class="fa-solid fa-fill", style={'font-size':'30px', 'color':'white'})
        #tool = html.SPAN(Class=edit, style={'font-size':'30px', 'color':'black'})
        self.tool = self.colors[0]
        self.menu <= self.filling
        self.menu <= self.tool
        self.tooler(tool=edit)
        for col in self.colors:
            self.menu <= col
            col.bind("click", lay)
        #off = 40*ncol - 40
        for _col, _tool in zip(self.tools, (edit, select, zoom)):
            _col.style.top = f"{off}px"
            off+=40
            self.menu <= _col
            _col <= html.SPAN(Class=_tool, style={'font-size':'30px', 'color':'black'})
            _col.bind("click", lambda ev, tol=_tool, it=self: it.tooler(ev=ev, tool=tol))
    def filler(self, color):
        self.filling.style.color = color
    def tooler(self, ev=0, tool=0):
        self.tool.html = ""
        self.tool <= html.SPAN(Class=tool, style={'font-size':'30px', 'color':'black'})
    def paint(self, f=None, **kwargs):
        self.model.paint(f=f, **kwargs)
        
#s = SvgPainter()
#m = SvgMarquee(s)
main = Main().main()
'''
s.paint("b", f="yellow", x=10, y=10, w=400, h=200)
s.paint("b", f="green", x=60, y=20, w=80, h=60)
s.paint("b", f="red", x=40, y=40, w=120, h=20)
m.paint(x=40, y=40, w=120, h=20)
'''
        
