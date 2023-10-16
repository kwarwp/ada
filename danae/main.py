# ada.danae.main.py
""" Aventura Antartica.

Changelog
---------

.. versionadded::    23.10

    |br|   Incluir trash game (16)

.. versionadded::    23.06

    |br| Spike da Antartica (28)

|   **Open Source Notification:** This file is part of open source program **Alite**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from browser import document, alert, html, svg
from _spy.vitollino.main import Cena, STYLE, Elemento, Salao, NADA, Labirinto, NDCT, INVENTARIO as INV
from collections import namedtuple
from random import randint, shuffle, choice
Hero = namedtuple("Hero", "luck pers levl")
STYLE['width'] = 1350
W, H = 1350, 650
# IMGSIZE, IMGHEIGHT = f"{8*W}px", f"{4*H}px"
IMGSIZE, IMGHEIGHT = f"{32*W}px", f"{4*H}px"
ANICONS = "https://i.imgur.com/A2pPOED.png"
SNOWY = "https://i.imgur.com/KxcqKpJ.gif"
SNOW = "https://i.imgur.com/mpOU7Ca.gif"
HSNOW = "https://i.imgur.com/i5dLK8G.gif"
BSNOW = "https://i.imgur.com/4B1xuMw.gif"
SUICONS = "https://i.imgur.com/cM95ybG.jpg"
ANICONS = "https://i.imgur.com/bmUoCIb.png"
SUPPLY = "https://i.imgur.com/zWiteqC.gif"
SUPPLY = "https://i.imgur.com/PWreEK2.gif"
PARADRP = "https://i.imgur.com/ShQMIoU.png"

LIXAO = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/lixocenter.svg"
GATEIRA = "https://i.imgur.com/Ey0W3TR.png"
DESISTO = "https://i.imgur.com/OwMSTHC.png"
RUBISH = "https://i.imgur.com/fCEvaqu.png"
ROFFX, ROFFY, TOFF, SCAL =625, 430, 10, 2.5
#HALO = "https://imgur.com/FiS2X97.gif"
HALO = "https://i.imgur.com/fCEvaqu.png"
lixo = ['mala', 'chaves', 'escova', 'isqueiro', 'suco', 'vinil', 'baralho', 'dez',
        'eifell', 'porquinho', 'bule', 'luva', 'panda', 'cafe', 'guitarra', 'aranha',
        'livro', 'soldado', 'garrafa', 'pizza', 'fone', 'microfone', 'plug', 'visa', 'lata', 'moeda', 'carro', 'sino',
        'presente', 'ipod', 'clarineta', 'cinquenta', 'sujeira', 'blob', 'sujo',
        'facao', 'copinho', 'espremedor', 'pandeiro', 'sacola', 'latao', 'pimenta', 'areia',
        'regar', 'latinha', 'casca', 'hd', 'tenis', 'filme', 'ampulheta', 'pimentao',
        'bumerangue', 'relogio_pulso', 'relogio', 'oculos', 'martelo', 'faca', 'joaninha',
        'radio', 'bussola', 'chapeu', 'alicate', 'trolha', 'tamborim', 'pelucia', 'formiga',
        'jornal', 'chave_fenda', 'vidro', 'cd', 'calculadora', 'lapiseira', 'lampada', 'diploma',
        'lapis', 'tesoura', 'disquete', 'escorpiao', 'bife', 'lagosta', 'pera', 'cubo', 'canivete',
        'pulover', 'banana', 'tampinha', 'cantil', 'rolha', 'fava', 'vaso', 'vinho', 'bola',
        'dalia', 'saco', 'melancia', 'azeitona', 'limao', 'hotdog', 'cachecol', 'papel', 'pote',
        'picareta']


class Thrash:
    def __init__(self):
        self.sujeira =['sujeira', 'blob', 'sujo', 'formiga', 'areia', 'casca', 'joaninha', 'escorpiao', 'aranha', 'latinha']*4
        self.cache = self.create_script_tag(LIXAO)
        self.bonus = 20
        pycard = document["pycard"]
        hidden = Elemento('', style={'position':'absolute', 'top':-2000, 'left':-2000})
        hidden.elt <= self.cache
        pycard <= hidden.elt
        self.comida = ['carpa', 'bacalhau', 'atum', 'robalo', 'dourado']
        self.resposta = self.limpa = lambda *_: None
    def dump(self, cena, sorte=4):
        h =  Hero(1, 2,10) # TheHero()
        self.cena = cena
        self.fundo = Elemento(RUBISH, x=0, y=0, w=1350, h=800, cena=cena)
        self.desiste = Elemento(DESISTO, y=100, cena = cena, vai=self.quit)
        self.remaining_shuffle_count = 20 + 2*h.pers + h.levl//5
        self.rubish = svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
        self.fundo.elt <= self.rubish
        comer = self.comida * (4 + h.levl//2)
        shuffle(comer)
        shuffle(lixo)
        trash = 20 + 2*h.levl
        sujo = 10 + 2*h.levl
        sorte += h.luck + randint(0, h.levl)//3
        pilha = lixo[:trash] + self.sujeira[:sujo] + comer[:sorte] + ['gato']
        shuffle(pilha)
        for indice, label in enumerate(pilha):
            dx, dy = randint(-300,300) , 100  - randint(-100,100)
            dy = (300 - abs(dx))//2
            dx, dy = 200 - dx , 100  - randint(-dy, dy)
            obj = svg.use(id=f"#{indice:03d}{label}", href=f"#{label}", x=200, y=100 , width=250, height=250,
            transform=f"translate({dx} {dy})  rotate({7*indice} {ROFFX} {ROFFY}) scale(2.5)")
            self.rubish <= obj
            obj.bind('click', self._vai)
            obj.setAttribute("data-didit", "_no_")
            
    def _vai_(self, ev):
        self.__vai(ev)
    def quit(self, *_):
        self.remaining_shuffle_count = 0
        if not self.remaining_shuffle_count:
            self.fundo.elt.remove()
            self.desiste.elt.remove()
            TheHero().learn(self.bonus)
            return
    def _vai(self, ev):
        self.remaining_shuffle_count -= 1
        if not self.remaining_shuffle_count:
            self.quit()
            return
            
        from browser import document, alert, svg
        dx, dy = randint(-300,300) , 100  - randint(-100,100)
        dy = abs(300 -dx)//3
        dx, dy = 200 - dx , 100  - randint(-dy,dy)
        obj = document[ev.target.id]
        obj_name = ev.target.id[4:]
        if obj.getAttribute("data-didit") == "_did_":
            return
        if obj_name in self.comida+["gato"]:
            food = Elemento('', x=0, y=50, w=200, h=200, tit=f"{ev.target.id}_", cena=self.cena)
            stag = svg.svg(version="1.1", width="200", height="200")
            food.elt <= stag
            stag <= obj
            obj.setAttribute('transform',f"translate(-{ROFFX-485} -{ROFFY-220}) scale(0.60 1.35)")
            obj.setAttribute('transform',f"translate(-{ROFFX-485} -{ROFFY-220}) scale(0.60 1.35)")
            INV.bota(food)
            obj.setAttribute("data-didit", "_did_")
            if obj_name == "gato":
                obj.setAttribute('transform',f"translate(-{ROFFX-485} -{ROFFY-345}) scale(0.60 0.6)")
                #food.vai = TheHero().calma
                #TheHero().blacking(food.tit)
                return
            #TheHero().fishing(food.tit)
        else:
            obj.setAttribute('transform',f"translate({dx} {dy})  rotate({7*randint(0,70)} {ROFFX} {ROFFY}) scale(2.5)")


    def create_script_tag(self, src):
        import urllib.request
        from browser import document
        _fp = urllib.request.urlopen(src)
        _data = _fp.read()

        _tag = document.createElement('div')
        _tag.html = _data
        return _tag

class Sprite(Elemento):
    def __init__(self, img="", vai=None, style=NDCT, tit="", alt="",
                 x=0, y=0, w=100, h=100, o=1, texto='', foi=None, index=0, sw=100, sh=100, cx=1, b=0, s=1,
                 cena="", score=NDCT, drag=False, drop={}, tipo="100% 100%", **kwargs):
        #style=dict(left=x, top=x, width=f"{w}px", height=f"{h}px", overflow="hidden", filter= f"blur({b}px)", scale=s)
        style=dict(width=f"{w}px", height=f"{h}px", overflow="hidden", filter= f"blur({b}px)", scale=s)
        position = f"-{index % cx * w}px -{index // cx * w}px"
        style.update({"max-width": f"{sw}px", "max-height": f"{sh}px", "background-position": position})

        super().__init__(img=img, vai=vai, tit=tit, alt=alt,
                 x=x, y=y, w=w, h=h, o=o, texto=texto, foi=foi,
                 cena=cena, score=NDCT, drag=drag, drop=drop, tipo=f"{sw}px {sh}px", 
                 style=style,
                 **kwargs)

class CenaSprite(Cena):
    def __init__(self,image, index, **kwargs):
        super().__init__(image,  **kwargs)
        # style=dict(left=x, top=x, width="80px", height="80px", overflow="hidden")
        style = dict(position="relative", left=f"-{index % 8 * W}px", top=f"-{(index%16) // 4 * H}px", width=f"{W}px",
                     height=f"{H}px", overflow="hidden", minWidth=IMGSIZE, minHeight=IMGHEIGHT)
        divsty = dict(STYLE)
        divsty.update({"max-width": f"{W}px", "max-height": f"{H}px", "overflow": "hidden"})
        self.elt = html.DIV(style=divsty)
        self.img = html.IMG(src=image, width=W, height=H, style=style)
        self.elt <= self.img
        self._cria_divs(W)
        
class SpriteSala(Salao):
    def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
        self.cenas = [n, l, s, o]
        self.nome = nome
        # Sala.c(**kwargs)
        self.p()
def is7(j):
    if j//8:
        j+7
LAND = "https://i.imgur.com/Cmyq9vd.jpg"
MAPA = [{k:CenaSprite(LAND, index=v) for k, v in zip("nlso", range(l,l+4))} for l in range(0,64*7,7)]
#MAPA = [{k:v for k, v in zip("nlso", range(l,l+4))} for l in range(0,16,4)]
# print(MAPA)
sl = [SpriteSala(**sl) for sl in MAPA]
# LA = [(j, (j-1)%(((j)//8+1)*8), (j+64+8)%64, (j+1)%(((j)//8+1)*8),  (j+56)%64) for  j in range(0,64)]
LA = [(j, (j -1) if (j%8) else (j+7), (j+64+8)%64, (j+1)%(((j)//8+1)*8),  (j+56)%64) for  j in range(0,64)]
# LABS = [{k: v for k, v in zip("cnlso", [sl[int(s)] for s in cruz])} for cruz in "03131 12020 21313 30202".split()]
LABS = [{k: v for k, v in zip("cnlso", [sl[int(s)] for s in cruz])} for cruz in LA]
lb = [Labirinto(**salas) for salas in LABS]
#c=CenaSprite(LAND, index=6)
#c.vai()
Elemento(BSNOW, w=W, h=H, o=0.8, cena=sl[0].norte, style={'pointer-events': 'none'})
s = 64
i = sl[0].norte
j = sl[0].leste
a = Sprite(ANICONS, x=700, y=300, w=s, h=s, o=0.4, index=0, sw=320, sh=256, cx=5, cena=i, b=4, s=1)  #, tipo="320px 256px")
s = Elemento(SUPPLY, w=200, cena=i)
p = Elemento(PARADRP, x=888, w=100, h=50, y=500, cena=i)
t = Thrash().dump(j)
i.vai()
# i.elt.text=LABS
#print(a.style)
