# ada.elevador.main.py
from _spy.vitollino.main import Cena, INVENTARIO, STYLE, Musica, NS, NOSC, Elemento as Elemento_
# from texto.main import Texto
from collections import namedtuple
Pos = namedtuple("Pos", "x, y")
STYLE.update(width=900, height=650)
PREDIO= "https://i.imgur.com/K7xS3Oa.jpg"
CESTA = "https://i.imgur.com/ouziL1K.png"
Doggie = "https://i.imgur.com/1YbsNfD.png"
PLATO = "http://archive.xaraxone.com/webxealot/workbook85/index_html_files/154.png"


class Elemento(Elemento_):
    def __init__(self, img="", vai=None, style=NS, tit="", alt="", cena=INVENTARIO,
                 score=NOSC, drag=False, drop='', **kwargs):
        super().__init__(img=img, vai=vai, style=style, tit=tit, alt=alt, cena=cena,
                         score=score, drag=drag, drop=drop, **kwargs)
        self.nome = tit

    def entra(self, cena, style=NOSC):
        cena <= self
                         
    @property
    def x(self):
        return int(self.elt.style.left[:-2])
                         
    @x.setter
    def x(self, value):
        self.elt.style.left = value
                         
    @property
    def y(self):
        return int(self.elt.style.top[:-2])
                         
    @y.setter
    def y(self, value):
        self.elt.style.top = value

    def __le__(self, other):
        try:
            self.elt <= other.elt
        except:
            pass

class Item:
    def __init__(self, imagem, posicao_final, plato=None, vai=None, **kwargs):
        self.nome = "veiculo"
        self.posicao_final = posicao_final
        self.plataforma = plato or [0, 0]
        self.doca = self.plataforma[0]
        self.doca.aporta(self) if self.doca else None
        self._movimenta = self._vai
        self.vai = vai or lambda *_: None
        self._ir = self.__ir
        self.elt = Elemento(imagem, vai=self.movimenta, **kwargs)        
        
    def movimenta(self, *_):
        self._ir = lambda *_: None
        self.vai()
        self._movimenta()
        self._ir = self.__ir
        
    def __ir(self, *_):
        self._ir = lambda *_: None
        self.movimenta()
        
    def ir(self, *_):
        self._ir()
        
    def _vai(self, *_):
        self._movimenta = self._volta
        self.elt.x += self.posicao_final["x"]
        self.elt.y += self.posicao_final["y"]
        self.doca = self.plataforma[1]
        self.doca.aporta(self)
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        self.elt.x -= self.posicao_final["x"]
        self.elt.y -= self.posicao_final["y"]
        self.doca = self.plataforma[0]
        self.doca.aporta(self)

    def _embarca(self, passageiro):
        passageiro.entra(self)
            
    def desembarca(self, passageiro):
        passageiro.entra(self.doca)

    def __le__(self, other):
        assert isinstance(other, Passageiro), other
        other.veiculo = self
        self.elt.elt <= other.elt.elt


class Plataforma():
    def __init__(self, imagem=PLATO, **kwargs):
        self.elt = Elemento(imagem, style=dict(opacity=1), **kwargs)
        self.nome = "plataforma"

    def __le__(self, other):
        assert isinstance(other, Passageiro), other
        other.veiculo = self
        self.elt.elt <= other.elt.elt
            
    def aporta(self, veiculo):
        self.doca = veiculo
            
    def _veiculo(self):
        return self.doca
            
    def desembarca(self, veiculo):
        veiculo.entra(self.elt)  # .elt)
            
    def embarca(self, veiculo):
        veiculo.entra(self.doca)  # .elt)


class Passageiro(Item):
    def __init__(self, imagem, posicao_final, veiculo, cena, **kwargs):
        super().__init__(imagem, posicao_final, cena=cena, **kwargs)
        self.veiculo, self.cena = veiculo, cena
        
    def entra(self, cena):
        cena <= self
        
    def _vai(self, *_):
        self._movimenta = self._volta
        self.veiculo.embarca(self)
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        self.veiculo.desembarca(self)



class Elevador:
    def __init__(self):
        predio = Cena(PREDIO)
        predio.vai()
        # Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
        self.plataforma0 = p0 = Plataforma(cena=predio, x=320, y=50,w=250,h=180)
        self.plataforma1 = p1 = Plataforma(cena=predio, x=320, y=390,w=250,h=180)
        self.cesta0 = Item(CESTA, dict(x=0, y=300),[p0, p1], cena=predio, x=150, y=50,w=180,h=180)
        self.cesta1 = Item(CESTA, dict(x=0, y=-300),[p1, p0],  cena=predio, vai=self.cesta0.ir, x=550, y=350,w=180,h=180)
        self.cesta0.vai = self.cesta1.ir
        self.doggie = Passageiro(Doggie, dict(x=20, y=40), cena=predio, veiculo=p0, x=10, y=10)
        self.doggie.entra(p0)
        
Elevador()