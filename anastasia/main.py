# sarah.roxanne.main.py
#Autor: Isabel Hortencia Garnica
from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE, Musica
from texto.main import Texto

#STYLE.update(width=1300, height=500)
TRACK = "https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3"
SOMA = "https://i.imgur.com/Rpo5MDy.png"
SOMB = "https://i.imgur.com/Hysq98H.png"
CENAINICIO = "https://i.imgur.com/3qdowNm.jpg"
PREDIO= "https://i.imgur.com/vL9kR9Y.png"
PREDIOQ = "https://i.imgur.com/qFTCSE7.png"
CESTA = "https://i.imgur.com/qtw6IoO.png"
DOG = "https://i.imgur.com/ZQ9SSMz.png"
MENINOHAPPY = "https://i.imgur.com/LsinOyd.png"
MENINOSAD = "https://i.imgur.com/x3JZ93M.png"
IRMAHAPPY = "https://i.imgur.com/XZJuxnZ.png"
IRMASAD = "https://i.imgur.com/Iv9gWTD.png"
PLAY = "https://i.imgur.com/Jcnz4vj.png"
SAIR = "https://i.imgur.com/PISMKLy.png"
FUNDODIA = "https://i.imgur.com/zRGdYRp.gif"
FUNDONOITE = "https://i.imgur.com/2Vff3L0.png"
FOGOLARGO = "https://i.imgur.com/S1AyGFi.png"
FOGOESTREITO = "https://i.imgur.com/N93X5s1.png"
ROLDANA = "https://i.imgur.com/FvD7tcb.png"
CONFETES = "https://i.imgur.com/SIV1CTm.png"
CORDA="https://i.imgur.com/cUf3qAv.png"
CORDANO= "https://i.imgur.com/qyAtbdK.png"
BILHETE = "https://i.imgur.com/p9SteRs.png"
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
        
        self.predio = Elemento(PREDIOQ, x=350, y=180,w=600,h=300, vai = self.sobe_desce)
        self.girl = Elemento(IRMASAD, x=550, y=80,w=200,h=130, cena=todos, vai=self.sobe_desce)
        self.boy = Elemento(MENINOSAD, x=600, y=60,w=250,h=150, cena=todos, vai=self.sobe_desce)
        
    def sobe_desce(self, *_):#*_ serve para criar estados para poder detrminar quando está dentro, fora, sobe, desce
        pass
        #self._sobe_desce()
        
        
        
gameInicio()