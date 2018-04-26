# ada.roxanne.main.py
from browser import document, alert
from _spy.vitollino.main import Cena, STYLE
STYLE['width'] = 740
STYLE['min-height'] = 300

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
from _spy.vitollino.main import Cena, Elemento, Droppable


class Planta(Cena, Droppable):

    def __init__(self, *a, **k):
        Cena.__init__(self, *a, **k)
        Droppable.__init__(self, self.divesq, "regador", self.regou)

    def regou(self, *_):
        alert("Você regou a planta")


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
    rega = Elemento(wpt, style=dict(width=60, left=200, top=200), tit="regador")
    rega.entra(cenan)
    
if __name__ == "__main__":
	main()