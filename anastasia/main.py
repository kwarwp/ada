# sarah.roxanne.main.py
#Autor: Isabel Hortencia Garnica
from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE, Musica
from texto.main import Texto
IGR = "https://i.imgur.com/"
SOMA, SOMB, CENAINICIO, PREDIO, PREDIOQ = f"{IGR}Rpo5MDy.png", f"{IGR}Hysq98H.png", f"{IGR}3qdowNm.jpg", f"{IGR}vL9kR9Y.png", f"{IGR}qFTCSE7.png"
DOG, MENINOHAPPY, IRMAHAPPY, PLAY, SAIR = f"{IGR}ZQ9SSMz.png", f"{IGR}LsinOyd.png", f"{IGR}XZJuxnZ.png", f"{IGR}Jcnz4vj.png", f"{IGR}PISMKLy.png"
#FUNDODIA, BILHETE, FOGO, LOGO BOTAO = f"{IGR}am71B72.png"
TRACK = "https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3"

FUNDODIA = "https://i.imgur.com/zRGdYRp.gif"
BILHETE = "https://i.imgur.com/p9SteRs.png"
FOGO= "https://i.imgur.com/v0hHNyO.gif"
FOGUI= "https://i.imgur.com/jcJ0beK.gif"
LOGO = "https://i.imgur.com/JflnamW.png"
BOTAO = "https://i.imgur.com/kTocYiF.png"
STYLE ["width"] = 1320
STYLE ["height"] = "600px"
# Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
#INICIO DO JOGO
class gameInicio:
    # start da classe, é aqui que o jogo se inicia
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark = Elemento("",style=dict(width="1345px",height="600px",backgroundColor="black",opacity=0.7),cena=gameInicio)
        self.logotipo = Elemento(LOGO, x=370, y=30,w=650,h=400, cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)
        
    # método que controla o background, aparece o bilhete
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
        todos = Cena(FUNDODIA)
        todos.vai()
        self.musica = Musica(TRACK)
        self.musica.sound.pause()
        self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
        self.musB = Elemento(SOMB, x=-1200, y=500,w=80,h=80, cena=todos, vai=self.pause)
        
        self.predio = Elemento(PREDIOQ, x=440, y=150,w=450,h=350, tit ="Que maravilha, você salvou as crianças!!!", cena =todos, vai = self.sobe_desce)
        self.foguinho = Elemento(FOGO, x=440, y=450,w=150,h=100, cena=todos, vai=self.sobe_desce)
        self.foguim = Elemento(FOGUI, x=550, y=250,w=50,h=50, cena=todos, vai=self.sobe_desce)        
        self.girl = Elemento(IRMAHAPPY, x=450, y=420,w=240,h=150, cena=todos, vai=self.sobe_desce)
        self.boy = Elemento(MENINOHAPPY, x=600, y=400,w=260,h=160, cena=todos, vai=self.sobe_desce) 
        self.dog = Elemento(DOG, x=600, y=450,w=150,h=100, cena=todos, vai=self.sobe_desce)
 
        
    def sobe_desce(self, *_):#*_ serve para criar estados para poder detrminar quando está dentro, fora, sobe, desce
        pass
        #self._sobe_desce()
        
        
        
gameInicio()