# ada.agora.main.py
# Este aplicativo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Gerência de Recursos Educacionais
__version__ = "23.12.18" : Disponibilidade de professores
__version__ = "22.12.18" : Correlacionando entidades
__version__ = "21.12.18" : Priemeira estrutura OO
__version__ = "19.12.18" : Maquete de Visualização
"""
__author__ = "Carlo Oliveira"
__version__ = "23.12.18"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO
from browser import document, html
from random import choice, shuffle, sample
from pprint import pprint

STYLE["width"]=1350
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CENA, RECT, SLATE, FACES = f"{IGR}kH1aOtS.jpg", f"{IGR}92GKogg.png", f"{IGR}pT6cuym.jpg", f"{IGR}utEu3Ib.png"
NOME = """_ Adriana Ana Maria Sandra Juliana Antônio Carlos Francisco João José Bruna Camila Jéssica
Letícia Amanda Lucas Luiz Mateus Guilherme Pedro""".split()
NOMES = NOME[1:]
COR = """#101010 #E0BBE4 #957DAD #D291BC #FEC8D8 #FFDFD3 #B7C68B #F4F0CB #DED29E #B3A580 #929574
#85A8BA #96B6C5 #ADC4CE #9E70C9 #B3C8C8 #4CB2A1 #4F9EC4 #769ECB #9DBAD5 #8FC1A9""".split()
NOMECOR = {nome: cor for nome, cor in zip(NOME, COR)}
WD ="stqnx".split()
WDS = "seg ter qua qui sex".split()

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
        self.adiciona(self)
        
    def adiciona(self, item):
        self.lista().append(item)
        
    def atualiza(self, item):
        self.detalhe.append(item)
        
    def __str__(self):
        return self.nome
        
    def __repr__(self):
        return self.nome
        
class Pessoa(Item):
    LISTA = []
    def __init__(self, nome, turmas=None, disponibilidade=None):
        super().__init__(nome)
        self.detalhe = self.turmas = turmas or list()
        self.disponibilidade = disponibilidade or list()
        [turma.rege(self) for turma in self.turmas]
        
    def lista(self):
        return Pessoa.LISTA
        
class Sala(Item):
    LISTA = []
    def __init__(self, nome, turmas=None):
        super().__init__(nome)
        self.detalhe = self.turmas = turmas or list()
        [turma.localiza(self) for turma in self.turmas]
        
    def lista(self):
        return Sala.LISTA
        
    def aloca(self, item):
        self.turmas.append(item)
        
class Turma(Item):
    LISTA = []
    def __init__(self, nome, horarios=None, sala=None):
        super().__init__(nome)
        self.detalhe = self.horarios = horarios or list()
        self.sala = sala or list()
        [s.aloca(self) for s in self.sala]
        
    def lista(self):
        return Turma.LISTA
        
    def localiza(self, item):
        self.sala.append(item)
        [hora.localiza(item) for hora in self.horarios]
        
    def rege(self, regente):
        [hora.rege(regente) for hora in self.horarios]
        
SEMSALA = Sala("")   
SEMREGE = Pessoa("")

class Horario:
    SEG = "U"
    LISTA = []
    def __init__(self, dia, horario, segmento="U", regente=SEMREGE, sala=SEMSALA):
        self.horario = horario
        self.dia = dia
        self.regente = regente
        self.sala = sala
        sala.localiza(self) if sala.nome else None
        self.nome = f"{self.SEG}-{self.dia}-{self.horario}-{self.regente.nome}-{self.sala.nome}"
        self.LISTA.append(self)
        
    def localiza(self, item):
        self.sala = item
        self.nome = f"{self.SEG}-{self.dia}-{self.horario}-{self.regente.nome}-{self.sala.nome}"
        
    def rege(self, regente):
        self.regente = regente
        self.nome = f"{self.SEG}-{self.dia}-{self.horario}-{self.regente.nome}-{self.sala.nome}"
        
class Infantil(Horario):
    HORA = "8:00 9:30 10:00 10:05 10:35 10:40 11:10 11:15 11:45 12:00".split()
    SEG = "I"
    def __init__(self, dia, horario, segmento="I", regente=SEMREGE, sala=SEMSALA):
        super().__init__(dia, self.HORA[horario], segmento, regente, sala)
        
class Fundamental1(Horario):
    HORA = "7:30 7:45 8:35 9:25 9:40 10:30 11:20 12:10 12:15".split()
    SEG = "J"
    def __init__(self, dia, horario, segmento="J", regente=SEMREGE, sala=SEMSALA):
        super().__init__(dia, self.HORA[horario], segmento, regente, sala)
        
class Fundamental2(Horario):
    HORA = "7:20 8:00 8:50 9:40 10:00 10:20 11:10 12:00 12:50 13:00".split()
    SEG = "K"
    def __init__(self, dia, horario, segmento="K", regente=SEMREGE, sala=SEMSALA):
        super().__init__(dia, self.HORA[horario], segmento, regente, sala)
        
