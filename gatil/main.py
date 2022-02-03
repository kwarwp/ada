# ada.gatil.main.py
from _spy.vitollino.main import Cena, STYLE, Elemento, Sala, Labirinto, INVENTARIO as INV
from browser import html
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
    def __init__(self, img, lixo=NO,  gente=NO,  video=NO,  stray=NO):
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
        sala_b = Sala(*[IM.format(lnk) for lnk in SB])
        lab0 = Labirinto(sala_a, sala_b, sala_b, sala_b, sala_b)
        self.cena = c = Elemento(WIND, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        self.hero = h = Elemento(PETUNIO, x=200, y=550, w=130, h=100, cena=sala_b.norte)
        self.gatar = g = Elemento(GATAR, x=200, y=550, w=100, h=100)
        INV.bota(g)
        sala_b.norte.vai()

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
        sala_b = Sala(*[IM.format(lnk) for lnk in SB])
        lab0 = Labirinto(sala_a, sala_b, sala_b, sala_b, sala_b)
        # self.cena = c = Elemento(WIND, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        # self.rain = r = Elemento(HAIL, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        self.hero = h = Elemento(PETUNIO, x=200, y=550, w=130, h=100, cena=sala_b.norte)
        self.stray = s = Elemento(IMP.format(STRAY[0]), x=600, y=550, w=130, h=100, cena=sala_b.norte)
        # self.strays = z = Elemento(IMP.format(STRAYS[0]), x=300, y=50, w=650, h=650, cena=sala_b.norte)
        self.gatar = g = Elemento(GATAR, x=200, y=550, w=100, h=100)
        self.pix = p = Elemento(PIX, x=200, y=550, w=100, h=100)
        INV.inicia()
        INV.bota(g)
        INV.bota(p)
        sala_b.norte.vai()
    
Gatil(GATIL_MOS).vai()