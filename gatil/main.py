# ada.gatil.main.py
from _spy.vitollino.main import Cena, STYLE, Elemento, Sala as SalaVit, Labirinto, NADA, INVENTARIO as INV
from browser import html
from collections import namedtuple
from random import randint, shuffle
GITRAW = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Anonymous_Eiffel_tower.svg"
TORRE = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Anonymous_Eiffel_tower.svg"
LIGHT = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/brunurb_yellowlighter_1.svg"
CANDY = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/Chrisdesign_candystick.svg"
LIXAO = "https://raw.githubusercontent.com/kwarwp/ada/master/gatil/trink/lixocenter.svg"
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
        'livro', 'soldado', 'garrafa', 'pizza', 'carpa', 'bacalhau', 'atum', 'robalo',
        'dourado', 'fone', 'microfone', 'plug', 'visa', 'lata', 'moeda', 'carro', 'sino',
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
class Abrigo:
    GW = 1350
    GH = 800
    IW = 4000
    IH = 1000
    DW = (IW-GW)//6
    def __init__(self):
        super().__init__(img)

class Rua(Cena):
    def __init__(self, img, props=NO):
        cena = self
        class Hero(Elemento):
            def __init__(self, x=0, y=0, w=130, h=100):
                super().__init__(PETUNIO, x=x, y=y, w=w, h=h, cena=cena)
        class Trash(Elemento):
            def __init__(self, x=0, y=0, w=40, h=40):
                super().__init__(HALO, x=x, y=y, w=w, h=h, o=0.2, cena=cena)
        class Stray(Elemento):
            def __init__(self, x=0, y=0, w=60, h=60):
                #super().__init__(STRAY[randint(0,4)], x=x, y=y, w=w, h=h, cena=cena)
                super().__init__(IMP.format(STRAY[0]), x=x, y=y, w=w, h=h, cena=cena)
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
    def __init__(self, elt, cena):
        from browser import svg
        self.cena = cena
        cache = self.create_script_tag(LIXAO)
        cena <= cache
        #s = svg.svg(version="1.1", viewBox="0 0 400 600", width="1300", height="800")
        s = svg.svg(version="1.1", viewBox="400 200 1500 1000", width="1600", height="800")
        '''
        self.c = circle = svg.circle(id="svcirc", cx=170, cy=220, r=100,
                    stroke="black",stroke_width="2",fill="red")
        circle.bind('click', self.vai)
        #u = svg.use("#g1111", x=0, y=0, width=90, height=90)
        cc = svg.use(href="#svcirc", x=100, y=0, width=90, height=90)
        '''
        u = svg.use(href="#mala", x=50, y=50, width=50, height=50,
        transform="rotate(-10) scale(2.5 2.5)")
        #transform="rotate(-10 50 100) translate(-36 45.5) scale(2.5 2.5)")
        u.bind('click', self.vai)
        cs = svg.use(href="#guitarra", x=70, y=50, width=50, height=50,
        transform="rotate(-20) scale(2.5 2.5)")
        cs.bind('click', self.vai)

        #s = svg.Svg()
        elt <= s
        shuffle(lixo)
        for indice, label in enumerate(lixo[:70]):
            dx, dy = randint(-300,300) , 100  - randint(-100,100)
            dy = abs(300 -dx)//3
            dx, dy = 200 - dx , 100  - randint(-dy,dy)
            #obj = svg.use(href=f"#{label}", x= 6100 -600*dx, y=3500 - 350*dy, width=100, height=100,
            #obj = svg.use(href=f"#{label}", x=1000 - 100*dx, y=500 -50*dy, width=50, height=50,
            #obj = svg.use(href=f"#{label}", x=200 - randint(-100,100), y=100 -randint(0,1), width=50, height=50,
            obj = svg.use(id=f"#0{label}", href=f"#{label}", x=200, y=100 , width=250, height=250,
            transform=f"translate({dx} {dy})  rotate({7*indice} {ROFFX} {ROFFY}) scale(2.5)")
            #transform=f"rotate({-10*indice} 50 100) translate(-36 45.5) scale(2.5 2.5)")
            s <= obj
            obj.bind('click', self.vai)
            
            '''
            [s <= svg.use(href=f"#{label}", x=300, y=100, width=50, height=50,
            transform=f"translate({dx} {TOFF}) rotate({indice} {ROFFX} {ROFFY}) scale({SCAL})") for indice in range(0, 360, 15)]
        '''        
        #s <= circle
        #s <= u
        #s <= cs
    def vai(self, ev):
        come = ['pizza', 'carpa', 'bacalhau', 'atum', 'robalo', 'dourado']
        from browser import document, alert
        dx, dy = randint(-300,300) , 100  - randint(-100,100)
        dy = abs(300 -dx)//3
        dx, dy = 200 - dx , 100  - randint(-dy,dy)
        #alert (ev.target.id)
        obj = document[ev.target.id]
        if ev.target.id[1:] in come:
            food = Elemento('', x=0, y=0, cena=self.cena)
            stag = svg.svg(version="1.1", width="200", height="200")
            food.elt <= stag
            stag <= obj
            obj.setAttribute('transform',f"translate(0, 0) scale(0.5)")
            #INV.bota(food)
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
        sala_b_args[0] = Rua(sala_b_args[0],[
        (P.H, [200, 550]), (P.T, [540, 440]), (P.T, [840, 470]), (P.S, [1050, 550]), (P.G, [480, 400])])
        sala_b_args[1] = Rua(sala_b_args[1],[
        (P.H, [310, 490]), (P.T, [540, 490]), (P.T, [780, 430, 150]), (P.G, [60, 510, 100]), (P.S, [980, 500])])
        sala_b_args[2] = Rua(sala_b_args[2],[
        (P.H, [100, 500]), (P.T, [780, 590, 60, 50]), (P.T, [840, 670]), (P.S, [850, 550]), (P.G, [390, 510, 80, 140])])
        sala_b_args[3] = Rua(sala_b_args[3],[
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
        x = Elemento('', x=0, y=0, w=1000, h=800, cena=sala_b.norte)#, vai=self.et_vai)
        INV.inicia()
        INV.bota(g)
        INV.bota(p)
        sala_b.norte.vai()
        Thrash(x.elt, sala_b.norte.elt)
    
Gatil(GATIL_MOS).vai()