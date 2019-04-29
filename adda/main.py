# ada.adda.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import choice
from browser import timer

#img de fundo
STYLE ["width"] = 1345 
STYLE ["height"] = "600px" 
FIRE_L = 215
FIRE_R = 200+850
def _get_fire(ix,fire1_): 
    r1,r2 = fire_offset [ix], fire_offset [ix] + 400
    rect1 = {"clip": f"rect(0px,{r2}px,600px,{r1}px)", "position": "absolute"}
    fire1_.img.src= ix #os_glows[o_glow]
    fire1_.img.style = rect1
    return ix

#adc imagem
wall = "https://i.imgur.com/OclGL7S.png" 
window_= "https://i.imgur.com/O1pEa77.png"
window_2 = "https://i.imgur.com/mHVwSU8.png"
torch_= "https://i.imgur.com/GYdWkb0.png"
torch_2 = "https://i.imgur.com/GYdWkb0.png"
glow1 = "https://i.imgur.com/qlN7awe.png"
glow_1 = "https://i.imgur.com/qlN7awe.png"
glow2 = "https://i.imgur.com/bCji6HU.png"
glow3 = "https://i.imgur.com/GHc47CQ.png"
glow4 = "https://i.imgur.com/W3OysVW.png"
glow5 = "https://i.imgur.com/EajKgg3.png"
door = "https://i.imgur.com/MwjexQO.png"
fire1 = "https://i.imgur.com/dNHUPQZ.png"
fire_1 = "https://i.imgur.com/dNHUPQZ.png"
fire2 = "https://i.imgur.com/I5eZveE.png"
fire_2 = "https://i.imgur.com/I5eZveE.png"
fire3 = "https://i.imgur.com/Gw9pNuR.png"
fire_3 = "https://i.imgur.com/Gw9pNuR.png"
fire4 = "https://i.imgur.com/tANP62N.png"
fire_4 = "https://i.imgur.com/tANP62N.png"
fire5 = "https://i.imgur.com/TCG2mkF.png"
fire_5 = "https://i.imgur.com/TCG2mkF.png"

#list para gif
os_fire = [fire1,fire2,fire3,fire4,fire5] 
os_glows = [glow1,glow2,glow3,glow4,glow5]
fire_offset = {fire1:10,fire2:120,fire3:230,fire4:350,fire5:470}
cena = Cena(wall)
def get_fire(ix,fire1_): 
    fire1_.elt.style.backgroundImage = f"url({ix})"
    fire1_.elt.style.overflow = "hidden"
    fire1_.elt.style.backgroundSize = f"600px 300px"
    fire1_.elt.style.backgroundPositionX = f"-{fire_offset[ix]}px"
    fire1_.elt.style.backgroundPositionY = "10px"
    return ix

#abaixo como dimensionar o objeto
window = Elemento(window_,style=dict(left=0,top=-50,width="420px",height="600px",overflow="hidden"))
window.img.style=dict(position="relative",left="-200px")
window2 = Elemento(window_2,style=dict(left=925,top=-45,width="420px",height="600px",overflow="hidden"))
window2.img.style=dict(position="relative",right="-230px")
torch = Elemento(torch_,style=dict(left=-40,top=-5,width="600px",height="400px"))
torch_2 = Elemento(torch_2,style=dict(left=800,top=-4,width="600px",height="400px"))
glow1 = Elemento(glow1,style=dict(left=-0,top=0,width="500px",height="400px",opacity=0.7))
glow_1= Elemento(glow_1,style=dict(left=850,top=0,width="500px",height="400px",opacity=0.7))
door = Elemento(door,style=dict(left=30,top=7,width="1300px",height="612px"))
os_fire1 = Elemento(None,style=dict(left=FIRE_L,top=-103,width="600px",height="300px"))
os_fire2 = Elemento(None,style=dict(left=FIRE_R,top=-103,width="600px",height="300px"))
os_fire3 = Elemento((fire2),style=dict(left=FIRE_L,top=-103,width="600px",height="300px"))
os_fire4 = Elemento((fire3),style=dict(left=FIRE_L,top=-103,width="600px",height="300px"))
os_fire5 = Elemento((fire4),style=dict(left=FIRE_L,top=-103,width="600px",height="300px"))

#dark= Elemento("",style=dict(width="960px",height="600px",backgroundColor="black",opacity=0.5))

#como fazer a imagem aparecer na tela
window.entra(cena)
window2.entra(cena)
torch.entra(cena)
torch_2.entra(cena)
glow1.entra(cena)
glow_1.entra(cena)
door.entra(cena)
os_fire1.entra(cena)
os_fire2.entra(cena)
#dark.entra(cena)
cena.vai()

o_glow = 0 #efeito gif glow
def troca_glow(ev=0): 
    global o_glow
    glow1.img.src= choice(os_glows)#efeito aleatorio #os_glows[o_glow] #efeito sincronizado
    glow_1.img.src= choice(os_glows) 
    o_glow += 1
    if o_glow > 4:
        o_glow = 0
troca_glow()
timer.set_interval(troca_glow,200)

o_fire = 0 #efeito gif fire
def troca_fire(ev=0): 
    global o_fire
    thefire1 = choice(os_fire)
    get_fire(thefire1, os_fire1)
    thefire2 = choice(os_fire)
    get_fire(thefire2, os_fire2)
    o_fire += 1
    if o_fire > 4:
        o_fire = 0
timer.set_interval(troca_fire,80)