# ada.ruzwana.main.py
from browser import doc
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.blue #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600
box(color=color.red)
cylinder(color=color.blue)
tr = shapes.triangle(length=5)
