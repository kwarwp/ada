# ada.natalia.main.py
from _spy.vitollino.main import Cena,Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv
CANADA= "https://www.estudopratico.com.br/wp-content/uploads/2019/04/ottawa-capital-canada.jpg"
SALA= " https://cdn.imgbin.com/17/18/18/imgbin-kim-taehyung-bts-k-pop-tomorrow-exo-others-B9xAfxjVW72prTfKWQzahU4PQ.jpg"
WHITE = "https://i.imgur.com/NXIQIja.jpg"
GREEN = 'https://i.imgur.com/ECVki8P.jpg'
STYLE.update(width=1300, height="700px")
'''
class anna():
    sala=Elemento(img=SALA)
    canada=Cena(img=CANADA)
    sala.entra(canada)
    canada.vai()
#anna()
'''
class Numer:
    def __init__(self, name):
        words = name.split()
        orda = ord('a') - 1
        nums = self.alka(sum(sum(self.alka(ord(lt)- orda) for lt in ws) for ws in words))
        print(nums)
        
    def alka(self, alk):
        return alk if alk < 10 else alk//10 + alk%10
        
#Numer('jon doe')
class Rainbow:
    def __init__(self):
        cena  = Cena(WHITE).vai()
        bar = Elemento(GREEN, w=40, h=600, cena=cena, style={'filter': 'hue-rotate(90deg)'})
        [Elemento(GREEN,x=ix*40, w=40, h=600-ix*30, cena=cena, style={'filter': f'hue-rotate({ix*20}deg)'}) for ix in range(20)]

class Rainbow2:
    def __init__(self):
        from browser import svg, document
        # cena  = Cena(WHITE).vai()
        base = document["pydiv"]
        base.html = ''
        tela = svg.svg(width=1200, height=700)
        base <= tela
        bar = svg.rect( width="300", height="100", style={"fill":'rgb(255,0,0)'})
        tela <= bar
        [tela <= svg.rect(x=ix*40, width="40", height=600-ix*30, style={"fill":'rgb(255,0,0)','filter': f'hue-rotate({ix*18}deg)'}) for ix in range(20)]


class Volpi:
    def __init__(self):
        from browser import svg, document
        from random import randint
        def bandeira(x, y, style, **_):
            x += randint(-9, 9)
            y += randint(-9, 9)
            return svg.path(d=f"M{x} {y} h40 v50 l-20 -20 l-20 20 v-40 Z", style=style)
        # cena  = Cena(WHITE).vai()
        base = document["pydiv"]
        base.html = ''
        tela = svg.svg(width=1200, height=700)
        base <= tela
        #[tela <= svg.rect(x=randint(0,ix%20)*40, y=randint(0,ix%15)*50, width="40", height=50,
        #[tela <= svg.rect(x=randint(0,30)*40, y=randint(0,15)*50, width="40", height=50,
        [tela <= bandeira(x=randint(0,30)*40, y=randint(0,15)*50, width="40", height=50,
        style={"fill":'rgb(255,100,100)','filter': f'hue-rotate({randint(0, 360)}deg)'}) for ix in range(900)]

Volpi()
