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
        # cena  = Cena(WHITE).vai()
        base = document["pydiv"]
        self.rect, self.path = svg.rect, svg.path
        self.hue = (0, 360)
        self.color = (255, 100, 100)
        base.html = ''
        self.tela = svg.svg(width=1200, height=700)
        base <= self.tela
        #[tela <= svg.rect(x=randint(0,ix%20)*40, y=randint(0,ix%15)*50, width="40", height=50,
        #[tela <= svg.rect(x=randint(0,30)*40, y=randint(0,15)*50, width="40", height=50,
    def bandeira(self, x, y, style, **_):
        x += randint(-9, 9)
        y += randint(-9, 9)
        path = self.path(d=f"M{x} {y} h40 v50 l-20 -20 l-20 20 v-40 Z", style=style)
        path.onclick = self.main
        return path
    def main(self, *_):
        from random import randint
        r, g, b = self.color
        self.tela.html = ''
        self.tela <= self.rect(width=1200, height=700, style={f"fill":'white'})
        [self.tela <= self.bandeira(x=randint(0,30)*40, y=randint(0,15)*50, width="40", height=50,
        style={"fill":f'rgb({r},{g},{b})','filter': f'hue-rotate({randint(*self.hue)}deg)'}) for ix in range(900)]

class Labir:
    def __init__(self):
        from browser import svg, document
        rosa = [(1,0),(0,-1),(-1,0),(0,1)]*20
        self.last = (500,200)
        def block(dd):
            nx, ny = rosa.pop(0)
            ox, oy = self.last
            nx, ny = ox+nx*20, oy-ny*20
            self.last = (nx, ny)
            return svg.rect(width=400-dd*20, height=400-dd*20, x=nx, y=ny,
                style={"fill":'rgb(255,0,0)','filter': f'hue-rotate({dd*48}deg)', 'opacity':0.2})
        # cena  = Cena(WHITE).vai()
        base = document["pydiv"]
        base.html = ''
        tela = svg.svg(width=1200, height=700)
        base <= tela
        [tela <= block(dd) for dd in range(4)]
Volpi().main()
#Labir()
