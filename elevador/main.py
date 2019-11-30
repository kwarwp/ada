# ada.elevador.main.py
from _spy.vitollino.main import Cena, INVENTARIO, STYLE, Musica, NS, NOSC, Elemento as Elemento_
# from texto.main import Texto
from collections import namedtuple
Pos = namedtuple("Pos", "x, y")
STYLE.update(width=900, height=650)
PREDIO= "https://i.imgur.com/K7xS3Oa.jpg"
CESTA = "https://i.imgur.com/ouziL1K.png"
Doggie = "https://i.imgur.com/1YbsNfD.png"


class Elemento(Elemento_):
    def __init__(self, img="", vai=None, style=NS, tit="", alt="", cena=INVENTARIO,
                 score=NOSC, drag=False, drop='', **kwargs):
        super().__init__(img=img, vai=vai, style=style, tit=tit, alt=alt, cena=cena,
                         score=score, drag=drag, drop=drop, **kwargs)
        self.nome = tit
                         
    @property
    def x(self):
        # return self.elt.style.getPropertyValue("left")
        return int(self.elt.style.left[:-2])
                         
    @x.setter
    def x(self, value):
        # self.elt.style.setPropertyValue("left", value)
        self.elt.style.left = value
                         
    @property
    def y(self):
        # return self.elt.style.getPropertyValue("top")
        return int(self.elt.style.top[:-2])
                         
    @y.setter
    def y(self, value):
        # self.elt.style.setPropertyValue("top", value)
        self.elt.style.top = value

    def __le__(self, other):
        if hasattr(other, 'elt'):
            self.elt <= other.elt
        else:
            self.elt <= other

class Item:
    def __init__(self, imagem, posicao_final, **kwargs):
        self.posicao_final = posicao_final
        self.posicao = dict(x=elt.x, y=elt.y)
        self._movimenta = self._vai
        self.elt = Elemento(imagem, vai=self.movimenta, **kwargs)
        
    def movimenta(self, *_):
        self._movimenta()
        
    def _vai(self, *_):
        self._movimenta = self._volta
        self.posicao = self.posicao_final
        self.elt.x += self.posicao_final["x"]
        self.elt.y += self.posicao_final["y"]
        self.posicao = dict(x=self.elt.x, y=self.elt.y)
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        self.posicao = dict(x=0, y=0)
        self.elt.x -= self.posicao_final["x"]
        self.elt.y -= self.posicao_final["y"]
        self.posicao = dict(x=self.elt.x, y=self.elt.y)

    def __le__(self, other):
        if hasattr(other, 'elt'):
            self.elt <= other.elt
        else:
            self.elt <= other


class Passageiro(Item):
    def __init__(self, imagem, posicao_final, veiculo, cena, **kwargs):
        super().__init__(imagem, posicao_final, cena=cena, **kwargs)
        self.veiculo, self.cena = veiculo, cena
        self.posicao = Pos(self.veiculo.x - self.elt.x, self.veiculo.y - self.elt.y)
        
    def entra(self, cena):
        self.elt.entra(cena)
        
    def _vai(self, *_):
        self._movimenta = self._volta
        self.off = Pos(**self.veiculo.posicao)
        self.entra(self.veiculo.elt)
        self.elt.x = 0
        self.elt.y = 0
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        self.off = Pos(**self.veiculo.posicao)
        # self.off = Pos(self.veiculo.elt.x, self.veiculo.elt.y)
        self.entra(self.cena)
        self.elt.x = self.posicao.x + self.off.x
        self.elt.y = self.posicao.y + self.off.y



class Elevador:
    def __init__(self):
        predio = Cena(PREDIO)
        predio.vai()
        # Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
        self.cesta = Item(CESTA, dict(x=0, y=300), cena=predio, x=250, y=50,w=180,h=180)
        self.doggie = Passageiro(Doggie, dict(x=-420, y=0), veiculo=self.cesta, cena=predio, x=440, y=60)


class Elevador_:
    def __init__(self):
        predio = Cena(PREDIO)
        predio.vai()
        # Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
        self._sobe_desce = self._desce
        self._entra_sai = self._entra
        self._doggie_sobe_desce = lambda *_:None
        self._doggie_desce = lambda *_:None
        self._doggie_sobe = lambda *_:None
        self.na_cesta = "nada"
        # self.cesta = Elemento(CESTA, x=300, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.cesta = Elemento(CESTA, x=300, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.doggie = Elemento(Doggie, x=350, y=80, cena=predio, vai=self.entra_sai)
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=0)
        a = Texto(predio, "oi", foi=lambda op="YY": Texto(predio, f"escolheu {op}").vai(), A="ee", B="uu")
        a.vai()
        #b = 
        
    def sobe_desce(self, *_):
        self.cesta.y = 400
        self._sobe_desce()
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cesta.elt.style.top = 400
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cesta.elt.style.top = 100
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="sobe", ponto=0, valor=0, _level=1)
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_):
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.na_cesta="doggie"
        self.doggie.elt.style.left = 300
        # INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="entra", ponto=0, valor=0, _level=1)
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.na_cesta="nada"
        self.doggie.elt.style.left = 350
        # INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="sai", ponto=0, valor=0, _level=1)
        
Elevador()