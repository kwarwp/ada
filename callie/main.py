from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=850, height="650px")

GOGHRoom ="https://i.imgur.com/CRNsfXO.jpg"
GOGHIntru = "https://i.imgur.com/nVpyITK.png"


class Cubos:
    def __init__(self):
        cena = Cena(GOGHRoom).vai()
        el = Elemento(GOGHIntru, cena=cena)
#Drag and drops: Elemento -> na Cena; Elemento -> Elemento; Elemento para inventário

if __name__ == "__main__":
    Cubos()



