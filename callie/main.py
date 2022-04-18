from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=850, height="650px")

IMGUR = "https://i.imgur.com/{}.jpg"
GOGHRoom ="https://i.imgur.com/CRNsfXO.jpg"
FUNDO = "qWcEao4"
GOGHIntru = "https://i.imgur.com/nVpyITK.png"
CITY1 = "https://i.imgur.com/jiJY1NY.jpg"
LAND1 = "https://i.imgur.com/GsdFmpz.jpg"
CENAS = "CRNsfXO nVpyITK jiJY1NY GsdFmpz T6pmXbY dJ4WOIh "
CENAS_ = "swVe1IW      "
OFF = 2000

class Cubos:
    def __init__(self, cenas, tw=800, th=500, nx=4, ny=3):
        class Face(Elemento):
            def __init__(self,inx, face, **kwargs):
                w, h = tw//nx, th//ny
                x, y = (inx % nx)*w, (inx // nx)*h
                super().__init__(IMGUR.format(face), x=x, y=y-OFF, w=w, h=h, cena=cena)
                self.siz = (tw, th)
                self.pos = (-x, -y)
            def show(self):
                self.y += OFF if self.y < -10  else 0
            def hide(self):
                self.y -= OFF if self.y > 10  else 0
        class Cubo:
            def __init__(self,inx, faces, **kwargs):
                self.faces = [Face(inx=inx, face=face) for face in faces]
            def roll(self,inx):
                [face.show() if inx == face_index else face.hide() for face_index, face in enumerate(faces)]
        cena = Cena(IMGUR.format(FUNDO)).vai()
        #el = Elemento(IMGUR.format(FUNDO), cena=cena)
        cubos = [Cubo(inx=inx, faces=cenas) for inx in range(12)]
        [cube.roll(0) for cube in cubos]
#Drag and drops: Elemento -> na Cena; Elemento -> Elemento; Elemento para inventário

if __name__ == "__main__":
    Cubos(CENAS)



