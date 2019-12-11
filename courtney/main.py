# ada.courtney.main.py
# kesha.morgan.main.py
# sarah.roxanne.main.py
__autor__ = "Isabel Hortencia Garnica"
__designer__ = "Marília Campos Galvão"
__version__ = "05.12.2019"
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE, Musica

STYLE ["width"] = 1320
STYLE ["height"] = "600px"
IGR = "https://i.imgur.com/"
CEST, DOG, BASE, CENA, PRED = f"{IGR}qtw6IoO.png", f"{IGR}ek5NQYw.png", f"{IGR}7Wh2Px0.png", f"{IGR}zRGdYRp.gif", f"{IGR}vL9kR9Y.png"
BOY, GIRL = f"{IGR}MXiGMEc.png", f"{IGR}GDK3tcT.png"
CESTF = f"{IGR}am71B72.png"

class Predio(Elemento): #predio que  inicia bom e no fim fica queimado
     def __init__(self, imagem, cena):
        super().__init__(imagem, x= 350, y=180, w=650, h=350)
        self.nome = "casa"

#Lado esquerdo
class Plataforma(Elemento): #retangulo tranparente
    def __init__(self, imagem, cena, x=430, y=0):
        super().__init__(imagem, cena=cena, w=500,h=200, x=x, y=y)
        self.destino = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)


class Personagem(Elemento):
    def __init__(self,  imagem, controlador, destino, cena,tit, x, y, w, h):
        super().__init__(imagem, cena=cena, tit=tit, x=x, y=y, w=w, h=h)
        self.destino = destino
        self.controlador = controlador
        self.vai = self.move
        self.entra(destino)
        
        
    def move(self, evento=None):
        input(self,destino.x)
        self.destino = self.controlador.cesta_topo
        self.destino.entra_na_cesta(self)
        

class Cesta(Elemento): #cesta da esquerda
    def __init__(self, imagem, controlador, destino, cena, x=0, y=10):
        self.nome = "veiculo"
        self.i = 0
        self.controlador = controlador
        self.integrantes = []
        super().__init__(imagem, cena=cena, w= 170, x=x, y=y)
        self.fundo = Elemento(img = imagem,cena=self, x=0, y=0, w=170)
        frente = Elemento(img = CESTF, cena=self, x=15, y=45, w=140, h =56)
        self.destino = destino
        self.outro = self
        self.vai = self.mover
        frente.vai =self.mover
        self.fundo.vai = self.mover
               
    def mover(self, evento=None):
        if self.i > 0:
            self.do_move()
            self.outro.do_move()
            self.inverte_topo_base(self);
        self.i+=1
    
    def do_move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        
    def movimenta(self, destino):
        destino.move(self)
    
    def entra_na_cesta(self, personagem):
        self.integrantes.append(personagem)
        personagem.entra(self.fundo)
        personagem.y=0
        x = 25
        #personagem.x = x
        for p in self.integrantes:
            p.x=x
            x+=20
            
    def inverte_topo_base(self):
        topo = self.controlador.cesta_topo
        base = self.controlador.cesta_base
        self.controlador.cesta_topo = base
        self.controlador.cesta_base = topo
        
class Controlador:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        
        self.base = Plataforma(BASE, y=200, cena=cena)
        self.base_topo = Plataforma(BASE, y=440, cena=cena)
        self.base.destino, self.base_topo.destino = self.base_topo, self.base
        
        self.cesta_esquerda = Cesta(CEST, controlador = self, destino=self.base_topo, cena=self.base, x=1)
        self.cesta_direita = Cesta(CEST, controlador = self, destino= self.base, cena= self.base_topo, x=300)
        self.cesta_esquerda.outro, self.cesta_direita.outro = self.cesta_direita.outro, self.cesta_esquerda.outro
        
        self.cesta_topo, self.cesta_base = self.cesta_esquerda, self.cesta_direita
        
        self.doggie = Personagem(DOG, controlador=self, destino=self.cena, cena=cena, tit = "10kg", x=0, y=0, w=80,h=50)
        self.menina = Personagem(GIRL,controlador=self, destino=self.base, cena=cena, tit = "20kg", x=50, y=120, w=60,h=80)
        self.menino = Personagem(BOY, controlador=self, destino=self.base.destino, cena=cena, tit = "40kg", x=100, y=100, w=60,h=100)

        cena.vai()
        
        
if __name__ == "__main__":
    Controlador()