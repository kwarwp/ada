# ada.natalia.main.py
from _spy.vitollino.main import Cena,Elemento 
from _spy.vitollino.main import INVENTARIO as inv
CANADA= "https://www.estudopratico.com.br/wp-content/uploads/2019/04/ottawa-capital-canada.jpg"
SALA= " https://cdn.imgbin.com/17/18/18/imgbin-kim-taehyung-bts-k-pop-tomorrow-exo-others-B9xAfxjVW72prTfKWQzahU4PQ.jpg"
class anna():
    sala=Elemento(img=SALA)
    canada=Cena(img=CANADA)
    sala.entra(canada)
    canada.vai()
#anna()
class Numer:
    def __init__(self, name):
        words = name.split()
        orda = ord('a') - 1
        nums = [self.alka(ord(lt)- orda) for ws in words for lt in words]
        print(nums)
        
    def alka(self, alk):
        return alk if alk < 10 else alk//10 + alk%10
        
Numer('jonh doe')
        
