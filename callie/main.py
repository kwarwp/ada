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
OFX, OFY = 100, 50

class Cubos:
    CUBOS = None
    def write(self, text):
        self.el.elt.html = text
        
    def __init__(self, cenas, tw=600//3*4, th=600, nx=4, ny=3):
        class Face(Elemento):
            def __init__(self,cubo, inx, face, **kwargs):
                self.cubo = cubo
                w, h = tw//nx, th//ny
                self.dh = h
                x, y = (inx % nx)*w, (inx // nx)*h
                super().__init__(IMGUR.format(face), x=x+OFX, y=y-OFF+OFY, w=w, h=h, cena=cena, vai=self.vai)
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
                self.elt.style.transform=f"rotate({ori*90}deg)"
                return False
            def vai(self, evt):
                e = evt.target;
                dim = e.getBoundingClientRect()
                x = evt.clientX - dim.left
                y = evt.clientY - dim.top
                e, n, h  = x-y, x+y , self.dh
                self.quad = 0
                self.quad = 0 if (e > 0) and ( n <h) else 1 if (e > 0) and ( n >h) else 2 if (e < 0) and ( n >h) else 3
                #self.quad += 1 if  > self.h else -1
                Cubo.CUBOS.write(f"x: {x} y: {y} qd: {self.quad}")
                #self.cubo.roll(randint(0,5))
                self.cubo.go(self.quad)
        class Cubo:
            ROLL = [
                [[19,4,21,12],[18,8,22,0],[17,12,23,4],[16,0,20,8],[6,1,12,11],[12,3,6,10]],
                [[5,22,13,16],[9,23,1,19],[13,20,5,18],[1,21,9,17],[2,13,8,7],[0,7,10,13]],
                [[23,14,17,6],[20,2,16,10],[21,6,19,14],[22,10,18,2],[14,9,4,3],[4,11,14,1]],
                [[15,18,7,20],[3,17,11,21],[7,16,15,22],[11,19,3,23],[10,5,0,15],[8,15,2,5]],
                ]
            def __init__(self,inx, faces, **kwargs):
                self.faces = [Face(cubo=self, inx=inx, face=face) for face in faces]
                self.face, self.orient = 0, 0
            def roll(self,inx):
                facer, self.orient = inx//4, inx % 4
                self.face = [face.show() if facer == face_index else face.hide()
                             for face_index, face in enumerate(self.faces)].index(True)
                self.faces[self.face].orient(self.orient)
                Cubo.CUBOS.write("completou com sucesso") if Cubo.CUBOS.complete() else None
            @property
            def inx(self):
                return self.face *4 + self.orient
            def go(self,inx):
                go_face_roll = Cubo.ROLL[self.orient][self.face][inx]
                fc0, ot0 = self.face, self.orient
                self.roll(go_face_roll)
                fc1, ot1 = self.face, self.orient
                Cubo.CUBOS.write(f"inx: {inx} face: {fc0} ori: {ot0} gfr: {go_face_roll} face: {fc1} ori: {ot1} ")
        cena = Cena(IMGUR.format(FUNDO)).vai()
        Cubo.CUBOS = self
        self.el = Elemento(IMGUR.format(FUNDO),w=300, cena=cena, style={"color": "white"})
        self.cubos = cubos = [Cubo(inx=inx, faces=cenas) for inx in range(12)]
        [cube.roll(randint(0,23)) for cube in cubos]
        #[cube.roll(0) for cube in cubos]
    def complete(self):
        return len(set(cubo.inx for cubo in self.cubos)) = 1
#Drag and drops: Elemento -> na Cena; Elemento -> Elemento; Elemento para inventário

if __name__ == "__main__":
    Cubos(CENAS)



