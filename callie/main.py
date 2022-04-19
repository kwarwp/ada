from _spy.vitollino.main import Cena, Elemento, STYLE
from random import randint
from browser import alert
STYLE.update(width=850, height="650px")

IMGUR = "https://i.imgur.com/{}.jpg"
GOGHRoom ="https://i.imgur.com/CRNsfXO.jpg"
FUNDO = "qWcEao4"
GOGHIntru = "https://i.imgur.com/nVpyITK.png"
CITY1 = "https://i.imgur.com/jiJY1NY.jpg"
LAND1 = "https://i.imgur.com/GsdFmpz.jpg"
CENAS = "CRNsfXO swVe1IW jiJY1NY GsdFmpz T6pmXbY dJ4WOIh".split()
CENAS_ = "swVe1IW nVpyITK     "
OFF = 2000

class Cubos:
    def __init__(self, cenas, tw=800, th=500, nx=4, ny=3):
        class Face(Elemento):
            def __init__(self,cubo, inx, face, **kwargs):
                self.cubo = cubo
                w, h = tw//nx, th//ny
                self.dh = h
                x, y = (inx % nx)*w, (inx // nx)*h
                super().__init__(IMGUR.format(face), x=x, y=y-OFF, w=w, h=h, cena=cena, vai=self.vai)
                self.siz = (tw, th)
                self.pos = (-x, -y)
                self.quad = 0
            def show(self):
                self.y += OFF if self.y < -10  else 0
                return True
            def hide(self):
                self.y -= OFF if self.y > 10  else 0
                return False
            def orient(self, ori):
                self.elt.style.transform="rotate({ori*90}deg)"
                return False
            def vai(self, evt):
                e = evt.target;
                dim = e.getBoundingClientRect()
                x = evt.clientX - dim.left
                y = evt.clientY - dim.top
                e, n, h  = x-y, x+y , self.dh
                self.quad = 0
                self.quad = 0 if (e > 0) and ( n <h) else 1 if (e > 0) and ( n >h) else 3 if (e < 0) and ( n >h) else 2
                #self.quad += 1 if  > self.h else -1
                alert(f"x: {x} y: {y} qd: {self.quad}")
                self.cubo.roll(randint(0,5))
        class Cubo:
            ROLL = [[16,4,20,12],[18,8,22,0],[17,12,23,4],[16,0,20,8],[6,1,12,11],[12,3,6,10]]
            def __init__(self,inx, faces, **kwargs):
                self.faces = [Face(cubo=self, inx=inx, face=face) for face in faces]
                self.face, self.orient = 0, 0
            def roll(self,inx):
                facer, self.orient = inx//4, inx % 4
                self.face = [face.show() if facer == face_index else face.hide()
                             for face_index, face in enumerate(self.faces)].index(True)
        cena = Cena(IMGUR.format(FUNDO)).vai()
        #el = Elemento(IMGUR.format(FUNDO), cena=cena)
        cubos = [Cubo(inx=inx, faces=cenas) for inx in range(12)]
        [cube.roll(randint(0,23)) for cube in cubos]
#Drag and drops: Elemento -> na Cena; Elemento -> Elemento; Elemento para inventário

if __name__ == "__main__":
    Cubos(CENAS)



