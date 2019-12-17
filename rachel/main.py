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
CENAINICIO = "https://i.imgur.com/3qdowNm.jpg"
PLAY = "https://i.imgur.com/Jcnz4vj.png"
SAIR = "https://i.imgur.com/PISMKLy.png"
FUNDODIA = "https://i.imgur.com/zRGdYRp.gif"
BILHETE = "https://i.imgur.com/p9SteRs.png"
LOGO = "https://i.imgur.com/JflnamW.png"
BOTAO = "https://i.imgur.com/kTocYiF.png"
SOMA = "https://i.imgur.com/Rpo5MDy.png"
SOMB = "https://i.imgur.com/Hysq98H.png"

#parte inicial
class gameInicio:

    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark = Elemento("",style=dict(width="1345px",height="600px",backgroundColor="black",opacity=0.7),cena=gameInicio)
        self.logotipo = Elemento(LOGO, x=370, y=30,w=650,h=400, cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)
        
    def mostradia(self,ev=0):
        fake = Cena()
        fake.vai = self.elevador
        dia = Cena(FUNDODIA, direita=fake )
        dia.vai()
        self.bil = Elemento(BILHETE, x=200, y=20,w=900,h=600, cena=dia, vai = self.elevador)
        self.boton = Elemento(BOTAO, x=820, y=470,w=70,h=70, cena=dia, vai = self.elevador)
    
    def toca(self, ev=0):
        self.musica.sound.play()
        self.musA.x = -1200
        self.musB.x = 1200
    
    def pause(self, ev=0):
        self.musica.sound.pause()
        self.musA.x = 1200
        self.musB.x = -1200
    
    def elevador(self, ev=0):
        todos = Controlador()
        todos.vai()
        self.musica = Musica(TRACK)
        self.musica.sound.pause()
        self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
        self.musB = Elemento(SOMB, x=-1200, y=500,w=80,h=80, cena=todos, vai=self.pause)
        
# fim da parte inicial     
class Predio(Elemento): #predio
     def __init__(self, imagem, cena):
        super().__init__(imagem, x= 300, y=180, w=700, h=350)
        self.nome = "casa"


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
        

class Cesta(Elemento): #cestas
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
        self.inverte_corda()
    
    def inverte_corda(self):
        aux = self.corda_esquerda_maior.elt.style.opacity
        self.corda_esquerda_maior.elt.style.opacity = self.corda_direita_maior.elt.style.opacity
        self.corda_direita_maior.elt.style.opacity = aux
        
    def atualiza_vai(self):
        for p in self.cesta_base.integrantes:
            p.seta_vai_base()
        for p in self.cesta_topo.integrantes:
            p.seta_vai_topo()
            
    def concluir_jogo(self, evento=None):
        print("dddd")
        self.casa.elt.style.background-image=CEST
        
    def __init__(self):
        controlador = self
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        
        self.corda_telhado = Elemento(CORDA, x=520, y=10,w=270,h=115, cena=cena)
        #Roldana, corda     
        self.corda_esquerda_menor = Elemento(CORDA, x=420, y=90,w=150,h=115, cena=cena)
        self.corda_esquerda_menor.elt.style.transform = "rotate(90deg)"
        
        self.corda_esquerda_maior = Elemento(CORDA, x=312, y=215,w=365,h=115, cena=cena)
        self.corda_esquerda_maior.elt.style.transform = "rotate(90deg)"
        self.opacity_esquerda = self.corda_esquerda_maior.elt.style.opacity = 0
        self.roldana_esquerda = Elemento(ROLDANA, x=320, y=37,w=380,h=180, cena=cena)
        #Roldana, corda e cesta
        self.corda_direita_menor = Elemento(CORDA, x=740, y=115,w=180,h=115, cena=cena)
        self.corda_direita_menor.elt.style.transform = "rotate(90deg)"
        
        self.corda_direita_maior = Elemento(CORDA, x=630, y=245,w=400,h=115, cena=cena)
        self.corda_direita_maior.elt.style.transform = "rotate(90deg)"
        self.opacity_direita = self.corda_direita_maior.elt.style.opacity = 1
        self.roldana_direita = Elemento(ROLDANA, x=605, y=37,w=380,h=190, cena=cena)
                
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
        
        self.sair = Elemento(SAIR, x=1050, y=490,w=140,h=80, cena=cena, vai = self.concluir_jogo)

        cena.vai()


if __name__ == "__main__":
    Controlador()
    gameInicio()