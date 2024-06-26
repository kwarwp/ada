# ada.libby.main.py
from _spy.vitollino.main  import Cena,Elemento, Texto, Sala, Labirinto
from _spy.vitollino.main import INVENTARIO as inv
from browser import svg, document, html, alert
from collections import namedtuple
#import collections as col
#create employee NamedTuple
Boxer = namedtuple('Boxer', ['f','x', 'y', 'w', 'h'])
NOBOX = Boxer(0, 0, 0, 100,60)

CDD="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cidade_de_Deus.jpg"
FLASH="https://pngriver.com/wp-content/uploads/2018/03/Download-Flash-PNG-Pic-For-Designing-Projects.png"
#AWESOME = "https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"
"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.2/css/fontawesome.min.css"
AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css"
FAW = html.LINK(rel="stylesheet", href=AWESOME, Type="text/css")
FAW.setAttribute("type", "text/css")
JEPPETO = "https://i.imgur.com/eI50beC.png"
document.head <= FAW
'''
class sempai():
    cdd= Cena(img=CDD)
    flash= Elemento(img=FLASH)
    flash.entra(cdd)
    cdd.vai()
#sempai()
'''

class Box:
    BOX = []
    def __init__(self, box=NOBOX):
        #Box.BOX = []
        self.box = box
        
    def paint(self, f=None, **kwargs):
        box = Box(Boxer(f=f, **kwargs))
        Box.BOX.append(box)
    def remove(self, box):
        Box.BOX.remove(box)
    def as_dict(self):
        b = self.box
        return dict(f=b.f, x=b.x, y=b.y, w=b.w, h=b.h)
    def find(self, x, y):
        for bbox in Box.BOX:
            box = bbox.box
            if (box.x < x < box.x+box.w) and (box.y < y < box.y+box.h) :
                return bbox
        return None

class Tomada(Cena, Box):
    def __init__(self, img='', box=NOBOX):
        Cena.__init__(self, img)
        Box.__init__(self, box)

class Ator(Elemento, Box):
    def __init__(self, img='', cena='', box=NOBOX):
        Elemento.__init__(self, img, cena=cena)
        Box.__init__(self, box)

class Objeto(Elemento, Box):
    def __init__(self, img='', cena='', box=NOBOX):
        Elemento.__init__(self, img, cena=cena)
        Box.__init__(self, box)

class Fala(Texto, Box):
    def __init__(self, cena='', fala='', box=NOBOX):
        Texto.__init__(self, cena, fala)
        Box.__init__(self, box)

class Quarto(Sala, Box):
    def __init__(self, img='', box=NOBOX):
        Sala.__init__(self, img)
        Box.__init__(self, box)
        
class ModelMake:
    def __init__(self):
        self.parts = dict(tomada=self.tomada, ator=self.ator, objeto=self.objeto, texto=self.texto, sala=self.sala)
        
    def paint(self, box=NOBOX, **kwargs):
        if box.f not in self.parts:
            return
        box = self.parts[box.f](box=box, **kwargs)
        Box.BOX.append(box)
        
    def tomada(self, img='', box=NOBOX):
        return Tomada(img=img, box=box)
        
    def ator(self, img='', box=NOBOX):
        return Ator(img=img, box=box)
        
    def objeto(self, img='', box=NOBOX):
        return Objeto(img=img, box=box)
        
    def texto(self, img='', box=NOBOX):
        return Fala(img=img, box=box)
        
    def sala(self, img='', box=NOBOX):
        return Quarto(img=img, box=box)


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
        Box.BOX = []
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
        canvas = self.canvas.canvas
        canvas.bind("mousedown", self.down)
        canvas.bind("mouseup", self.up)
        canvas.bind("mousemove", self.move)
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
    def paint(self, f=None, **kwargs):
        self.fill = f if f else self.fill
        shp = self.shape(**kwargs)
        self.marquee = shp
        self.canvas.canvas <= shp
        print(str(kwargs), shp)
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
        #ev.preventDefault()
        ev.stopImmediatePropagation()

        x, y = self.origin
        dx, dy = (ev.clientX- self.ox)/self.zoom+self.px, (ev.clientY- self.oy)/self.zoom+self.py
        w, h = self.size  =  dx-x, dy-y
        self.go_move = self.no_move
        self.marquee.remove()
        self.marquee = self.paint(x=0, y=0, w=0, h=0)
        if w < 2 or h < 2:
            color = ev.target.getAttribute("fill")
            box = Boxer(f=color, x=x, y=y, w=w, h=h)
            self.canvas.filler(color=color)
            self._main.select(x=dx, y=dy)
        else:
            self.canvas.paint(x=x, y=y, w=w, h=h)
        return True
        
class Main:
    def __init__(self, marker=None, painter=None, tool=None, make=None):
        self.modelmodel = make
        self.painter = painter
        self.marquee = marker
        self.tool = tool
        self.root = document["pydiv"]
        self.root.html = ""
        self.splash = html.DIV(style={
            'position':"absolute", 'left':'200px', 'top':'100px',
            'background-size': 'cover',    'background-repeat': 'no-repeat',
            'min-height':"500px", 'width':"400px",'background-image': f'url({JEPPETO})'})
        self.splash.onclick=self.main 
        self.root <= self.splash
    def main(self, _=0):
        self.root.html = ""
        self.painter = self.painter or SvgPainter(self)
        self.marquee = self.marquee or SvgMarquee(self, self.painter)
        self.tool = self.tool or ToolBox(self, self.painter)
        self.modelmodel = self.model or ModelMake(self)
        self.tool.main()
        self.marquee.main()
        return
    def filler(self, color):
        self.filling.style.color = color
    def tooler(self, ev=0, tool=0):
        self.tool.html = ""
        self.tool <= html.SPAN(Class=tool, style={'font-size':'30px', 'color':'black'})
    def paint(self, f=None, **kwargs):
        self.model.paint(f=f, **kwargs)
    def remove(self, box):
        self.model.remove(box)
    def select(self, f=None, x=-1, y=-1, **kwargs):
        box = self.model.find(x, y)
        bbox = box.as_dict() if box else None
        #print(box, bbox,">>>", [(b.box.x, b.box.y) for b in Box.BOX])
        #self.marquee.paint(x=x, y=y, w=40, h=40) if box
        self.marquee.paint(**bbox) if box else None
        