class Agora:
    def __init__(self, nome="agora", pessoas=None, turmas=None, salas=None, horarios=None):
        self.nome = nome
        self.turmas = turmas or Turma.LISTA
        self.pessoas = pessoas or Pessoa.LISTA
        self.salas = salas or Sala.LISTA
        self.horarios = salas or Horario.LISTA
        self.entidade = {e.__name__: e for  e in (Pessoa, Turma, Sala)}
        SEG = dict(U=Horario, I=Infantil, J=Fundamental1, K=Fundamental2)
        self.entidade.update(SEG)
        self.contents = document["pydiv"]
        self.go = True

    def limpa(self):
        self.turmas = Turma.LISTA = []
        self.pessoas = Pessoa.LISTA = []
        self.salas = Sala.LISTA = []
        self.horarios = Horario.LISTA = []
        return self

    def atualiza(self, tipo, indice, outro, **kwargs):
        self.entidade[tipo].LISTA[indice].atualiza(self.entidade[outro](**kwargs))

    def cria(self, tipo, **kwargs):
        return self.entidade[tipo](**kwargs)
        
    def seleciona_pessoa(self, ev):
        pessoa = ev.target.id[2:] if self.go else None
        self.go = not self.go
        self.mostra_disponibilidades(pessoa)
        
    def mostra_disponibilidades(self, person=None):
        def button(nome):
            nick = nome[0]
            _button = html.BUTTON(f"{nick}", Class="tile is-child is-dark is-outlined is-inverted", Id=f"b_{nome}")
            _button.style.backgroundColor = NOMECOR[nome]
            _button.onclick = self.seleciona_pessoa
            return _button
        
        def tiler(wd, tile, box):
            box <= tile
            tile <= html.BUTTON(wd.upper(), Class="tile is-child is-dark is-outlined is-inverted")
            lines = [html.DIV(Class="tile is-ancestor is-dark") for _ in range(12)]
            [tile <= div for div in lines]
            disp = [ (p.nome, tuple(range(inicio, inicio+fim)))
                    for i, p in enumerate(as_pessoas)
                    for wy, inicio, fim in p.disponibilidade if wd == wy]
            slots = {slot: [person if slot in dsp else "_" for person, dsp in disp ] for slot in range(7, 19)}
            [[lines[slot-7] <= button(person) for person in persons if (slot-7)<12] for slot, persons in  slots.items()]
            
            return (disp, slots)
        #return tiler("seg", html.DIV())
        self.contents.html = ""
        as_pessoas = [pessoa for pessoa in self.pessoas if pessoa.nome == person] if person else self.pessoas
        self.calendar = html.DIV(Class="tile is-ancestor")
        self.tiles = [(wd, html.DIV(Class="tile is-parent is-vertical", Id=f"weekday-{wd}"), html.BOX()) for wd in WDS]
        [self.calendar <= box  or tiler(wd, tile, box) for wd, tile, box in self.tiles]
        self.contents <= self.calendar
        
class Storage(Item):
    def __init__(self, nome, horarios):
        super().__init__(nome)
        self.horarios = horarios

def main():
    agora = Agora().limpa()
    HS, TS = [int(h) for h in "01234567"], "abcdefghijklmn"
    SS = TS.upper()
    SS = "fund2 agr3a agr3b agr4 agr2a nido1 agr2b nido mus1 mus2 mul idi".split()
    # print(agora.entidade)
    [agora.cria("Sala", nome=nome) for nome in SS]
    # print(agora.salas, Sala.LISTA)
    # [agora.cria("Turma", nome=nome, sala=sample(agora.salas, 3)) for nome in TS]
    [agora.cria("Turma", nome=nome, sala=sample(agora.salas, 3), horarios=[
     agora.cria(choice("IJK"), dia=choice(WDS), horario=choice(HS)) for _ in range(3)]) for nome in TS]
    [agora.cria(
        "Pessoa", nome=nome, turmas=[choice(agora.turmas)for _ in range(1, choice([2, 3]))],
        disponibilidade = [
            (wd, choice([7, 8, 9]), choice([2, 3, 4, 5, 6, 7, 8, 9]))
            for wd in sample(WDS, choice([1, 2, 3, 4]))]
        ) for nome in NOMES]
    #print(agora.mostra_disponibilidades())
    agora.mostra_disponibilidades()
    return
    
    """
    s = [Sala(nome, sample(t, 3)) for nome in SS]
    p = [Pessoa(nome, [choice(t)]) for nome in NOME]
    """
    [print(a.nome, [s.nome for s in a.sala], [h.nome for h in a.horarios]) for a in Turma.LISTA]
    # [print(a.nome, a.horarios) for a in Turma.LISTA]
    [print(a.nome, [s.nome for s in a.turmas], [d for d in a.disponibilidade]) for a in Pessoa.LISTA]
    print("-"*8, "SALAS", "-"*8)
    [print(a.nome, [s.nome for s in a.turmas]) for a in Sala.LISTA]

def _main():
    HS, TS = [int(h) for h in "0123456789"], "abcdefghijklmn"
    SS = TS.upper()
    SEG = dict(U=Horario, I=Infantil, J=Fundamental1, K=Fundamental2)
    t = [Turma(nome, [Infantil(choice("stqnx"), choice(HS)) for _ in range(3)]) for nome in TS]
    s = [Sala(nome, sample(t, 3)) for nome in SS]
    p = [Pessoa(nome, [choice(t)]) for nome in NOMES]
    
    [print(a.nome, [h.nome for h in a.horarios]) for a in Turma.LISTA]
    # [print(a.nome, a.horarios) for a in Turma.LISTA]
    [print(a.nome, [s.nome for s in a.turmas]) for a in Pessoa.LISTA]
    [print(a.nome, [s.nome for s in a.turmas]) for a in Sala.LISTA]
    
    
if __name__ == "__main__":
    # Application()
    main()