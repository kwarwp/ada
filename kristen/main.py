from _spy.vitollino.main import Cena,  Texto, STYLE, PSTYLE,LSTYLE, EIMGSTY, NOSC, NoEv
from _spy.vitollino.main import INVENTARIO
from browser import html, doc


STYLE["width"] = 800
STYLE["height"] = "600px"

NDCT = {}
FIX_COUNT = {}        

class Elemento():

    NDCT = {}
    FIX_COUNT = {}

    """
        Um objeto de interação que é representado por uma imagem em uma cena.

                papel = Elemento(
                 img="papel.png", tit="caderno de notas",
                 vai=pega_papel, style=dict(left=350, top=550, width=60))


        :param img: URL de uma imagem
        :param vai: função executada quando se clica no objeto
        :param style: dicionário com dimensões do objeto {"left": ..., "top": ..., width: ..., height: ...}
        :param tit: Texto que aparece quando se passa o mouse sobre o objeto
        :param alt: Texto para leitores de tela
        :param cena: cena alternativa onde o objeto vai ser colocado; sendo o inventário presente em todas as cenas
        :param score: determina o score para este elemento
        :param drag: atributo do objeto arrastável {True , False}
        :param drop: localização de permitida soltura do objeto
        :param kwargs: lista de parametros nome=URL que geram elementos com este nome e a dada imagem

        """

    _score = None
    limbo = html.DIV(style=LSTYLE)
    
    def __init__(self, img="", vai=None, style=NDCT, tit="", alt="",
                 x=0, y=0, w=100, h=100, texto='',
                 cena=INVENTARIO, score=NDCT, drag=False, drop='', **kwargs):
        self._auto_score = self.score if score else self._auto_score
        self.img, self.title, self.real, self.alt = img, tit, drop, alt
        self._drag = self._over = self._drop = self._dover = self.vai = lambda *_: None
        self.nome = "_NO_NAME_"
        self.cena = cena
        self.opacity = 0
        self.texto = texto
        self.vai = Texto(cena, texto, foi=self.foi).vai if texto else vai if vai else self.vai
        
        # height = style["height"] if "height" in style else style["maxHeight"] if "maxHeigth" in style else 100
        # height = height[:-2] if isinstance(height, str) and "px" in height else height
        self.style = dict(**PSTYLE)
        self.style.update(**{'position': 'absolute', 'overflow': 'hidden',
                             'left': x, 'top': y, 'width': '{}px'.format(w), 'height': '{}px'.format(h),
                             'background-image': 'url({})'.format(img),
                             'background-position': '{} {}'.format(0, 0),
                             'background-size': '{}px {}px'.format(w, h)
                             })
        # self.style["min-width"], self.style["min-height"] = w, h
        self.style.update(**style)
        self.elt = html.DIV(Id=tit + drop, title=tit, style=self.style)
        self.xy = (-111, -111)
        self.scorer = dict(ponto=1, valor=cena.nome, carta=tit or img, casa=self.xy, move=None)
        self.scorer.update(score)
        # if False:
        #     self.img = html.IMG(Id="img_" + tit, src=img, title=tit, alt=alt,
        #                         style=EIMGSTY)  # width=self.style["width"])
        #     self.elt <= self.img
        self.elt.onclick = self._click
        #self.c(**kwargs)
        # _ = Dragger(self.elt) if drag else None
        # _ = Droppable(self.elt, drop, self.vai) if drop else None
        _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
        self.elt.ondragstart = lambda ev: self._drag(ev)
        self.elt.onmouseover = lambda ev: self._over(ev)
        self.elt.ondrop = lambda ev: self._drop(ev)
        self.elt.ondragover = lambda ev: self._dover(ev)
        # self.img.onmousedown = self.img_prevent
        self.do_drag(drag)
        self.do_drop(drop)
        #Elemento._scorer_()
    def do_score(self, tit):
        if tit not in FIX_SCORE:
            FIX_SCORE[tit] = int(Elemento._score.score_.html) + 1
            Elemento._score.score_.html = FIX_SCORE[tit]
            
    @classmethod
    def _scorer_(cls):
        Elemento._scorer_ = lambda *_ : None
        Elemento._score = scr = Elemento(SCORE)
        scr.score_ = html.H2("0")
        scr.elt <= scr.score_
        scr.entra(INVENTARIO)
        
    def move(x,y):
        self.elt.style.top = x
        self.elt.style.left = y
        
        
        
    def _click(self, ev=NoEv()):
        self.xy = (ev.x, ev.y)
        ev.stopPropagation()
        return self.vai(ev)
      
    def entra(self, cena, style=NOSC):
        styler = dict(self.style)
        styler.update(style)
        self.elt.style = styler
        self.cena = cena
        self.scorer.update(valor=cena.nome, move=self.xy,
                           casa=(styler["left"], styler["top"] if "top" in styler else 0))
        self._auto_score(**self.scorer)
        cena.elt <= self.elt
        
    def _auto_score(self, **kwargs):
         pass


    def foi(self):
        self._do_foi()

    def _do_foi(self):
        style = {'opacity': "inherited", 'width': 30, 'height': "30px", 'min-height': '30px', 'float': 'left',
                 'position': 'unset', 'overflow': 'hidden',
                 'background-image': 'url({})'.format(self.img),
                 'background-position': '{} {}'.format(0, 0),
                 'background-size': '{}px {}px'.format(30, 20),
                 }
        self.do_drag(False)
        # Texto(self.cena, "Finally,got my correct name: {}".format(self.tit)).vai()
        _texto = self.texto if self.tit == self.title else CORRECT.format(self.tit)
        self.vai = Texto(self.cena, _texto).vai

        clone_mic = Elemento(self.img, tit=self.title, drag=True, style=style, cena=INVENTARIO)
        clone_mic.entra(INVENTARIO)
        self._do_foi = lambda *_: None

    @property
    def tit(self):
        return self.elt.title

    @tit.setter
    def tit(self, texto):
        self.elt.title = texto

    def img_prevent(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        return False

    def mouse_over(self, ev):
        # ev.preventDefault()
        ev.target.style.cursor = "pointer"
        return False

    def img_drag_start(self, ev):
        # ev.preventDefault()
        ev.stopPropagation()
        return False

    def drag_start(self, ev):
        # ev.preventDefault()
        ev.stopPropagation()
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'
        return False

    def do_drag(self, drag=True):
        self.elt.draggable = drag
        if drag:
            self._drag = self.drag_start
            self._over = self.mouse_over
        else:
            self._drag = self._over = lambda *_: None

    def do_drop(self, drop=""):
        if drop:
            self._drop = self.drop
            self._dover = self.drag_over
        else:
            self._drop = self._dover = lambda *_: None

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
        return False

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        tit = doc[src_id].title
        #if tit != self.real:
           # Texto(self.cena, "Hey, this is not my name: {}.".format(tit)).vai()
            #return False
        self.tit = tit
        #Texto(self.cena, "Finally, my correct name: {}.".format(self.tit)).vai()
        doc[src_id].remove()
        self.do_score(tit)
        self.do_drag(False)
        # Texto(self.cena, "Finally,got my correct name: {}".format(self.tit)).vai()
        _texto = self.texto if self.tit == self.title else CORRECT.format(self.tit)
        self.vai = Texto(self.cena, _texto, foi=self.foi).vai
        #self._do_foi = lambda *_: None
        
    def doit_drop(src_id, x, y):
        self.tit = tit
        Texto(self.cena, "Finally, my correct name: {}.".format(self.tit)).vai()
        doc[src_id].remove()
        self.do_score(tit)
        self.do_drag(False)
        # Texto(self.cena, "Finally,got my correct name: {}".format(self.tit)).vai()
        _texto = self.texto if self.tit == self.title else CORRECT.format(self.tit)
        self.vai = Texto(self.cena, _texto, foi=self.foi).vai

        
    @classmethod
    def c(cls, **kwargs):
        return [setattr(cls, nome, Elemento(**img) if isinstance(img, dict) else Elemento(img=img))
        for nome, img in kwargs.items()]
        
FUNDO = "https://imagens.simplo7.net/static/2497/sku/thumb_tricoline-100-algodao-lisa-tricoline-100-algodao-lisa-branca-1474467553683.jpg"
BACKG = "https://i.imgur.com/5QRsbVs.jpg"
SETA = "https://trabalhodigitalinfo.files.wordpress.com/2016/01/seta-vermelha-2png.png"




def teste():
    fundo = Cena(FUNDO)
    backg = Elemento(BACKG,tit = "estatico", drag= False, x=0, y=0,
        w = 800 , h = 600, drop= "fundo",
        cena= fundo)
    def reposiciona_figura(sid, x, y):
        sid.style.left = x
        sid.style.top = y
        
    seta = Elemento(SETA, tit = "Mova-me", drag=True,
        x = 50, y = 50, w = 300, h = 300, drop="backg",
        cena=fundo)
        
    backg.doit_drop = reposiciona_figura
    fundo.vai()

teste()    

        
        