class ToolBox:
    def __init__(self, app=None, painter=None):
        nomes = "tomada ator papel texto coisa sala castelo enigma".split()
        cores = "yellow green orange red blue cyan magenta purple".split()
        self.parts = {nome: cor for zip(nomes, cores)}
        self.model = Box()
        self.painter = painter
        self.app = app
        self.tool_action = {}
    def main(self, _=0):
        self.painter = self.painter or SvgPainter(self)
        # self.menu = html.DIV(style={'position':"absolute", 'left':'10px', 'top':'100px'}) #, 'z-index': 10})
        self.menu = html.DIV(style={'position':"absolute", 'left':'-120px', 'top':'-30px'}) #, 'z-index': 10})
        self.app.root <= self.menu
        def sty(tp, bg):
            return {'position':"absolute", 'left':'0px', 'top': f'{tp}px',
            'min-height':"30px", 'width':"30px", 'background-color':bg}
        def lay(ev, cor):
            # cor = ev.target.style.backgroundColor
            cor = ev.target.title
            #cor = "orange"
            self.filler(color=cor)
            self.painter.filler(color=cor)
        colors = "transparent yellow green orange red blue cyan magenta purple".split()
        tools = ["transparent"] * 4
        ncol = len(colors)+1
        style = {}
        off = 40*ncol + 40
        self.colors = [html.DIV(title=bg, style=sty(tp, bg)) for tp, bg in zip(list(range(80, ncol*40, 40)), colors)]
        self.tools = [html.DIV(style=sty(tp, bg)) for tp, bg in zip(list(range(off, off+4*40, 40)), tools)]
        # document <= self.menu
        edit = "fa-solid fa-paintbrush"
        select = "fa-solid fa-object-group"
        zoom = "fa-solid fa-magnifying-glass"
        turnoff = "fa-solid fa-power-off"
        cena = "fa-solid fa-image"
        people = "fa-solid fa-person"
        roteiro = "fa-sharp fa-solid fa-scroll"
        texto ="fa-solid fa-comment"
        coisa = "fa-solid fa-screwdriver-wrench"
        sala = "fa-solid fa-building"
        labirinto = "fa-solid fa-castle"
        puzzle = "fa-solid fa-puzzle-piece"
        self.filling = html.SPAN(Class="fa-solid fa-fill", style={'font-size':'30px', 'color':'white'})
        #tool = html.SPAN(Class=edit, style={'font-size':'30px', 'color':'black'})
        self.tool = self.colors[0]
        self.menu <= self.filling
        self.menu <= self.tool
        self.tooler(tool=edit)
        for col, tol_ in zip(self.colors,(cena, cena, people, roteiro, texto, coisa, sala, puzzle)):
            self.menu <= col
            col <= html.SPAN(Class=tol_, style={'font-size':'30px', 'pointer-events':'none', 'color':'black','opacity':0.4})
            col.bind("click", lambda ev, color=col:lay(ev, color))
        #off = 40*ncol - 40
        actions = (self.tool_edit, self.tool_select, self.tool_zoom, self.tool_turnoff)
        for _col, _tool, _act in zip(self.tools, (edit, select, zoom, turnoff), actions):
            _col.style.top = f"{off}px"
            off+=40
            self.menu <= _col
            _col <= html.SPAN(Class=_tool, style={'font-size':'30px', 'color':'black'})
            _col.bind("click", lambda ev, tol=_tool, act=_act, it=self: it.tooler(ev=ev, tool=tol, action=act))
    def filler(self, color):
        self.filling.style.color = color
    def tooler(self, ev=0, tool=0, action=lambda *_: None):
        self.tool.html = ""
        self.tool <= html.SPAN(Class=tool, style={'font-size':'30px', 'color':'black'})
        action(ev)
    def paint(self, f=None, **kwargs):
        self.model.paint(f=f, **kwargs)
    def remove(self, box):
        self.model.remove(box)
    def tool_edit(self, ev):
        pass
    def tool_select(self, ev):
        pass
    def tool_zoom(self, ev):
        pass
    def tool_turnoff(self, ev):
        self.app.root.html = ""
    def select(self, f=None, x=-1, y=-1, **kwargs):
        box = self.model.find(x, y)
        bbox = box.as_dict() if box else None
        #print(box, bbox,">>>", [(b.box.x, b.box.y) for b in Box.BOX])
        #self.marquee.paint(x=x, y=y, w=40, h=40) if box
        self.marquee.paint(**bbox) if box else None
        
#s = SvgPainter()
#m = SvgMarquee(s)
main = Main()#.main()
'''
s.paint("b", f="yellow", x=10, y=10, w=400, h=200)
s.paint("b", f="green", x=60, y=20, w=80, h=60)
s.paint("b", f="red", x=40, y=40, w=120, h=20)
m.paint(x=40, y=40, w=120, h=20)
'''
        
