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

class Char(Elemento):
    def __init__(self, imagem, destino, cena, x=0, y=0):
        super().__init__(imagem, cena=cena,  tit = "10kg", x=x, y=y, w=80, h=50)
        self.destino = destino

class Personagem(Elemento): #dog
    def __init__(self, imagem, destino, cena, x=540, y=150):
        super().__init__(imagem, cena=cena,  tit = "10kg", x=x, y=y, w=80, h=50)
        self.destino = destino
        self.vai = self.move
        list=[self.destino, ]
    def move(self, evento=None):
        #input(isinstance(self.destino,Veiculo))
        self.entra(self.destino)
        self.x=15
        self.y=13
        #self.destino = Cena(IMG = Cena)#cao tá saindo mas some no espaço
        

class Personagem2(Elemento): #Irma no predio
    def __init__(self, imagem, destino, cena, x=620, y=120):
        super().__init__(imagem, cena=cena,  tit = "20kg", x=x, y=y, w=60, h=80)
        self.destino = destino
        self.vai = self.move

    def move(self, evento=None):
        self.entra(self.destino)
        self.x=50
        self.y=0

class Personagem3(Elemento): #garoto no predio
    def __init__(self, imagem, destino, cena, x=710, y=100):
        super().__init__(imagem, tit = "40kg", cena=cena, x=x, y=y, w=60, h=100)
        self.destino = destino
        self.vai = self.move

    def move(self, evento=None):
        self.entra(self.destino)
        self.x=80
        self.y=0


class Veiculo(Elemento): #cesta da esquerda
    def __init__(self, imagem, destino, cena, x=0, y=10):
        self.nome = "veiculo" 
        super().__init__(imagem, cena=cena, w= 170, x=x, y=y)
        self.fundo = Elemento(img = imagem,cena=self, x=0, y=0, w=170)
        frente = Elemento(img = CESTF, cena=self, x=15, y=45, w=140, h =56)
        self.destino = destino
        self.outro = self
        self.vai = self.mover
        frente.vai =self.mover
               
    def mover(self, evento=None):
        self.do_move()
        self.outro.do_move()
    
    def do_move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        
    def movimenta(self, destino):
        destino.move(self)


class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        
        self.base0 = Plataforma(BASE, y=200, cena=cena)
        self.base1 = Plataforma(BASE, y=440, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        
        self.cesta = Veiculo(CEST, destino=self.base1, cena=self.base0)
        self.cesta2 = Veiculo(CEST, destino= self.base0, cena= self.base1, x=300)
        self.cesta.outro, self.cesta2.outro = self.cesta2.outro, self.cesta.outro
        
        self.bicho = Char(DOG, destino=self.cesta.fundo, cena=cena)
        self.doggie = Personagem(DOG, destino=self.cesta.fundo, cena=cena)
        self.menina = Personagem2(GIRL, destino=self.cesta.fundo, cena=cena)
        self.menino = Personagem3(BOY, destino=self.cesta.fundo, cena=cena)

        cena.vai()
        
        
if __name__ == "__main__":
    Basico()
