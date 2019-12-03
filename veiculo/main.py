# ada.veiculo.main.py
# Este jogo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Demonstração de elementos para jogo de transporte
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.03"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
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
            cat.x = cart.x-100
            cat.y = cart.y+100
            cat.vai = lambda *_: None
        def chegou(*_):
            cat.vai = sai
        cena = Cena(CENA)
        cena.vai()
        entrada = Base(BASE, x=650, y=300, w=200, h=200, cena=cena)
        saida = Base(BASE, x=50, y=300, w=200, h=200, cena=cena)
        cart = Base(CART, x=400, y=300, w=200, h=200, cena=cena, vai=vai)
        cat = Item(CAT, x=650, y=400, w=100, h=100, cena=cena, vai=anda)
        cart.elt.style.transition = "left 1s"
        cat.elt.style.transition = "all 1s"
        cat.elt.ontransitionend = entra
        cart.elt.ontransitionend = chegou
        
        
Jogo()
