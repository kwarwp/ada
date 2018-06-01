# ada.parisa.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.blue #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600
silv = dict(color=color.white, opacity=0.4)
hull = dict(color=color.yellow)
#s = shapes.rectangle(width=10, height=6)
h1=sphere(pos=(1.5, -0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.black)
h2=sphere(pos=(1.5, 0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.black)
#pyramid(pos=(1, -0.5, 0),size=(0.5,0.1,1), axis=(0,1,0), color=color.black)
# --- hull ---
aft=sphere(pos=(2, 0, 0), size=(1,1,2), color=color.yellow)
fr=sphere(pos=(6, 0, 0), size=(1,1,2), color=color.yellow)
body=cylinder(pos=(2, 0, 0), size=(4,1,2) , color=color.yellow)
# --- cockpit ---
caft=sphere(pos=(5, 0.2, 0), size=(1,1,2), **silv)
cfor=sphere(pos=(6.2, 0.2, 0), size=(1,1,2), **silv)
cbody=cylinder(pos=(5, 0.2, 0), size=(1.2,1,2) , **silv)
# --- periscope ---
paft=sphere(pos=(5, 2, 0), size=(0.4,0.4,0.4), **hull)
pfor=sphere(pos=(5.2, 2, 0), size=(0.3,0.5,0.5), **silv)
ptub=cylinder(pos=(5.0, 2, 0), size=(0.2,0.4,0.4), **hull)
pbody=cylinder(pos=(5, 0, 0), axis=(0,1,0), size=(2,0.4,0.4) , **hull)
per = [paft, pfor, ptub, pbody]
# --- portholes ---
phs = [sphere(pos=(x/2+2.2, 0.15, 0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
php = [sphere(pos=(x/2+2.2, 0.15, -0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
pts = [h1, h2, aft, fr, body, caft, cfor, cbody]+per+php+phs
sup = compound(pts, pos=(-1,0,0))
def sail(*_):
    sup.pos = vec(-1+x,0,0)

for x in range(10):
    rate(sail, 10)
    # sup.pos = vec(-1+x,0,0)
