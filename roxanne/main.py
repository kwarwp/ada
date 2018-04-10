# ada.roxanne.main.py
from browser import document
from _spy.vitollino.main import Cena, STYLE
STYLE['width'] = 740

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
from _spy.vitollino.main import Cena

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
    
if __name__ == "__main__":
	main()