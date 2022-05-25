# ada.naomi.main.py
from _spy.vitollino.main import Cena, Elemento
from _spy.vitollino.main import INVENTARIO as inv 
STAR="http://media.comicbook.com/2017/10/central-city-the-flash-1038707.jpg"
CR7="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cristiano_Ronaldo_2018.jpg/399px-Cristiano_Ronaldo_2018.jpg"
class jogador():
    star=Cena(img=STAR)
    cr7=Elemento(img=CR7)
    cr7.entra(star)
    star.vai()
    cr7.direita(img=cr7)
jogador()    