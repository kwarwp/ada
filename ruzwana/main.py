# ada.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from collections import namedtuple
STYLE.update(width=1300, height="650px")
Elenco = namedtuple('Elenco','ator, nome, mini, alinha')
Deixa = namedtuple('Deixa','ator, fala, age')
IMGUR = "https://i.imgur.com/{}.png"
ELENCO = "z7zIJHV iJqmT9V ehoPNb1 WJ1QdZ9 yqrocJa NShlUFP".split()
class Roteiro:
    def __init__(self,cena, elenco, roteiro):
        self.elenco, self.roteiro = elenco, roteiro
        class Fala(Texto):
            def __init__(self, ator, fala, **kwarg):
                self.elenco, self.roteiro = elenco, roteiro
                super().__init__(cena,fala, **kwarg)
        


if __name__ == "__main__":
    cena = Cena(IMGUR.format(ELENCO[0])).vai()
    ymara = Elemento(IMGUR.format(ELENCO[1]), y=400, cena=cena)
    mawapi = Elemento(IMGUR.format(ELENCO[2]), y=400,x=200, cena=cena)
    wetere = Elemento(IMGUR.format(ELENCO[3]), y=400,x=400, cena=cena)
    xacria = Elemento(IMGUR.format(ELENCO[4]), y=400,x=600, cena=cena)
    kexere = Elemento(IMGUR.format(ELENCO[5]), y=400,x=800, cena=cena)
