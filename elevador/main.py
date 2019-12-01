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
    def __init__(self, imagem, posicao_final, plato=None, vai=None, **kwargs):
        self.posicao_final = posicao_final
        self.plataforma = plato or [0, 0]
        self.doca = self.plataforma[0]
        self._movimenta = self._vai
        self.movimentar = True
        self.item = lambda *_: None
        self.vai = vai or lambda *_: None
        self._ir = self.__ir
        self.elt = Elemento(imagem, vai=self.movimenta, **kwargs)
        self.posicao = dict(x=self.elt.x, y=self.elt.y)
        
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
        self.posicao = self.posicao_final
        self.elt.x += self.posicao_final["x"]
        self.elt.y += self.posicao_final["y"]
        self.posicao = dict(x=self.elt.x, y=self.elt.y)
        self.doca = self.plataforma[0]
        self.plataforma[0].aporta(self)
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        self.posicao = dict(x=0, y=0)
        self.elt.x -= self.posicao_final["x"]
        self.elt.y -= self.posicao_final["y"]
        self.posicao = dict(x=self.elt.x, y=self.elt.y)
        self.item()
        self.doca = self.plataforma[1]
        self.plataforma[1].aporta(self)

    def embarca(self, passageiro):
        passageiro.entra(self.elt.elt)
            
    def desembarca(self, passageiro):
        passageiro.entra(self.doca.elt.elt)

    def __le__(self, other):
        if hasattr(other, 'elt'):
            self.elt <= other.elt
        else:
            self.elt <= other


class Plataforma():
    def __init__(self, imagem=PLATO, **kwargs):
        # super().__init__(imagem, posicao_final, cena=cena, **kwargs)
        self.elt = Elemento(imagem, style=dict(opacity=1), **kwargs)
        self.nome = "plataforma"

    def __le__(self, other):
        other.veiculo = self.veiculo
        self.elt.elt <= other.elt.elt
        '''if hasattr(other, 'elt'):
            self.elt <= other.elt
        else:
            self.elt <= other'''
            
    def aporta(self, veiculo):
        self.doca = veiculo
            
    def veiculo(self):
        return self.doca
            
    def embarca(self, veiculo):
        veiculo.entra(self.elt.elt)
            
    def desembarca(self, veiculo):
        veiculo.entra(self.doca.elt.elt)


class Passageiro(Item):
    def __init__(self, imagem, posicao_final, veiculo, cena, **kwargs):
        super().__init__(imagem, posicao_final, cena=cena, **kwargs)
        self.veiculo, self.cena = veiculo, cena
        self.posicao = Pos(self.elt.x - self.veiculo().elt.x - posicao_final["x"],
                           self.elt.y - self.veiculo().elt.y - posicao_final["y"])
        
    def entra(self, cena):
        self.elt.entra(cena)
        
    def _vai(self, *_):
        self._movimenta = self._volta
        self._veiculo = veiculo = self.veiculo()
        self.off = Pos(**veiculo.posicao)
        # self.entra(veiculo.elt)
        veiculo.embarca(self)
        self.elt.x = self.posicao_final["x"]
        self.elt.y = self.posicao_final["y"]
        # INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _volta(self, *_):
        self._movimenta = self._vai
        veiculo = self._veiculo
        self.off = Pos(**veiculo.posicao)
        # self.off = Pos(self.veiculo.elt.x, self.veiculo.elt.y)
        # self.entra(self.cena)
        veiculo.desembarca(self)
        self.elt.x = self.posicao.x + self.off.x
        self.elt.y = self.posicao.y + self.off.y



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
        self._cesta = self.cesta0
        self.__cesta = self.cesta1
        self.cesta0.item = self.item
        self.doggie = Passageiro(Doggie, dict(x=20, y=40), cena=predio, veiculo=self.cesta, x=10, y=10)
        p0 <= self.doggie
        # self.doggie.entra(p0.elt)
                         
    def cesta(self):
        return self._cesta

    def item(self):
        self._cesta, self.__cesta = self.__cesta, self._cesta


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
        self.cesta = Elemento(CESTA, x=320, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.doggie = Elemento(Doggie, x=320, y=80, cena=predio, vai=self.entra_sai)
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