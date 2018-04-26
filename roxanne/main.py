# ada.roxanne.main.py
from browser import document
from _spy.vitollino.main import Cena, STYLE
STYLE['width'] = 740
#STYLE['min-height'] = 740

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



"""
class Regador(Cena, Droppable):

    def __init__(self, img, esquerda):
        self.pega = Cena(vai=self.pega_card)
        Cena.__init__(self, img=img, esquerda=esquerda)
        Droppable.__init__(self, self.divmeio, "card", self.passa_card)

    def vai_meio(self, _=0):
        if self.passou:
            alert("Você precisa encostar o passe no leitor")
        else:
            alert("Você está sem o passe, volte para buscar")

    def passa_card(self, _=0, __=0):
        if Card.passou:
            alert("Você segue para o seu destino")
        else:
            alert("Você está sem o passe, volte para buscar")
"""

def main():
    cenae = Cena(g6e)
    cenas = Cena(g6s)
    cenan = Cena(g6n, direita=cenae)
    cenae.direita = cenas
    cenas.esquerda = cenae
    cenae.esquerda = cenan
    cenan.esquerda = cenas
    cenas.direita = cenan
    cenan.vai()
    rega = Elemento(wpt, style=dict(width=60, left=200, top=200))
    rega.entra(cenan)
    
if __name__ == "__main__":
	main()