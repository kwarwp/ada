# ada.adda.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import choice
from browser import timer
STYLE ["width"] = 1155 #img de fundo
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
fire2 = "https://i.imgur.com/I5eZveE.png"
fire3 = "https://i.imgur.com/Gw9pNuR.png"
fire4 = "https://i.imgur.com/tANP62N.png"
fire5 = "https://i.imgur.com/TCG2mkF.png"
os_fire = [fire1,fire2,fire3,fire4,fire5]
os_glows = [glow1,glow2,glow3,glow4,glow5]
cena = Cena(wall)
window = Elemento(window_,style=dict(left=0,top=-50,width="420px",height="600px",overflow="hidden"))
window.img.style=dict(position="relative",left="-200px")
window2 = Elemento(window_2,style=dict(left=735,top=-45,width="420px",height="590px",overflow="hidden"))
window2.img.style=dict(position="relative",right="-230px")
torch = Elemento(torch_,style=dict(left=-66,top=-5,width="600px",height="400px"))
torch_2 = Elemento(torch_2,style=dict(left=650,top=-4,width="600px",height="400px"))
glow1 = Elemento(glow1,style=dict(left=-15,top=0,width="500px",height="400px",opacity=0.7))
glow_1= Elemento(glow_1,style=dict(left=700,top=0,width="500px",height="400px",opacity=0.7))
door = Elemento(door,style=dict(left=-20,top=7,width="1200px",height="612px"))
os_fire1 = Elemento(os_fire,style=dict(left=180,top=-103,width="600px",height="300px"))
os_fire2 = Elemento(os_fire,style=dict(left=900,top=-103,width="600px",height="300px"))
#dark= Elemento("",style=dict(width="960px",height="600px",backgroundColor="black",opacity=0.5))
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
o_glow = 0
def troca_glow(ev=0): #efeito gif
    global o_glow
    glow1.img.src= choice(os_glows) #os_glows[o_glow]
    glow_1.img.src= choice(os_glows) #os_glows[o_glow]
    o_glow += 1
    if o_glow > 4:
        o_glow = 0
troca_glow()
timer.set_interval(troca_glow,200)