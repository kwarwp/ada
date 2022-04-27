# ada.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from collections import namedtuple
STYLE.update(width=1300, height="650px")
Ator = namedtuple('Elenco','ator nome mini alinha')
Fala = namedtuple('Fala','ator fala age')
A = namedtuple('Ali','e m d')(-1, 0, 1)
IMGUR = "https://i.imgur.com/{}.png"
ELENCO = "z7zIJHV iJqmT9V ehoPNb1 WJ1QdZ9 yqrocJa NShlUFP".split()
yma, maw, wet, xac, ker = "Ymara Guajajara|Maria Wapichana|Weteré ParkatêJê|Celia Xacriabá|Kerexu Yxapyry".split("|")
nomes = [yma, maw, wet, xac, ker]


class Roteiro:
    def __init__(self,cena, elenco, roteiro):
        self.elenco, self.roteiro = elenco, roteiro
        script = self
        for ator in elenco:
            ator.ator.vai = self.nada
            ator.ator.tit = ator.nome
        elenco.pop(0).ator.vai = self.segue
        class Falar(Texto):
            def __init__(self, ator, fala, **kwarg):
                self.ator, self.fala = ator, fala
                super().__init__(cena,fala, **kwarg)
                def foi(self, *_):
                    super().foi()
                    script.segue()
        self._fala = Falar
        
    def nada(self, *_):
        pass
        
    def segue(self, *_):
        ator, fala, action = self.scripter()
        self._fala(ator, fala).vai()
        if action:
            action.vai = self.segue
        
        
    def scripter(self, *_):
        '''# scp = (fal for fal in self.roteiro)
        scp = iter([fal for fal in self.roteiro])
        scp = [fal for fal in self.roteiro]
        #yield next(scp)
        a, b, c = scp.pop(0)
        yield (a, b, c)'''
        return self.roteiro.pop(0)


if __name__ == "__main__":
    cena = Cena(IMGUR.format(ELENCO[0])).vai()
    ymara = Elemento(IMGUR.format(ELENCO[1]), y=400, cena=cena)
    mawapi = Elemento(IMGUR.format(ELENCO[2]), y=400,x=200, cena=cena)
    wetere = Elemento(IMGUR.format(ELENCO[3]), y=400,x=400, cena=cena)
    xacria = Elemento(IMGUR.format(ELENCO[4]), y=400,x=600, cena=cena)
    kerexu = Elemento(IMGUR.format(ELENCO[5]), y=400,x=800, cena=cena)
    atores = [ymara, mawapi, wetere, xacria, kerexu]
    nome_ator = zip( atores, nomes)
    ele = [Ator(ato,nom, 100, A.e) for ato, nom in nome_ator]
    nome_ator = zip( atores, nomes, atores[1:]+[None])
    rot = [Fala(ato, nom, prox) for ato, nom, prox in nome_ator]
    roteiro = Roteiro(cena, ele, rot)
