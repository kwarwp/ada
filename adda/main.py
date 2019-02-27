# ada.adda.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE ["width"] = 960
STYLE ["height"] = "600px" 
wall = "https://i.imgur.com/y2Cmt0D.png"
floor = "https://i.imgur.com/hQGOZGZ.png"
cena = Cena(wall)
elemento = Elemento(floor,style=dict(width="920px"))
elemento.entra(cena)
cena.vai()