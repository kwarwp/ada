# ada.gatil.main.py
from _spy.vitollino.main import Cena, STYLE, Elemento, Sala as SalaVit, Labirinto, NADA, INVENTARIO as INV
from _spy.vitollino.main import Jogo as J
from browser import html, alert
from collections import namedtuple
from random import randint, shuffle, choice
CATPUZ = "lVlPvCB zVp6z".split()
GITRAW = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Anonymous_Eiffel_tower.svg"
TORRE = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Anonymous_Eiffel_tower.svg"
LIGHT = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/brunurb_yellowlighter_1.svg"
CANDY = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Chrisdesign_candystick.svg"
LIXAO = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/lixocenter.svg"
#RUBISH = "https://i.imgur.com/4cZQRvF.png"
RUBISH = "https://i.imgur.com/MSJw5kB.png"
#ROFFX, ROFFY, TOFF, SCAL =720, 330, 150, 2.5
ROFFX, ROFFY, TOFF, SCAL =625, 430, 10, 2.5
P = namedtuple('Properties',"H T S G")(0, 1, 2, 3)
STYLE.update(width=1350, height="800px")
GATIL_MOS = "https://i.imgur.com/5ZISX93.jpg"
GATIL_POR = "https://i.imgur.com/Ockz2ae.png"
PETUNIO = "https://i.imgur.com/2KeouVt.png"
IM = "https://i.imgur.com/{}.jpg"
IMP = "https://i.imgur.com/{}.png"
SA = "VV1xbBG SEblwJG JVXK8gA nyly8wp".split()
SB = "NqNXbr4 2QdVrAj jvM9BQC 2KZpwVf".split()
WIND = "https://imgur.com/3LJN7lT.gif"
GATAR = "https://imgur.com/WcrEeLj.png"
STRAY = "qooCvWD SfGf1gv hlA5iCO RWc9j9Q FPWh9Nt".split()
STRAYS = "pMEwzkz llqWlNC LAUEEAj KA7r39r 8nBLnkF".split()
PIX = "https://imgur.com/0OoP7wt.jpg"
RAIN = "https://cdn.wallpapersafari.com/44/7/bvCdLK.gif"
STORM = "https://media.giphy.com/media/xT9GEDhzERbjDD15O8/giphy.gif"
FLOOD = "https://media.giphy.com/media/3HoB7BmMnKMdq/giphy.gif"
HAIL = "https://i.imgur.com/ZZ8nEkV.gif"
HALO = "https://i.imgur.com/XDuFNZw.png"
HERO = Elemento(PETUNIO, x=200, y=550, w=130, h=100)
NO = []
lixo = ['mala', 'chaves', 'escova', 'isqueiro', 'suco', 'vinil', 'baralho', 'dez',
        'eifell', 'porquinho', 'bule', 'luva', 'panda', 'cafe', 'guitarra', 'aranha',
        'livro', 'soldado', 'garrafa', 'pizza', 'fone', 'microfone', 'plug', 'visa', 'lata', 'moeda', 'carro', 'sino',
        'presente', 'gato', 'ipod', 'clarineta', 'cinquenta', 'sujeira', 'blob', 'sujo',
        'facao', 'copinho', 'espremedor', 'pandeiro', 'sacola', 'latao', 'pimenta', 'areia',
        'regar', 'latinha', 'casca', 'hd', 'tenis', 'filme', 'ampulheta', 'pimentao',
        'bumerangue', 'relogio_pulso', 'relogio', 'oculos', 'martelo', 'faca', 'joaninha',
        'radio', 'bussola', 'chapeu', 'alicate', 'trolha', 'tamborim', 'pelucia', 'formiga',
        'jornal', 'chave_fenda', 'vidro', 'cd', 'calculadora', 'lapiseira', 'lampada', 'diploma',
        'lapis', 'tesoura', 'disquete', 'escorpiao', 'bife', 'lagosta', 'pera', 'cubo', 'canivete',
        'pulover', 'banana', 'tampinha', 'cantil', 'rolha', 'fava', 'vaso', 'vinho', 'bola',
        'dalia', 'saco', 'melancia', 'azeitona', 'limao', 'hotdog', 'cachecol', 'papel', 'pote',
        'picareta']


