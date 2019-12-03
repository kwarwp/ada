# ada.veiculo.main.py
# Este jogo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Demonstração de elementos para jogo de transporte
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.03"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
from browser import timer
STYLE["width"]=900
STYLE["height"]= "600px"
CART = "https://i.imgur.com/m2k5sv6.png"
CAT = "https://i.imgur.com/ek8oINR.png"

BASE = "https://i.imgur.com/DAUyvBP.jpg"
CENA = "https://i.imgur.com/nkwZCrR.jpg"
class Item(Elemento):
    """ Item básico que implementa funções gerais """
    def __init__(self, img="", vai=None, tit="", alt="",
                 x=0, y=0, w=100, h=100, o=1, texto='', cena=INVENTARIO):
        super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                     x=x, y=y, w=w, h=h, o=o, cena=cena)
        pass
                     

class Base(Item):
    """ Item básico que implementa funções gerais """
    def __init__(self, img="", vai=None, tit="", alt="",
                 x=0, y=0, w=100, h=100, o=1, texto='', cena=INVENTARIO):
        super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                     x=x, y=y, w=w, h=h, o=o, cena=cena)
        self.nome = "base"
                     

class Veiculo(Item):
    """ Veículo que transporta itens entre duas bases """
    def __init__(self, img="", basea, baseb, cena=INVENTARIO):
        super().__init__(img=img, w=200, h=200, cena=cena, vai= self.ir)
        self.nome = "veiculo"
        self.basea, self.baseb = basea, baseb
        self._move = self._vai
        self.elt.style.transition = "left 1s"
        self.elt.ontransitionend = self.chega
        self.x, self.y = self.basea.x-150, self.basea.y
        
    def ir(self, *_):
        self._move()
        
    def chega(self, *_):
        pass
        
    def _vai(self, *_):
        self.x, self.y = self.baseb.x+150, self.baseb.y
        self._move = self._volta
        
    def _volta(self, *_):
        self.x, self.y = self.basea.x-150, self.basea.y
        self._move = self._vai
                     

class Passageiro(Item):
    """ Item que se transporta em um veículo """
    def __init__(self, img="", basea, baseb, cena=INVENTARIO):
        super().__init__(img=img, w=100, h=100, cena=cena, vai= self.ir)
        self.nome = "passageiro"
        self.basea, self.baseb, self.cena = basea, baseb, cena
        self._move = self._vai
        self._chega = self.chegaa
        self.elt.style.transition = "left 1s, top 1s"
        self.elt.ontransitionend = self.chega
        self.x, self.y = self.basea.x+30, self.basea.y+30
        
    def ir(self, *_):
        self._move()
        
    def chega(self, *_):
        self._chega()
        
    def chegaa(self, *_):
        #self.baseb, self.basea = self.basea, self.baseb
        self.entra(self.baseb)
        
    def chegab(self, *_):
        #self.baseb, self.basea = self.basea, self.baseb
        self.entra(self.cena)
        #self.x, self.y = self.baseb.x+30, self.baseb.y+30
        self.x, self.y = 30, 30
        
    def _vai(self, *_):
        self._chega = self.chegaa
        self.x, self.y = self.baseb.x+10, self.baseb.y
        self._move = self._volta
        
    def _volta(self, *_):
        self._chega = self.chegab
        self.entra(self.cena)
        self.x, self.y = self.basea.x-self.baseb.x+30, self.basea.y-self.baseb.y+30
        self._move = self._vai
    
    
class Jogo:
    def __init__(self):
        def vai(*_):
            cart.x = 200
        def anda(*_):
            cat.x = 420
            cat.y = 300
        def entra(*_):
            cat.entra(cart)
            cat.x = 10
            cat.y = 20
            cat.vai = vai
        def sai(*_):
            cat.entra(cena)
            cat.x = cart.x+10
            cat.y = cart.y+20
            cat.elt.style.transition = "all 1s"
            cat.vai = lambda *_: None
            timer.set_timeout(saiu,1)
        def saiu(*_):
            cat.x = cart.x-100
            cat.y = cart.y+100
            cat.vai = lambda *_: None
            cat.elt.ontransitionend = lambda *_: None

        def chegou(*_):
            cat.vai = sai
        cena = Cena(CENA)
        cena.vai()
        entrada = Base(BASE, x=650, y=300, w=200, h=200, cena=cena)
        saida = Base(BASE, x=50, y=300, w=200, h=200, cena=cena)
        # cart = Veiculo(CART, x=400, y=300, w=200, h=200, cena=cena, vai=vai)
        cart = Veiculo(CART, entrada, saida, cena=cena)
        cat = Passageiro(CAT, entrada, cart, cena=cena)
        
        
Jogo()
