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
ROLDANA = f"{IGR}FvD7tcb.png"
CORDA= f"{IGR}cUf3qAv.png"


class Predio(Elemento): #predio que  inicia bom e no fim fica queimado
     def __init__(self, imagem, cena):
        super().__init__(imagem, x= 300, y=180, w=700, h=350)
        self.nome = "casa"

#Lado esquerdo
class Plataforma(Elemento): #retangulo tranparente
    def __init__(self, imagem, cena, x=390, y=0, h=200, w=570):
        super().__init__(imagem, cena=cena, w=w,h=h, x=x, y=y)
        self.destino = self
        self.fundo = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)
    

class Personagem(Elemento): #dog
    def __init__(self, imagem, controlador, cena, h, x=0, y=0, w=60, tit):
        super().__init__(imagem, cena=cena, tit = tit, x=h*3, y=h/2, w=w, h=h)
        self.h = h
        self.w = w
        self.entra(controlador.base_telhado.fundo)
        self.controlador = controlador 
        self.vai = self.move_topo_cesta
        
    def move_topo_cesta(self, evento=None):
        destino = self.controlador.cesta_topo
        self.entra(destino.fundo)
        self.controlador.cesta_topo.adiciona_personagem(self)
        self.vai = self.move_cesta_topo
        destino.arrumar_cesta()
    
    def move_cesta_topo(self, evento=None):
        destinho = self.controlador.base_telhado
        self.entra(destinho)
        self.controlador.cesta_topo.remove_personagem(self)
        self.vai = self.move_topo_cesta
        self.x= self.h*3
        self.y= 200 - self.h
        
    def move_cesta_base(self, evento=None):
        destino = self.controlador.base_solo
        self.entra(destino)
        self.controlador.cesta_base.remove_personagem(self)
        self.vai = self.move_base_cesta
        self.x= self.h*2 - 50#30 + self.h - self.w
        self.y= 200 - self.h
        print(self.w)
        
                
    def move_base_cesta(self, evento=None):
        destino = self.controlador.cesta_base
        self.entra(destino.fundo)
        self.controlador.cesta_base.adiciona_personagem(self)
        self.vai = self.move_cesta_base
        destino.arrumar_cesta()
    
    def seta_vai_topo(self):
        self.vai = self.move_cesta_topo
    
    def seta_vai_base(self):
        self.vai = self.move_cesta_base
        

class Cesta(Elemento):
    def __init__(self, imagem, destino, cena, x=0, y=10, nome="", controlador):
        super().__init__(imagem, cena=cena, w= 170, x=x, y=y)
        self.nome = nome
        self.integrantes = []
        self.controlador = controlador
        self.fundo = Elemento(img = imagem,cena=self, x=0, y=0, w=170)
        frente = Elemento(img = CESTF, cena=self, x=15, y=45, w=140, h =56)
        self.destino = destino
        self.nome = nome
        frente.vai =self.mover
        
    def mover(self, evento=None):
        self.do_move()
        self.outro.do_move()
        self.controlador.inverte_cesta_topo_base()
    
    def do_move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        
    def movimenta(self, destino):
        destino.move(self)
        
    def adiciona_personagem(self, personagem):
        self.integrantes.append(personagem)
        
    def remove_personagem(self, personagem):
        self.integrantes.remove(personagem)
        
    def arrumar_cesta(self):
        x=25
        for p in self.integrantes:
            p.y=0
            p.x=x
            x+=30
                        
class Controlador:
    def inverte_cesta_topo_base(self):
        aux = self.cesta_topo
        self.cesta_topo = self.cesta_base
        self.cesta_base = aux
        self.atualiza_vai()

    def atualiza_vai(self):
        for p in self.cesta_base.integrantes:
            p.seta_vai_base()
        for p in self.cesta_topo.integrantes:
            p.seta_vai_topo()
            
        
    def __init__(self):
        controlador = self
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        
        self.corda_telhado = Elemento(CORDA, x=520, y=-3,w=270,h=130, cena=cena)
        #Roldana, corda     
        self.corda_esquerda = Elemento(CORDA, x=420, y=90,w=150,h=115, cena=cena)
        self.corda_esquerda.elt.style.transform = "rotate(90deg)"
        self.roldana_esquerda = Elemento(ROLDANA, x=320, y=37,w=380,h=180, cena=cena)
        #Roldana, corda e cesta        
        self.corda_direita = Elemento(CORDA, x=620, y=195,w=410,h=130, cena=cena)
        self.corda_direita.elt.style.transform = "rotate(90deg)"
        self.roldana_direita = Elemento(ROLDANA, x=605, y=37,w=380,h=180, cena=cena)
        
        
        
        self.base0 = Plataforma(BASE, y=200, cena=cena)
        self.base1 = Plataforma(BASE, y=440, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        
        self.base_telhado = Plataforma(BASE, x=400, y=0,cena=cena)
               
        self.cesta_esquerda = Cesta(CEST, destino=self.base0, cena=self.base0, x=0, nome="esquerda", controlador=controlador)
        self.cesta_direita = Cesta(CEST, destino= self.base1, cena=self.base1, x=410, nome="direita", controlador=controlador)
        self.cesta_esquerda.outro, self.cesta_direita.outro = self.cesta_direita, self.cesta_esquerda
        
        self.base_solo = Plataforma(BASE, x=550, y=350, w=260,cena=cena)
        
        self.cesta_topo, self.cesta_base = self.cesta_esquerda, self.cesta_direita
        
        self.doggie = Personagem(DOG, controlador=controlador, cena=cena, tit="10kg", h=50, w=80)
        self.menina = Personagem(GIRL,controlador=controlador, cena=cena, tit="20kg", h=80)
        self.menino = Personagem(BOY, controlador=controlador, cena=cena, tit="40kg", h=100, y=0)

        cena.vai()
        
    
        
if __name__ == "__main__":
    Controlador()