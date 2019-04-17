# ada.adda.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import choice
from browser import timer
STYLE ["width"] = 1345 #img de fundo
STYLE ["height"] = "600px" #img de fundo

wall = "https://i.imgur.com/OclGL7S.png" #adc imagem
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


os_fire = [fire1,fire2,fire3,fire4,fire5] #list para gif
os_glows = [glow1,glow2,glow3,glow4,glow5]
fire_offset = {fire1:100,fire_1:200,fire2:300,fire_2:500,fire3:600,fire_3:700,fire4:800,fire_4:900}
cena = Cena(wall)

#abaixo como dimensionar o objeto
window = Elemento(window_,style=dict(left=0,top=-50,width="420px",height="600px",overflow="hidden"))
window.img.style=dict(position="relative",left="-200px")
window2 = Elemento(window_2,style=dict(left=925,top=-45,width="420px",height="600px",overflow="hidden"))
window2.img.style=dict(position="relative",right="-230px")
torch = Elemento(torch_,style=dict(left=-40,top=-5,width="600px",height="400px"))
torch_2 = Elemento(torch_2,style=dict(left=800,top=-4,width="600px",height="400px"))
glow1 = Elemento(glow1,style=dict(left=-0,top=0,width="500px",height="400px",opacity=0.7))
glow_1= Elemento(glow_1,style=dict(left=780,top=0,width="500px",height="400px",opacity=0.7))
door = Elemento(door,style=dict(left=-20,top=7,width="1200px",height="612px"))
fire1 = Elemento(fire1,style=dict(left=180,top=-103,width="600px",height="300px"))
fire_1 = Elemento(fire_1,style=dict(left=900,top=-103,width="600px",height="300px"))
#fire2 = Elemento(fire2,style=dict(left=65,top=-103,width="600px",height="300px"))
#fire_2 = Elemento(fire_2,style=dict(left=785,top=-103,width="600px",height="300px"))
#fire3 = Elemento(fire3,style=dict(left=-50,top=-103,width="600px",height="300px"))
#fire_3 = Elemento(fire_3,style=dict(left=660,top=-103,width="600px",height="300px"))
#fire4 = Elemento(fire4,style=dict(left=-160,top=-103,width="600px",height="300px"))
#fire_4 = Elemento(fire_4,style=dict(left=550,top=-103,width="600px",height="300px"))
#fire5 = Elemento(fire5,style=dict(left=430,top=-103,width="600px",height="300px"))
#fire_5 = Elemento(fire_5,style=dict(left=-280,top=-103,width="600px",height="300px"))
os_fire1 = Elemento(os_fire,style=dict(left=180,top=-103,width="600px",height="300px"))
#dark= Elemento("",style=dict(width="960px",height="600px",backgroundColor="black",opacity=0.5))

window.entra(cena)#como fazer a imagem aparecer na tela
window2.entra(cena)
torch.entra(cena)
torch_2.entra(cena)
glow1.entra(cena)
glow_1.entra(cena)
door.entra(cena)
fire1.entra(cena)
fire_1.entra(cena)
#fire2.entra(cena)
#fire_2.entra(cena)
#fire3.entra(cena)
#fire_3.entra(cena)
#fire4.entra(cena)
#fire_4.entra(cena)
#fire5.entra(cena)
#fire_5.entra(cena)
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
    thefire1 = coice(os_fire)
    r1,r2 = rect [thefire1], rect [thefire1] + 100
    rect1 = {"clip": f"rect({r1}px,0px,{r2}px,100px)"}
    fire1.img.src= choice(os_fire) #os_glows[o_glow]
    fire1.img.style = rect1
    fire_1.img.src= choice(os_fire) #os_glows[o_glow]
    '''fire2.img.src= choice(os_fire)
    fire_2.img.src= choice(os_fire)
    fire3.img.src= choice(os_fire)
    fire_3.img.src= choice(os_fire)
    fire4.img.src= choice(os_fire)
    fire_4.img.src= choice(os_fire)
    fire5.img.src= choice(os_fire)
    fire_5.img.src= choice(os_fire)'''
    o_fire += 1
    if o_fire > 4:
        o_fire = 0
troca_fire()
timer.set_interval(troca_fire,100)