# ada.libby.main.py
from _spy.vitollino.main  import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
from browser import svg, document
CDD="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cidade_de_Deus.jpg"
FLASH="https://pngriver.com/wp-content/uploads/2018/03/Download-Flash-PNG-Pic-For-Designing-Projects.png"
class sempai():
    cdd= Cena(img=CDD)
    flash= Elemento(img=FLASH)
    flash.entra(cdd)
    cdd.vai()
#sempai()

class Box:
    def __init__(self, box):
        self.box = box
    def paint(self, box):
        self.box = box


class SvgPainter:
    def __init__(self):
        root = document["pydiv"]
        root.html = ""
        self.fill = "red"
        self.opacity = 0.6
        self.shape = dict(b=lambda x, y, w, h, it=self: svg.rect(x=x, y=y, width=w, height=h, fill=it.fill, fillOpacity=it.opacity))
        self.canvas = svg.svg(viewBox="0 0 1200 650", width=1200, height=650)
    def paint(self, shape="b", **kwargs):
        self.canvas <= self.shape[shape](**kwargs)
        
SvgPainter().paint("b", x=10, y=10, w=200, h=100)
        
