# ada.gatil.main.py
from _spy.vitollino.main import Cena, STYLE, Elemento, Sala as SalaVit, Labirinto, NADA, INVENTARIO as INV
from browser import html
from collections import namedtuple
from random import randint
P = namedtuple('Properties',"H T S G")(0, 1, 2, 3)
STYLE.update(width=1350, height="800px")
GATIL_MOS = "https://i.imgur.com/5ZISX93.jpg"
GATIL_POR = "https://i.imgur.com/Ockz2ae.png"
PETUNIO = "https://i.imgur.com/2KeouVt.png"
IM = "https://i.imgur.com/{}.jpg"
IMP = "https://i.imgur.com/{}.png"
SA = "VV1xbBG SEblwJG JVXK8gA nyly8wp".split()
SB = "NqNXbr4 2QdVrAj jvM9BQC 2KZpwVf".split()
WIND = "https://imgur.com/3LJN7lT.gif"
GATAR = "https://imgur.com/WcrEeLj.png"
STRAY = "qooCvWD SfGf1gv hlA5iCO RWc9j9Q FPWh9Nt".split()
STRAYS = "pMEwzkz llqWlNC LAUEEAj KA7r39r 8nBLnkF".split()
PIX = "https://imgur.com/0OoP7wt.jpg"
RAIN = "https://cdn.wallpapersafari.com/44/7/bvCdLK.gif"
STORM = "https://media.giphy.com/media/xT9GEDhzERbjDD15O8/giphy.gif"
FLOOD = "https://media.giphy.com/media/3HoB7BmMnKMdq/giphy.gif"
HAIL = "https://i.imgur.com/ZZ8nEkV.gif"
HALO = "https://i.imgur.com/XDuFNZw.png"
HERO = Elemento(PETUNIO, x=200, y=550, w=130, h=100)
NO = []
class Abrigo:
    GW = 1350
    GH = 800
    IW = 4000
    IH = 1000
    DW = (IW-GW)//6
    def __init__(self):
        super().__init__(img)

class Rua(Cena):
    def __init__(self, img, props=NO):
        cena = self
        class Hero(Elemento):
            def __init__(self, x=0, y=0, w=130, h=100):
                super().__init__(PETUNIO, x=x, y=y, w=w, h=h, cena=cena)
        class Trash(Elemento):
            def __init__(self, x=0, y=0, w=40, h=40):
                super().__init__(HALO, x=x, y=y, w=w, h=h, o=0.4, cena=cena)
        class Stray(Elemento):
            def __init__(self, x=0, y=0, w=80, h=80):
                #super().__init__(STRAY[randint(0,4)], x=x, y=y, w=w, h=h, cena=cena)
                super().__init__(IMP.format(STRAY[0]), x=x, y=y, w=w, h=h, cena=cena)
        class Gui(Elemento):
            def __init__(self, x=0, y=0, w=40, h=100):
                super().__init__(HALO, x=x, y=y, w=w, h=h, o=0.4, cena=cena)
        super().__init__(img)
        self.props = p ={P.H: Hero, P.T: Trash, P.S: Stray, P.G: Gui}
        [p[proname](*proargs) for proname, proargs  in props]
        self.img = img
    def vai_(self):
        super().vai()
        c0 = Elemento(self.img, x=140, y=340, w=200, h=200, cena=self)
        p0 = Elemento(GATIL_POR, x=100, y=300, w=300, h=300, cena=self)
    def vai(self, *_):
        super().vai()
        #HERO.entra(self)

class Sala(SalaVit):
    def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
        self.cenas = [Rua(img) if isinstance(img, str) else img for img in [n, l, s, o]]
        self.nome = nome
        Sala.c(**kwargs)
        self.p()

class Gatil(Cena):
    def __init__(self, img, x=0, y=0):
        super().__init__(img)
        self.img = img
        #self.elt = html.DIV(style=STYLE, )
        self.dx, self.dy = x*Abrigo.DW, y*200, 
        self.cena = c = Elemento(img, x=0, y=0, w=1350, h=800, cena=self)
        self.hero = h = Elemento(PETUNIO, x=400, y=350, w=250, h=200, cena=self)
        # self.elt.style.width = w
        c.siz = (Abrigo.IW, Abrigo.IH)
        c.pos = (-self.dx, -self.dy)
    def vai_(self):
        super().vai()
        c0 = Elemento(self.img, x=140, y=340, w=200, h=200, cena=self)
        p0 = Elemento(GATIL_POR, x=100, y=300, w=300, h=300, cena=self)
    def vai(self):
        sala_a = Sala(*[IM.format(lnk) for lnk in SA])
        sala_a.norte.vai()
        sala_b_args = [IM.format(lnk) for lnk in SB]
        sala_b_args[0] = Rua(sala_b_args[0],[
        (P.H, [200, 550]), (P.T, [540, 440]), (P.T, [840, 470]), (P.S, [1050, 550]), (P.G, [480, 400])])
        sala_b_args[1] = Rua(sala_b_args[1],[
        (P.H, [200, 550]), (P.T, [540, 440]), (P.T, [840, 470]), (P.S, [1050, 550]), (P.G, [480, 400])])
        sala_b = Sala(*sala_b_args)
        lab0 = Labirinto(sala_a, sala_b, sala_b, sala_b, sala_b)
        lab1 = Labirinto(sala_b, sala_a, sala_a, sala_a, sala_a)
        # self.cena = c = Elemento(WIND, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        # self.rain = r = Elemento(HAIL, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        # self.hero = h = Elemento(PETUNIO, x=200, y=550, w=130, h=100, cena=sala_b.norte)
        # self.stray = s = Elemento(IMP.format(STRAY[0]), x=600, y=550, w=130, h=100, cena=sala_b.norte)
        # self.strays = z = Elemento(IMP.format(STRAYS[0]), x=300, y=50, w=650, h=650, cena=sala_b.norte)
        self.gatar = g = Elemento(GATAR, x=200, y=550, w=100, h=100)
        self.pix = p = Elemento(PIX, x=200, y=550, w=100, h=100)
        INV.inicia()
        INV.bota(g)
        INV.bota(p)
        sala_b.norte.vai()
    
Gatil(GATIL_MOS).vai()