class Swap:
    """ Jogo que embaralha as partes de um desenho e usa drag and drop para rearrumar.
        
        As peças aparecem inicialmente embaralhadas e devem ser arrastadas para o local onde deveriam estar
        
        :param    j: referência ao Jogo do Vitollino.
        :param  img: a imagem que deve ser embaralhada
        :param cena: a cena onde o jogo aparece
        :param    x: a posição horizontal da imagem
        :param    y: a posição vertical da imagem
        :param    w: a largura da imagem
        :param    h: a altura da imagem
        :param   dw: quantidade de colunas que recortam a imagem
        :param   dh: quantidade de linhas que recortam a imagem
    """
    def __init__(self, j, img, cena, w=900,h=400,x=100,y=50,dw=3,dh=3, venceu=None):
        swap = self
        class Peca(j.a):
            """ A Peça representa um recorte da imagem que vai ser embaralhada.
            """
            def __init__(self, local, indice):
                self.local, self.indice = local, indice
                """ local em que a peça foi colocada; local onde a peça deveria estar"""
                pw, ph = w//dw, h//dh
                """largura e altura da peça"""
                lx, ly = x+local%dw*pw, y+local//dw*ph
                """posição horizontal e vertical em pixels onde a peça será desenhada"""
                px, py = indice%dw*pw, indice//dw*ph
                """posição horizontal e vertical em pixels onde o desenho da peça está na imagem"""
                super().__init__(img, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena)
                """chama o construtor do Elemento Vitollino passandoa as informações necessárias"""
                self.siz = (w, h)
                """redimensiona a figura da imagem para o tamanho fornecido"""
                self.elt.Id = f"_swap_{local}"
                """rotula o elemento da peça com a posição onde foi alocada"""
                self.pos = (-px, -py)
                """reposiciona a figura da imagem para o pedaço que vai aparecer na peça"""
                self.elt.ondrop = lambda ev: self.drop(ev)
                """captura o evento drop da peça para ser tratado pelo método self.drop"""
            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                local = int(src_id.split('_')[-1])
                print(f"local -> {local} | indice -> {self.indice}")
                self.dropped(ev, local)
                
            def dropped(self, ev, local):
                o_outro = swap.pecas[local].pra_la(self, self.x, self.y, local)
                o_local = swap.pecas[local].local
                print(f"indice, o outro -> {self.indice} @ {self.local} <-> {o_outro} @ {o_local}")
                swap.montou()
            def pra_la(self, peca, x, y, local):
                self.local = peca.pra_ca(self.x, self.y, self.local)
                self.x, self.y = x, y
                return self.indice
            def pra_ca(self, x, y, local):
                self.local, local = local, self.local
                self.x, self.y = x, y
                return local
            def certo(self):
                return self.indice == self.local
            def __repr__(self):
                return str(self.indice)

        from random import shuffle
        pecas = list(range(dw*dh))
        shuffle(pecas)
        self.pecas = [Peca(local, indice) for local, indice in enumerate(pecas)]
        self.venceu = venceu or J.n(cena, "Voce venceu!")
    def montou(self):
        resultado = [peca.certo() for peca in self.pecas]
        print(resultado)
        self.venceu.vai() if all(resultado) else None 
        return all(resultado)


class Abrigo:
    GW = 1350
    GH = 800
    IW = 4000
    IH = 1000
    DW = (IW-GW)//6
    def __init__(self):
        super().__init__(img)

