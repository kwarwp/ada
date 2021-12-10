# ada.gatil.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE.update(width=1350, height="800px")
GATIL_MOS = "https://i.imgur.com/5ZISX93.jpg"


class Gatil(Cena):
    def __init__(self, img, x=0, y=0, w=1350, h=800):
        super().__init__(img)
        
Cena(GATIL_MOS).vai()