# ada.kellee.main.py
texto = "Vovó viu a uva"
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

def trigonometria():
    INVENTARIO.inicia()
    n_trig = Cena(trig_n)
    e_trig = Cena(trig_e, esquerda=n_trig)
    s_trig = Cena(trig_s, esquerda=e_trig)
    o_trig = Cena(trig_o, esquerda=s_trig, direita=n_trig)
    n_trig.esquerda, n_trig.direita = o_trig, e_trig
    s_trig.direita, e_trig.direita = o_trig, s_trig
    chistyle = dict(left = 610, top = 140, width = 80, maxHeight = "90px")
    globstyle = dict(left = 160, top = 210, width = 80, maxHeight = "100px")
    volcstyle = dict(left = 30, top = 500, width = 100, maxHeight = "120px")
    vdgball = Elemento(ball, tit = "earth globe", drag=True,
        style=chistyle, cena=e_trig, vai=Texto(e_trig,"please, help me, fix my name",
        foi=lambda: INVENTARIO.bota(vdgball)).vai)
    eglobe = Elemento(globe, tit = "volcano", drag=True,
        style=globstyle, cena=o_trig, vai=Texto(o_trig,"please, help me, fix my name",
        foi=lambda: INVENTARIO.bota(eglobe)).vai)
    volc = Elemento(volcano, tit = "glow ball", drop="volcano",
        style=volcstyle, cena=o_trig, vai=Texto(o_trig,"please, help me, fix my name",
        foi=lambda: INVENTARIO.bota(eglobe)).vai)
    txtchildren = Texto(n_trig,"please, help me")
    e_trig.vai()
    
    
#trigonometria()
from roxanne.main import test

test()