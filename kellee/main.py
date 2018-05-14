# ada.kellee.main.py
texto = "VovÃÂ´ viu a maÃÂ§ÃÂ£ ubiqÃÂ¼a"
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/4fTrn8X.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"
leyden  = "https://i.imgur.com/abeXKwL.jpg"
volcano  = "https://i.imgur.com/4Y5aie8.jpg"
globe  = "https://i.imgur.com/EQtHzod.jpg"
ball  = "https://i.imgur.com/rBbRsFU.jpg"
trig_s  = "https://i.imgur.com/9ZcjTjb.jpg"
trig_o  = "https://i.imgur.com/SyHdvjw.jpg"
trig_n  = "https://i.imgur.com/ChRcEvB.jpg"
trig_e  = "https://i.imgur.com/JD6oGRg.jpg"
class EleDG(Elemento):

    def __init__(self, img="", vai=None, style={}, tit="", alt="",
                 cena=None, score={}, drag=False, drop='', **kwargs):
        Elemento.__init__(self, img=img, vai=vai, style=style, cena=cena, tit=tit, alt=alt)
        _ = Dragger(self.elt) if drag else None
        _ = Droppable(self.elt, drop, self.vai) if drop else None
        _ = self.entra(cena) if cena else None

class Text(Texto):
    def __init__(self, cena=None, tit="", txt="", foi=None, **kwargs):
        Texto.__init__(self, cena=cena, tit=tit, txt=txt, **kwargs)
        self.esconde = foi if foi else self.esconde

def trigonometria():

    n_trig = Cena(trig_n)
    e_trig = Cena(trig_e, esquerda=n_trig)
    s_trig = Cena(trig_s, esquerda=e_trig)
    o_trig = Cena(trig_o, esquerda=s_trig, direita=n_trig)
    n_trig.esquerda, n_trig.direita = o_trig, e_trig
    s_trig.direita, e_trig.direita = o_trig, s_trig
    chistyle = dict(left = 610, top = 90, width = 80, maxHeight = "80px")
    globstyle = dict(left = 310, top = 90, width = 80, maxHeight = "80px")
    volcstyle = dict(left = 30, top = 500, width = 100, maxHeight = "120px")
    #chistyle.update({"max-height" = 200})
    vdgball = EleDG(ball, tit = "earth globe", drag=True,
    style=chistyle, cena=e_trig, vai=Text(e_trig,"please, help me",
        foi=lambda: INVENTARIO.bota(vdgball)).vai)
    eglobe = EleDG(globe, tit = "volcano", drag=True,
    style=globstyle, cena=o_trig, vai=Text(o_trig,"please, help me",
        foi=lambda: INVENTARIO.bota(eglobe)).vai)
    volc = EleDG(volcano, tit = "glow ball", drop="volcano",
    style=volcstyle, cena=o_trig, vai=Text(o_trig,"please, help me",
        foi=lambda: INVENTARIO.bota(eglobe)).vai)
    txtchildren = Texto(n_trig,"please, help me")
    e_trig.vai()
    
    
trigonometria()