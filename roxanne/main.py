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
        alert("VocÃª regou a planta")
        
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
    rega = Regador(wpt, style=dict(width=60, height=60, left=200, top=200),
                   tit="regador")
    rega.entra(cenan)



class Folha:
    def __init__(self, bloco, left=0, top=0, ileft=0, itop=0,
                 size=dict(width=100, height=100)):
        self.suporte = None
        w, h = size.values()
        ileft, itop = "%dpx" % (ileft*w), "%dpx" % (itop*h)
        style = {'position': 'absolute', 'overflow': 'hidden',
                'background-image': 'url({})'.format(bloco.img),
                'background-position': '{} {}'.format(ileft, itop),
                'background-size': '{}px {}px'.format(*bloco.size),
        }
        style.update({k:'{}px'.format(v) for k, v in size.items() })
        style.update(left="%dpx" % (left*(w+10)), top="%dpx" % (top*(h+10)))
        fid = "folha%d" % (10*top+left)
        self.folha = html.DIV(Id=fid, style=style, draggable=True)        
        bloco.folha <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over
        bloco.folhas[fid]=self

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"
        return False

    def img_drag_start(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        return False

    def drag_start(self, ev):
        ev.stopPropagation()
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'
        return False

    def troca(self, suporte):
        self.folha.style.left = 0
        self.folha.style.top = 0
        suporte.recebe(self, self.suporte)
        self.suporte = suporte
        self.folha.style.cursor = "auto"


class Suporte:
    def __init__(self, bloco, certa, left=0, top=0,
                 size=dict(width="25%", height="25%")):
        self.ladrilho = None
        style = {'position': "absolute", 'overflow': 'hidden',
                 'border':'1px solid MidnightBlue'}
        w, h = float(size['width'][:-1]), float(size['height'][:-1])
        style.update(size)
        style.update(left="%d%%" % (left*w), top="%d%%" % (top*h))
        self.certa = certa
        self.folha = html.DIV(style=style)
        bloco.suporte <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def recebe(self, folha, suporte):
        if folha:
            self.folha <= folha.folha
            self.folha.style.border=0
        else:
            self.folha.style.border='1px solid MidnightBlue'

        suporte.recebe(self.ladrilho, None) if suporte else None
        self.ladrilho = folha

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
        return False

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        self.bloco.folhas[src_id].troca(self) 
        """
        certa = True
        if src_id != self.certa:
            elt.style.background = "red"
            certa = False
            self.bloco.conta_pecas(certa)
        """
        #return False


class Bloco:
    def __init__(self, img, nx=4, ny=4, w=400, h=400):
        self.img = img
        *self.size = w, h
        self.folhas = {}
        self.monta = lambda *_: None
        # ordem = ["%02d"%x for x in range(nx*ny)]
        ordem = list(range(nx*ny))
        desordem = ordem[:]
        from random import shuffle
        shuffle(desordem)
        self.tela = document["pydiv"]
        self.suporte = html.DIV(style=dict(position="absolute",
        left=10, top=20, width=w, height='%dpx'%h, border=1,
        borderColor="slategrey"))
        self.folha = html.DIV(style=dict(position="absolute",
        left=w+20, top=20, width=w+nx*10, height='%dpx'%(h+ny*10)))
        self.tela.html = ""
        self.tela <= self.suporte
        self.tela <= self.folha
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, "folha%02d" % fl, pos//nx, pos%nx,
                    size=dict(width='{}%'.format(100/nx),
                    height='{}%'.format(100/ny)))
        for pos, tx in enumerate(desordem):
            Folha(self, pos//nx, pos%nx, int(tx)//nx, int(tx)%nx,
                    size=dict(width=w//nx, height=h/ny))

    def inicia_de_novo(self):
        pass

    def conta_pecas(self, valor_peca):
        self.pecas_colocadas += valor_peca
        if len(self.pecas_colocadas) == 4:
            if all(self.pecas_colocadas):
                input("O texto estÃ¡ certo.")
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
    Bloco(oce, 2, 2)