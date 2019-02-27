# ada.adda.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import choice
from browser import timer
STYLE ["width"] = 960
STYLE ["height"] = "600px" 
wall = "https://i.imgur.com/y2Cmt0D.png"
floor = "https://i.imgur.com/hQGOZGZ.png"
window_= "https://i.imgur.com/O1pEa77.png"
window_2 = "https://i.imgur.com/996rAAB.png"
torch_= "https://i.imgur.com/lnuZO60.gif"
torch_2 = "https://i.imgur.com/lnuZO60.gif"
glow1= "https://i.imgur.com/qlN7awe.png"
glow_1= "https://i.imgur.com/qlN7awe.png"
glow2= "https://i.imgur.com/bCji6HU.png"
glow3= "https://i.imgur.com/GHc47CQ.png"
glow4= "https://i.imgur.com/W3OysVW.png"
glow5= "https://i.imgur.com/EajKgg3.png"
os_glows= [glow1,glow2,glow3,glow4,glow5]
cena = Cena(wall)
elemento = Elemento(floor,style=dict(width="960px",height="900px"))
window = Elemento(window_,style=dict(left=190,top=-50,width="420px",height="600px"))
window2 = Elemento(window_2,style=dict(left=370,top=-50,width="420px",height="600px"))
torch = Elemento(torch_,style=dict(left=-55,top=-5,width="500px",height="400px"))
torch_2 = Elemento(torch_2,style=dict(left=540,top=-4,width="500px",height="400px"))
glow1= Elemento(glow1,style=dict(left=-55,top=0,width="500px",height="400px",opacity=0.5))
glow_1= Elemento(glow_1,style=dict(left=540,top=0,width="500px",height="400px",opacity=0.7))
dark= Elemento("",style=dict(width="960px",height="600px",backgroundColor="black",opacity=0.5))
elemento.entra(cena)
window.entra(cena)
window2.entra(cena)
torch.entra(cena)
torch_2.entra(cena)
glow1.entra(cena)
glow_1.entra(cena)
dark.entra(cena)
cena.vai()
o_glow = 0
def troca_glow(ev=0):
    global o_glow
    glow1.img.src= os_glows[o_glow]#choice(os_glows)
    glow_1.img.src= os_glows[o_glow]#choice(os_glows)
    o_glow += 1
    if o_glow > 4:
        o_glow = 0
troca_glow()
timer.set_interval(troca_glow,200)