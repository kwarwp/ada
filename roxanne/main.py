# ada.roxanne.main.py
from browser import document, alert, html
from _spy.vitollino.main import Cena, STYLE
STYLE['width'] = 740
#STYLE['height'] = "100%"

A_NORTE = "https://i.imgur.com/aLEjWgB.png"

def _main():
    document['pydiv'].html = ""
    a_norte = Cena(img=A_NORTE)
    a_norte.vai()
    
# main()
m6n="https://i.imgur.com/oThg1nq.jpg"
m6n="https://i.imgur.com/oThg1nq.jpg"
g6e="https://i.imgur.com/4vjrEEG.jpg"
g6n="https://i.imgur.com/DcyUIgN.jpg"
g6s="https://i.imgur.com/TbdLoXs.jpg"
wpt="https://i.imgur.com/vc9RMEN.png"
from _spy.vitollino.main import Cena, Elemento, Droppable, Dragger


class Planta(Cena, Droppable):

    def __init__(self, *a, **k):
        Cena.__init__(self, *a, **k)
        Droppable.__init__(self, self.divesq, "regador", self.regou)

    def regou(self, *_):
        alert("Você regou a planta")
        
class Regador(Elemento, Dragger):

    def __init__(self, *a, **k):
        Elemento.__init__(self, *a, **k)
        Dragger.__init__(self, self.img)


def main():
    cenae = Cena(g6e)
    cenas = Cena(g6s)
    cenan = Planta(g6n, direita=cenae)
    cenae.direita = cenas
    cenas.esquerda = cenae
    cenae.esquerda = cenan
    cenan.esquerda = cenas
    cenas.direita = cenan
    #print(dir(cenas))
    cenan.vai()
    rega = Regador(wpt, style=dict(width=60, height=60, left=200, top=200), tit="regador")
    rega.entra(cenan)



class Folha:
    def __init__(self, size=dict(width="25%", height="25%"), pos={'left': 0, 'top': 0}):
        style = {'position': "absolute"}
        style.update(**size)
        style.update(**pos)
        fid = "folha%d" % (pos['left'])
        self.folha = html.DIV(Id=fid, style=style, draggable=True)
        tela <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"

    def drag_start(self, ev):
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'


class Suporte:
    def __init__(self, bloco, texto, certa,
        size=dict(width="25%", height="25%"), pos={'left': 0, 'top': 0}):
        style = {'position': "absolute"}
        style.update(**size)
        style.update(**pos)
        self.certa = certa
        tela <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):
        ev.preventDefault()
        src_id = ev.data['text']
        elt = document[src_id]
        elt.style.left = self.left
        elt.style.top = 100
        elt.draggable = False  # don't drag any more
        elt.style.cursor = "auto"
        certa = True
        if src_id != self.certa:
            elt.style.background = "red"
            certa = False
            self.bloco.conta_peça(certa)


class Bloco:
    def __init__(self):
        self.monta = lambda *_: None
        ordem = "10 410 310 210 110".split()
        texto = "" \
                "Era uma vez|" \
                "de nós três|" \
                "por cima|" \
                "deu um salto|" \
                "um gato pedrêz|" \
                "".split("|")
        tela = document["pydiv"]
        tela.html = ""
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, html, tela, pos * 100 + 10, "folha" + fl)
        for pos, tx in enumerate(texto):
            Folha(tx, html, tela, pos * 100 + 10)

    def inicia_de_novo(self):
        pass

    def conta_pecas(self, valor_peca):
        self.pecas_colocadas += valor_peca
        if len(self.pecas_colocadas) == 4:
            if all(self.pecas_colocadas):
                input("O texto está certo.")
            else:
                vai = input("Tentar de novo?")
                if vai == "s":
                    self.inicia_de_novo()

    def nao_monta(self):
        pass

    def vai(self):
        self.monta()
        self.monta = self.nao_monta
        # self.centro.norte.vai()


if __name__ == "__main__":
    #main()
    Bloco()