class Rua(Cena):
    def __init__(self, img, trash=None, props=NO):
        cena = self
        class Hero(Elemento):
            def __init__(self, x=0, y=0, w=130, h=100):
                super().__init__(PETUNIO, x=x, y=y, w=w, h=h, cena=cena)
        class Trash(Elemento):
            def __init__(self, x=0, y=0, w=40, h=40):
                super().__init__(HALO, x=x, y=y, w=w, h=h, o=0.2, vai=self.dump, cena=cena)
            def dump(self, *_):
                trash.dump(cena)
        class Stray(Elemento):
            def __init__(self, x=0, y=0, w=60, h=60):
                #super().__init__(STRAY[randint(0,4)], x=x, y=y, w=w, h=h, cena=cena)
                super().__init__(IMP.format(STRAY[0]), x=x, y=y, w=w, h=h, vai=self.dump, cena=cena)
            def dump(self, *_):
                Swap(J(), IM.format(choice(CATPUZ)),cena, venceu=self)
            def vai(self, *_):
                INV.bota(self)
        class Gui(Elemento):
            def __init__(self, x=0, y=0, w=40, h=100):
                super().__init__(HALO, x=x, y=y, w=w, h=h, o=0.4, cena=cena)
        super().__init__(img)
        self.props = p ={P.H: Hero, P.T: Trash, P.S: Stray, P.G: Gui}
        [p[proname](*proargs) for proname, proargs  in props]
        self.img = img
    def vai_(self):
        super().vai()
        c0 = Elemento(self.img, x=140, y=340, w=200, h=200, cena=self)
        p0 = Elemento(GATIL_POR, x=100, y=300, w=300, h=300, cena=self)
    def vai(self, *_):
        super().vai()
        #HERO.entra(self)
class Thrash:
    def __init__(self):
        self.sujeira =['sujeira', 'blob', 'sujo', 'formiga', 'areia', 'casca', 'joaninha', 'escorpiao', 'aranha', 'latinha']*4
        self.cache = self.create_script_tag(LIXAO)
        #cena.elt <= cache
        self.comida = ['carpa', 'bacalhau', 'atum', 'robalo', 'dourado']
    def dump(self, cena, sorte=4):
        from browser import svg
        cena.elt <= self.cache
        self.cena = cena
        self.fundo = Elemento(RUBISH, x=0, y=0, w=1350, h=800, cena=cena)
        self.remaining_shuffle_count = 20
        self.rubish = svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
        self.fundo.elt <= self.rubish
        comer = self.comida * 4
        shuffle(comer)
        shuffle(lixo)
        pilha = lixo[:60] + self.sujeira + comer[:sorte]
        shuffle(pilha)
        for indice, label in enumerate(pilha):
            dx, dy = randint(-300,300) , 100  - randint(-100,100)
            dy = abs(300 -dx)//3
            dx, dy = 200 - dx , 100  - randint(-dy, dy)
            obj = svg.use(id=f"#{indice:02d}{label}", href=f"#{label}", x=200, y=100 , width=250, height=250,
            transform=f"translate({dx} {dy})  rotate({7*indice} {ROFFX} {ROFFY}) scale(2.5)")
            self.rubish <= obj
            obj.bind('click', self.vai)
            
    def vai(self, ev):
        self.remaining_shuffle_count -= 1
        if not self.remaining_shuffle_count:
            self.fundo.elt.remove()
            return
            
        from browser import document, alert, svg
        dx, dy = randint(-300,300) , 100  - randint(-100,100)
        dy = abs(300 -dx)//3
        dx, dy = 200 - dx , 100  - randint(-dy,dy)
        #alert (ev.target.id)
        obj = document[ev.target.id]
        if ev.target.id[3:] in self.comida:
            food = Elemento('', x=0, y=50, w=200, h=200, cena=self.cena)
            stag = svg.svg(version="1.1", width="200", height="200")
            food.elt <= stag
            stag <= obj
            obj.setAttribute('transform',f"translate(-{ROFFX-485} -{ROFFY-220}) scale(0.60 1.35)")
            INV.bota(food)
        else:
            obj.setAttribute('transform',f"translate({dx} {dy})  rotate({7*randint(0,70)} {ROFFX} {ROFFY}) scale(2.5)")

        # obj.transform = f"translate({dx} {dy})  rotate({7*randint(0,70)} {ROFFX} {ROFFY}) scale(2.5)")
        #obj.setTranslate(dx, dy)
        #obj.setRotate(7*randint(0,70), ROFFX, ROFFY)
        # self.c.cx =100

    def create_script_tag(self, src):
        import urllib.request
        from browser import document
        _fp = urllib.request.urlopen(src)
        _data = _fp.read()

        _tag = document.createElement('div')
        #_tag.type = "image/svg+xml"
        _tag.html = _data
        return _tag
        

