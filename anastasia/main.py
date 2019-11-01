# ada.anastasia.main.py
from _spy.Vitollino.main import Cena,Elemento
from _spy.Vitollino.main import INVENTARIO as inv
BARBIE="https://www.bigw.com.au/medias/sys_master/images/images/hc6/h0c/12811409752094.jpg"
CIDADE="https://www.bigw.com.au/medias/sys_master/images/images/hc6/h0c/12811409752094.jpg"
class barbie():
    barbie= Elemento(img=BARBIE)
    cidade= Cena(img=CIDADE)
    cidade.entra(cidade)
    cidade.vai()
barbie()