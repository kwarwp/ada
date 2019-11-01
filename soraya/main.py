# ada.soraya.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
CIDADE="http://4.bp.blogspot.com/-rcUdRcSt1J4/UwPgVCvTHBI/AAAAAAAAALc/wyg_Gb2FPHs/s1600/Autumn-Town.jpg"
JG="https://img2.gratispng.com/20180407/syq/kisspng-roblox-deviantart-digital-art-rendering-cartoon-character-5ac8e863845911.7926442315231161315421.jpg"
class metropolis():
    cidade= Cena(img=CIDADE)
    jg= Elemento(img=JG)
    jg.entra(cidade)
    cidade.vai()
metropolis()