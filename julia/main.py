# ada.julia.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from math import sqrt
from random import randint
from browser import timer
IMGSIZE = "240px"

class Sprite(Elemento):
    def __init__(self, x, y, image, cena, index=0):
        super().__init__(image, cena=cena, style=dict(left=x,top=x,width="80px",height="80px",overflow="hidden"))
        style = dict(position="relative",left=f"-{index%3*80}px",top=f"-{index//3*80}px", width=IMGSIZE, height=IMGSIZE)
        style.update({"max-width": IMGSIZE, "max-height": IMGSIZE})
        self.img.style=style
        

class Button(Sprite):
    BUTTONS = []
    def __init__(self, x, y, image, cena, index=0):
        super().__init__(x, y, image, cena, index)
        self.x, self.y, self.image, self.cena, self.index = x, y, image, cena, index
        self.grav, self.ele= 10, 10
        timer.set_timeout(self.move, 10)
    def move(self):
        self.x, self.y = self.x+ randint(-10,10), self.y+ randint(-10,10)
        self.img.style.left, self.img.style.top = self.x, self.y
        if 0< self.x < 800 and 0< self.y < 500:
            timer.set_timeout(self.move, 10)
    def _move(self):
        forces = zip(*[b.force(self.x) for b in Button.BUTTONS] if b != self)
        dx, dy = sum(forces[0]), sum(forces[1])
        self.x += int(dx)
        self.y += int(dy)
        self.img.style.left, self.img.style.top = self.x, self.y
        if dx > 1 or dy > 1:
            timer.set_timeout(self.move, 10)
            
    def force(self, x, y):
        dx, dy = x - self.x, y - self.y
        distance = sqrt(dx*dx + dy*dy)
        pull = 100.0 / min(0.1, distance) if distance > 90 else 0.0
        push = 100.0 / min(0.1, distance) if distance < 90 else 0.0
        return (-dx * pull + dx * push, -dy * pull + dy * push)
        
        
        
    def create(self):
        Button.BUTTONS = [Button(randint(0, 800), randint(0, 300), self.image, self.cena, index) for index in range(9)]
        return Button.BUTTONS

class Project:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        Buttons = "https://i.imgur.com/v6JS64Y.png"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        b0 = Button(10, 10, Buttons, cena, 0).create()
        #b0.entra(cena)
        cena.vai()


if __name__ == "__main__":
    _ = Project()