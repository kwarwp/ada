# ada.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from collections import namedtuple
STYLE.update(width=600, height="80px")
Ator = namedtuple('Elenco','ator nome mini alinha')
Fala = namedtuple('Fala','ator fala age prox')  # , defaults=(None,)*4)
A = namedtuple('Ali','e m d')(-1, 0, 1)
IMGUR = "https://i.imgur.com/{}.png"
ELENCO = "z7zIJHV iJqmT9V ehoPNb1 WJ1QdZ9 yqrocJa NShlUFP".split()
yma, maw, wet, xac, ker = "Ymara Guajajara|Maria Wapichana|Weteré ParkatêJê|Celia Xacriabá|Kerexu Yxapyry".split("|")
NOMES = [yma, maw, wet, xac, ker]


class Roteiro:
    def __init__(self,cena, roteiro, elenco=[]):
        prox = zip(roteiro, roteiro[1:]+[None])
        roteiro = [Fala(a, f, g, p.ator if p else None) for [a, f, g,_], p in prox]
        self.elenco, self.roteiro = elenco, roteiro
        script = self
        for ator in elenco:
            ator.ator.vai = self.nada
            ator.ator.tit = ator.nome
            ator.ator.elt.style.filter = "brightness(30%)"
        protagonista = elenco[0].ator if elenco else roteiro[0].ator
        self.atores = [ator.ator for ator in elenco] if elenco else [ator.ator for ator in roteiro]
        protagonista.vai = self.segue
        protagonista.elt.style.filter = "brightness(100%)"
        class Falar(Texto):
            def __init__(self, ator, fala, prox, **kwarg):
                self.ator, self.fala, self.prox = ator, fala, prox
                self.mini = Elemento(ator.img, cena=cena, w=80, h=80, style=dict(top="4%",margin="60px"))
                super().__init__(cena,fala, **kwarg)
            def esconde(self, *_):
                super().esconde()
                self.mini.elt.remove()
                self.ator.elt.style.filter = "brightness(30%)"
                script.testa(self.prox)
                #script.segue()
            def vai(self, *_):
                super().vai()
                self.ator.elt.style.filter = "brightness(5%)"
        self._fala = Falar
        
    def nada(self, *_):
        pass
        
    def segue(self, *_):
        ator, fala, action, prox = self.scripter()
        #ator.elt.style.filter = "brightness(30%)"

        self._fala(ator, fala, prox).vai()
        '''if action:
            action.vai = self.segue
            action.elt.style.filter = "brightness(100%)"'''
        if prox:
            prox.vai = self.segue
            # prox.elt.style.filter = "brightness(100%)"
        else:
            for ato in []: # self.atores:
                ato.elt.style.filter = "brightness(100%)"
        
    def testa(self, prox, *_):
        if self.roteiro:
            prox.elt.style.filter = "brightness(100%)"
        else:
            for ato in self.atores:
                ato.elt.style.filter = "brightness(100%)"
        
    def scripter(self, *_):
        return self.roteiro.pop(0)


if __name__ == "__main__":
    class Guerreiras:
        def __init__(self,nomes=NOMES, yy=40, xx=20, dx=100):
            cena = Cena(IMGUR.format(ELENCO[0])).vai()
            self.elenco = [Elemento(IMGUR.format(ELENCO[conta+1]), y=yy, x=xx+dx*conta, cena=cena) for conta in range(5)]
            '''
            ymara = Elemento(IMGUR.format(ELENCO[1]), y=yy, x=xx+dx*0, cena=cena)
            mawapi = Elemento(IMGUR.format(ELENCO[2]), y=yy, x=xx+dx*1, cena=cena)
            wetere = Elemento(IMGUR.format(ELENCO[3]), y=yy, x=xx+dx*2, cena=cena)
            xacria = Elemento(IMGUR.format(ELENCO[4]), y=yy, x=xx+dx*3, cena=cena)
            kerexu = Elemento(IMGUR.format(ELENCO[5]), y=yy, x=xx+dx*4, cena=cena)
            atores = [ymara, mawapi, wetere, xacria, kerexu]'''
            atores = self.elenco
            nome_ator = zip( atores, nomes)
            ele = [Ator(ato,nom, 100, A.e) for ato, nom in nome_ator]
            nome_ator = zip( atores, nomes, atores[1:]+[None])
            rot = [Fala(ato, nom, prox, None) for ato, nom, prox in nome_ator]
            roteiro = Roteiro(cena, rot, ele)
    Guerreiras()
