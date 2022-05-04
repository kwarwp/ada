# ada.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from collections import namedtuple
STYLE.update(width=600, height="80px")
Ator = namedtuple('Elenco','ator nome mini alinha')
Fala = namedtuple('Fala','ator fala age prox')  # , defaults=(None,)*4)
A = namedtuple('Ali','e m d')(-1, 0, 1)
IMGUR = "https://i.imgur.com/{}.png"
ELENCO = "z7zIJHV iJqmT9V ehoPNb1 WJ1QdZ9 yqrocJa NShlUFP".split()
SMILE = "https://purepng.com/public/uploads/large/purepng.com-mouth-smilemouth-smilefacial-expressionduchenne-smile-1421526971643lbaoz.png"
yma, maw, wet, xac, ker = "Ymara Guajajara|Maria Wapichana|Weteré ParkatêJê|Celia Xacriabá|Kerexu Yxapyry".split("|")
NOMES = [yma, maw, wet, xac, ker]
class Fala_:
    def __init__(self, ator, fala, age=None, prox=None):
        self.ator, self.fala, self.age, self.prox = ator, fala, age, prox

class Roteiro:
    def __init__(self, cena, roteiro, elenco=[], foi=None):
        prox = zip(roteiro, roteiro[1:]+[None])
        self.foi = foi if foi else lambda *_: None
        roteiro = [Fala(a, f, g, p.ator if p else None) for [a, f, g,_], p in prox]
        self.elenco, self.roteiro = elenco, roteiro
        self._foi = lambda *_: None
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
                self._foi = self.nada
                self.mini = Elemento(ator.img, cena=cena, w=80, h=80, style=dict(top="4%",margin="60px"))
                super().__init__(cena,fala, **kwarg)
            def esconde(self, *_):
                self.mini.elt.remove()
                self.ator.elt.style.filter = "brightness(30%)"
                script.testa(self.prox)
                #script.segue()
                #super().esconde()
                self._foi()
            def vai(self, *_):
                super().vai()
                self.ator.elt.style.filter = "brightness(5%)"
                self.ator.vai = self.nada

            @property  
            def foi(self):
                return self._foi

            @foi.setter  
            def foi(self, value):
                self._foi = value

            def nada(self, *_):
                pass
        self._fala = Falar
        
    def nada(self, *_):
        pass
        
    def segue(self, *_):
        ator, fala, action, prox = self.scripter()
        #ator.elt.style.filter = "brightness(30%)"
        '''if action:
            action.vai = self.segue
            action.elt.style.filter = "brightness(100%)"'''

        fala = self._fala(ator, fala, prox) #.vai()
        if prox:
            prox.vai = self.segue
            fala.vai()
        else:
            self._foi = self.foi_
            fala.foi = self.foi_
            fala.vai()
            # prox.elt.style.filter = "brightness(100%)"
        
    def gone(self, *_):
        self._foi
        
    def foi_(self, *_):
            #else:
            for ato in []: # self.atores:
                ato.elt.style.filter = "brightness(100%)"
            self.foi()
        
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
            sm1 = Elemento(SMILE, x=50, y=60, w=40, h=30, cena=cena)
            sm2 = Elemento(SMILE, x=463, y=92, w=25, h=18, cena=cena, style={'transform': 'rotate(-15deg)'})
            nome_ator = zip( atores, nomes)
            ele = [Ator(ato,nom, 100, A.e) for ato, nom in nome_ator]
            nome_ator = zip( atores, nomes, atores[1:]+[None])
            rot = [Fala(ato, nom, prox, None) for ato, nom, prox in nome_ator]
            roteiro = Roteiro(cena, rot, ele)
    class Sorrisos:
        def __init__(self,nomes=NOMES, yy=40, xx=20, dx=100):
            self.cena = cena = Cena(IMGUR.format(ELENCO[0])).vai()
            self.elenco = [Elemento(IMGUR.format(ELENCO[conta+1]), y=yy, x=xx+dx*conta, cena=cena) for conta in [0, 4]]
            ymara, kerexu = atores = self.elenco
            nome_ator = zip( atores, [nomes[0],nomes[4]])
            ele = [Ator(ato,nom, 100, A.e) for ato, nom in nome_ator]
            nome_ator = zip( atores, nomes, atores[1:]+[None])
            #rot = [Fala(ato, nom, prox, None) for ato, nom, prox in nome_ator]
            rot = [
            Fala(ymara, "Eu e a Kerexu gostamos de caçar. Muitas vezes nos divertimos muito!", kerexu, None),
            Fala(kerexu, "Mas as vezes caçar é um assunto sério. Se nós duas estamos sérias, estamos preparadas para caçar", ymara, None),
            Fala(ymara, "Mas também se nós duas estamos sorrindo é que vamos caçar", kerexu, None),
            Fala(kerexu, "As meninas_guerreiras retornam verdadeio (True) se nós vamos caçar", ymara, None),
            ]
            roteiro = Roteiro(cena, rot, ele, self.foi)
        def foi(self, *_):
            sm1 = Elemento(SMILE, x=50, y=60, w=40, h=30, cena=self.cena)
            sm2 = Elemento(SMILE, x=463, y=92, w=25, h=18, cena=self.cena, style={'transform': 'rotate(-15deg)'})
        
    Sorrisos()
