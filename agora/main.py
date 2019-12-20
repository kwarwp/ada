# ada.agora.main.py
# Este aplicativo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Gerência de Recursos Educacionais
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.18"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
from browser import document, html
from random import choice, shuffle
from pprint import pprint

STYLE["width"]=1350
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CENA, RECT, SLATE, FACES = f"{IGR}kH1aOtS.jpg", f"{IGR}92GKogg.png", f"{IGR}pT6cuym.jpg", f"{IGR}utEu3Ib.png"
NOME = """Adriana Ana Maria Sandra Juliana Antônio Carlos Francisco João José Bruna Camila Jéssica
Letícia Amanda Lucas Luiz Mateus Guilherme Pedro""".split()
COR = """#E0BBE4 #957DAD #D291BC #FEC8D8 #FFDFD3 #B7C68B #F4F0CB #DED29E #B3A580 #929574
#85A8BA #96B6C5 #ADC4CE #9E70C9 #B3C8C8 #4CB2A1 #4F9EC4 #769ECB #9DBAD5 #8FC1A9""".split()
NOMECOR = {nome: cor for nome, cor in zip(NOME, COR)}


class Application:
    def __init__(self):
        # self.contents = document.querySelector("div.container")
        self.contents = document["pydiv"]
        cena = Cena(CENA)
        cena.vai()
        slate = Elemento(SLATE, cena=cena)
        self.calendar()
        
    def calendar(self):
        ihour = "8:00 9:30 10:00 10:05 10:35 10:40 11:10 11:15 11:45 12:00".split()
        
        def button(hora, nome):
            _button = html.BUTTON(f"{hora} - {nome}", Class="tile is-child is-dark is-outlined is-inverted")
            _button.style.backgroundColor = NOMECOR[nome]
            return _button
        
        def tiler(wd, tile):
            nomes = NOME[:]
            shuffle(nomes)
            tile <= html.BUTTON(wd.upper(), Class="tile is-child is-dark is-outlined is-inverted")
            [tile <= button(hora, nome) for hora, nome in zip(ihour, nomes)]
        self.contents.html = ""
        self.calendar = html.DIV(Class="tile is-ancestor")
        weekdays = "seg ter qua qui sex".split()
        self.tiles = [(wd, html.DIV(Class="tile is-parent is-vertical", Id=f"weekday-{wd}")) for wd in weekdays]
        [self.calendar <= tile  or tiler(wd, tile) for wd, tile in self.tiles]
        self.contents <= self.calendar
        
class Item:
    def __init__(self, nome):
        self.nome = nome
        self._lista = []
        self.adiciona(self)
        
    def adiciona(self, item):
        self.lista.append(Item)
        
    def atualiza(self, item):
        self.detalhe.append(Item)
        
class Pessoa(Item):
    LISTA = []
    def __init__(self, nome, turmas=None):
        super().__init__(nome)
        self.detalhe = self.turmas = turmas or list()
        
    @property
    def lista(self):
        return Pessoa.LISTA
        
class Sala(Item):
    LISTA = []
    def __init__(self, nome, turmas=None):
        super().__init__(nome)
        self.detalhe = self.turmas = turmas or list()
        
    @property
    def lista(self):
        return Sala.LISTA
        
class Turma(Item):
    LISTA = []
    def __init__(self, nome, horarios=None):
        super().__init__(nome)
        self.detalhe = self.horarios = horarios or list()
        
    @property
    def lista(self):
        return Turma.LISTA
        
class Horario:
    def __init__(self, dia, horario, segmento="U", regente="I", sala=0):
        self.nome = f"{segmento}-{dia}-{horario}-{regente}-{sala}"
        self.horario = horario
        self.dia = dia
        self.regente = regente
        self.sala = sala
        
class Infantil(Horario):
    HORA = "8:00 9:30 10:00 10:05 10:35 10:40 11:10 11:15 11:45 12:00".split()
    def __init__(self, dia, horario, segmento="I", regente="I", sala=0):
        super().__init__(dia, horario, segmento, regente, sala)
        
class Fundamental1(Horario):
    HORA = "7:30 7:45 8:35 9:25 9:40 10:30 11:20 12:10 12:15".split()
    def __init__(self, dia, horario, segmento="J", regente="I", sala=0):
        super().__init__(dia, horario, segmento, regente, sala)
        
class Fundamental2(Horario):
    HORA = "7:20 8:00 8:50 9:40 10:00 10:20 11:10 12:00 12:50 13:00".split()
    def __init__(self, dia, horario, segmento="K", regente="I", sala=0):
        super().__init__(dia, horario, segmento, regente, sala)
        
class Agora(Item):
    def __init__(self, nome="agora", pessoas=None, turmas=None, salas=None):
        super().__init__(nome)
        self.turmas = turmas
        
class Storage(Item):
    def __init__(self, nome, horarios):
        super().__init__(nome)
        self.horarios = horarios

def main():
    Turma.LISTA = []
    HS, TS = [int(h) for h in "0123456789"], "abcdefghijklmn"
    SS = TS.upper()
    t = [Turma(nome, [Horario(choice("stqnx"), choice(HS), sala=choice(SS)) for _ in range(3)]) for nome in TS]
    p = [Pessoa(nome) for nome in NOME]
    
    [print(a.nome, [h.nome for h in a.horarios]) for a in t] # Turma.LISTA]
    [print(a.nome, a.turmas) for a in p]
    
    
if __name__ == "__main__":
    # Application()
    main()