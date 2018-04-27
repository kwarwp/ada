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
oce = "https://i.imgur.com/oDqeaBp.jpg"
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
    def __init__(self, bloco, left=0, top=0,
        size=dict(width="100px", height="100px")):
#        size=dict(width="25%", height="25%")):
        style = {'position': 'absolute', 'overflow': 'hidden', 'margin':'1%'}
        image_style = {'position': "relative", 'width': '400px', 'height': '400px'}
        w, h = int(size['width'][:-2])+10, int(size['height'][:-2])+10
        style.update(size)
        style.update(left="%dpx" % (left*w), top="%dpx" % (top*h))
        image_style.update(left="%dpx" % (-left*w), top="%dpx" % (-top*h))
        fid = "folha%d" % (10*top+left)
        self.folha = html.DIV(Id=fid, style=style, draggable=True)
        self.folha <= html.IMG(Id="img"+fid, src=bloco.img, style=image_style)
        
        bloco.folha <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"

    def drag_start(self, ev):
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'


class Suporte:
    def __init__(self, bloco, certa, left=0, top=0,
        size=dict(width="25%", height="25%")):
        style = {'position': "absolute", 'overflow': 'hidden'}
        w, h = int(size['width'][:-1]), int(size['height'][:-1])
        style.update(size)
        style.update(left="%d%%" % (left*w), top="%d%%" % (top*h))
        self.certa = certa
        self.folha = html.DIV(style=style)
        bloco.suporte <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        elt = document[src_id]
        #elt.style.left = self.left
        #elt.style.top = self.top
        # elt.draggable = False  # don't drag any more
        self.folha <= elt
        elt.style.cursor = "auto"
        certa = True
        if src_id != self.certa:
            elt.style.background = "red"
            certa = False
            self.bloco.conta_pecas(certa)


class Bloco:
    def __init__(self, img):
        self.img = img
        self.monta = lambda *_: None
        ordem = ["%02d"%x for x in range(1)]
        self.tela = document["pydiv"]
        self.suporte = html.DIV(style=dict(position="absolute", left=10, top=20, width=400, height='%dpx'%400))
        self.folha = html.DIV(style=dict(position="absolute",
        left=410, top=20, width=450, height='%dpx'%450))
        self.tela.html = ""
        self.tela <= self.suporte
        self.tela <= self.folha
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, "folha" + fl, pos//4, pos%4)
        for pos, tx in enumerate(ordem):
            Folha(self, pos//4, pos%4)

    def inicia_de_novo(self):
        pass

    def conta_pecas(self, valor_peca):
        self.pecas_colocadas += valor_peca
        if len(self.pecas_colocadas) == 4:
            if all(self.pecas_colocadas):
                input("O texto estÃÂÃÂÃÂÃÂ¡ certo.")
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
    Bloco(oce)