class Sala(SalaVit):
    def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
        self.cenas = [Rua(img) if isinstance(img, str) else img for img in [n, l, s, o]]
        self.nome = nome
        Sala.c(**kwargs)
        self.p()

class Gatil(Cena):
    def __init__(self, img, x=0, y=0):
        super().__init__(img)
        self.img = img
        self.trash = Thrash()
        #self.elt = html.DIV(style=STYLE, )
        self.dx, self.dy = x*Abrigo.DW, y*200, 
        self.cena = c = Elemento(img, x=0, y=0, w=1350, h=800, cena=self)
        self.hero = h = Elemento(PETUNIO, x=400, y=350, w=250, h=200, cena=self)
        # self.elt.style.width = w
        c.siz = (Abrigo.IW, Abrigo.IH)
        c.pos = (-self.dx, -self.dy)
    def vai_(self):
        super().vai()
        c0 = Elemento(self.img, x=140, y=340, w=200, h=200, cena=self)
        p0 = Elemento(GATIL_POR, x=100, y=300, w=300, h=300, cena=self)
    def et_vai(self, *_):
        self.et.x = 100
    def vai(self):
        sala_a = Sala(*[IM.format(lnk) for lnk in SA])
        sala_a.norte.vai()
        sala_b_args = [IM.format(lnk) for lnk in SB]
        sala_b_args[0] = Rua(sala_b_args[0], self.trash, [
        (P.H, [200, 550]), (P.T, [540, 440]), (P.T, [840, 470]), (P.S, [1050, 550]), (P.G, [480, 400])])
        sala_b_args[1] = Rua(sala_b_args[1], self.trash, [
        (P.H, [310, 490]), (P.T, [540, 490]), (P.T, [780, 430, 150]), (P.G, [60, 510, 100]), (P.S, [980, 500])])
        sala_b_args[2] = Rua(sala_b_args[2], self.trash, [
        (P.H, [100, 500]), (P.T, [780, 590, 60, 50]), (P.T, [840, 670]), (P.S, [850, 550]), (P.G, [390, 510, 80, 140])])
        sala_b_args[3] = Rua(sala_b_args[3], self.trash, [
        (P.H, [300, 600]), (P.T, [650, 440, 60, 50]), (P.T, [910, 470, 220, 120]), (P.T, [1140, 610, 90]), (P.S, [850, 550])])
        sala_b = Sala(*sala_b_args)
        lab0 = Labirinto(sala_a, sala_b, sala_b, sala_b, sala_b)
        lab1 = Labirinto(sala_b, sala_a, sala_a, sala_a, sala_a)
        # self.cena = c = Elemento(WIND, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        # self.rain = r = Elemento(HAIL, x=0, y=0, w=1350, h=800, o=0.4, cena=sala_b.norte)
        # self.hero = h = Elemento(PETUNIO, x=200, y=550, w=130, h=100, cena=sala_b.norte)
        # self.stray = s = Elemento(IMP.format(STRAY[0]), x=600, y=550, w=130, h=100, cena=sala_b.norte)
        # self.strays = z = Elemento(IMP.format(STRAYS[0]), x=300, y=50, w=650, h=650, cena=sala_b.norte)
        self.gatar = g = Elemento(GATAR, x=200, y=550, w=100, h=100)
        self.pix = p = Elemento(PIX, x=200, y=550, w=100, h=100)
        self.et = Elemento(GITRAW, x=500, y=200, w=100, h=100, cena=sala_b.norte)
        #x = Elemento('', x=0, y=0, w=1000, h=800, cena=sala_b.norte)#, vai=self.et_vai)
        INV.inicia()
        INV.bota(g)
        INV.bota(p)
        sala_b.norte.vai()
        #self.trash.dump(sala_b.norte)
        #go = Cena(vai=
        Swap(J(), IM.format(CATPUZ),sala_b.norte,)
    
Gatil(GATIL_MOS).vai()