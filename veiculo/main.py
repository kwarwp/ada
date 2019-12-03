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
        super().__init__(img=img, w=200, h=200, cena=cena)
        self.nome = "base"
        self.basea, self.baseb = basea, baseb
        self._move = self._vai
        self.elt.ontransitionend = self.chega
        self.x, self.y = self.basea.x, self.basea.y
        
    def vai(self, *_):
        self._move()
        
    def _vai(self, *_):
        self.x, self.y = self.baseb.x, self.baseb.y
        self._move = self._volta
        
    def _volta(self, *_):
        self.x, self.y = self.basea.x, self.basea.y
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
        cat = Item(CAT, x=650, y=400, w=100, h=100, cena=cena, vai=anda)
        cart.elt.style.transition = "left 1s"
        cat.elt.style.transition = "all 1s"
        cat.elt.ontransitionend = entra
        cart.elt.ontransitionend = chegou
        
        
Jogo()
