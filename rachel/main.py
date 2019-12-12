# ada.rachel.main.py
#kesha.naomi
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
    def __init__(self, imagem, cena, x=430, y=0, h=200):
        super().__init__(imagem, cena=cena, w=500,h=200, x=x, y=y)
        self.destino = self
        self.fundo = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)
    

class Personagem(Elemento): #dog
    def __init__(self, imagem, controlador, cena, h, x=0, y=0, w=60, tit):
        super().__init__(imagem, cena=cena, tit = tit, x=h*3, y=h/2, w=w, h=h)
        self.entra(controlador.base_telhado.fundo)
        self.controlador = controlador 
        self.vai = self.move_cesta_topo
        
    def move_cesta_topo(self, evento=None):
        destinho = self.controlador.pegar_cesta_topo()
        self.entra(destinho.fundo)
        self.x=15
        self.y=13       


class Cesta(Elemento):
    def __init__(self, imagem, destino, cena, x=0, y=10, nome="", controlador):
        super().__init__(imagem, cena=cena, w= 170, x=x, y=y)
        self.nome = nome 
        self.controlador = controlador
        self.fundo = Elemento(img = imagem,cena=self, x=0, y=0, w=170)
        frente = Elemento(img = CESTF, cena=self, x=15, y=45, w=140, h =56)
        self.destino = destino
        self.nome = nome
        self.vai = self.mover
        frente.vai =self.mover
        #self.fundo.vai = self.mover
        
    def mover(self, evento=None):
        self.do_move()
        self.outro.do_move()
        self.controlador.inverte_cesta_topo_base()
    
    def do_move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        print("move -> "+ self.nome)
        
    def movimenta(self, destino):
        destino.move(self)
        print("movimenta -> "+ self.nome)


class Controlador:
    def pegar_cesta_topo(self):
        print( self.cesta_esquerda.y)
        print( self.cesta_esquerda.x)
        return self.cesta_topo
        
    def inverte_cesta_topo_base(self):
        topo = self.cesta_topo
        base = self.cesta_base
        self.cesta_topo = base
        self.cesta_base = topo
        print

        
    def __init__(self):
        controlador = self
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        
        self.base0 = Plataforma(BASE, y=200, cena=cena)
        self.base1 = Plataforma(BASE, y=440, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        
        self.base_telhado = Plataforma(BASE, x=400, y=0,cena=cena)
        
        self.cesta_esquerda = Cesta(CEST, destino=self.base0, cena=self.base0, x=0, nome="esquerda", controlador=controlador)
        self.cesta_direita = Cesta(CEST, destino= self.base1, cena=self.base1, x=300, nome="direita", controlador=controlador)
        self.cesta_esquerda.outro, self.cesta_direita.outro = self.cesta_direita, self.cesta_esquerda
        
        self.cesta_topo, self.cesta_base = self.cesta_esquerda, self.cesta_direita
        
        self.doggie = Personagem(DOG, controlador=controlador, cena=cena, tit="10kg", h=50, w=80)
        self.menina = Personagem(GIRL,controlador=controlador, cena=cena, tit="20kg", h=80)
        self.menino = Personagem(BOY, controlador=controlador, cena=cena, tit="40kg", h=100, y=0)

        cena.vai()
        
    
        
if __name__ == "__main__":
    Controlador()