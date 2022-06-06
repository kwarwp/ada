# ada.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, JOGO as J

NEWTON = "http://4.bp.blogspot.com/-5gZeG2PCX-0/ViRIc3iUP_I/AAAAAAAACn4/IWvXueCewjU/s1600/fg_3456011-1024x576.jpg"
GALILEU = "https://pbs.twimg.com/profile_images/666413287639269377/-Yw4RtjG_400x400.png"
MACA = "https://macmagazine.com.br/wp-content/uploads/2011/02/24-rainbows.png"
ILUMINATTI = "https://vignette.wikia.nocookie.net/clubpenguin/images/2/2d/Illuminati.png/revision/latest?cb=20150117022611"
GROOT = "https://vignette.wikia.nocookie.net/marvelcomicsfanon/images/9/98/Subject-401_%28Earth-4045%29.png"

def teorias():
    inicio = Cena(img=NEWTON)
    inicio_t = Texto(inicio, "A gravidade da situação está em tornar tudo um material de consumo")
    iluminatti = Texto (inicio, "Ahhh mas disso você já sabia!")
    inicio_e = Elemento (img = MACA, tit="Gravidade", style = dict(left= 70,top=170, width=50, height=200,bottom=100))
    #personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 150, top=100, width=60, height=200))
    lado1 = Cena(img=GALILEU, direita =inicio)
    lado1_e = Elemento(img=ILUMINATTI, tit='O universo não gira em torno de você não,bb', style = dict(left= 150, top=240, width=40, height=200, bottom=100))
    iluminatti = Texto (inicio, "Ahhh mas disso você já sabia!")
    
    inicio_e.entra(inicio)
    inicio_e.vai = inicio_t.vai
    #inicio.vai = inicio_tt.vai
    inicio.esquerda = lado1
    lado1_e.vai = iluminatti.vai
    lado1_e.entra(lado1)
    
    inicio.vai()
    
# teorias()

from _spy.vitollino.jogos import Ator, Fala, A #, Roteiro
from ruzwana.main import Roteiro
IMGUR = "https://i.imgur.com/{}.png"
ELENCO = "z7zIJHV iJqmT9V ehoPNb1 WJ1QdZ9 yqrocJa NShlUFP".split()
SMILE = "https://purepng.com/public/uploads/large/purepng.com-mouth-smilemouth-smilefacial-expressionduchenne-smile-1421526971643lbaoz.png"
yma, maw, wet, xac, ker = "Ymara Guajajara|Maria Wapichana|Weteré ParkatêJê|Celia Xacriabá|Kerexu Yxapyry".split("|")
NOMES = [yma, maw, wet, xac, ker]

class Sorrisos:
    def __init__(self,nomes=NOMES, yy=40, xx=20, dx=100):
        self.cena = cena = Cena(IMGUR.format(ELENCO[0])).vai()
        self.elenco = [Elemento(IMGUR.format(ELENCO[1]), y=yy, x=xx, cena=cena),
                       Elemento(IMGUR.format(ELENCO[3]), y=yy, x=xx+dx*3, w=80, h=240, cena=cena)]
        ymara, wetere = atores = self.elenco
        nome_ator = zip( atores, [nomes[0],nomes[2]])
        ele = [Ator(ymara,nomes[0], 0.6, A.e),
               Ator(wetere,nomes[2], 0.2, A.e)]
        nome_ator = zip( atores, nomes, atores[1:]+[None])
        #rot = [Fala(ato, nom, prox, None) for ato, nom, prox in nome_ator]
        rot = [
               Fala(ymara, "Eu e a Wetere gostamos celebrar nossa cultura. Muitas vezes nos divertimos muito!", wetere, self.ri_ke),
               Fala(wetere, "Mas as vezes as ameaças à nossa cultura é um assunto sério. Se nós duas estamos sérias, estamos preparadas para defender nossa cultura", ymara, self.ri_ym),
               Fala(ymara, "Mas também se nós duas estamos sorrindo é porque gostamos de defender nossa cultura", wetere, self.ri_no),
               Fala(wetere, "As meninas_guerreiras retornam verdadeiro (True) quando vamos defender nossa cultura", ymara, self.foi),
               ]
        #roteiro = J.rt(cena, rot, ele, self.foi)
        roteiro = Roteiro(cena, rot, ele, self.foi)
        self.sm_ym = Elemento(SMILE, x=50, y=-1000+60, w=40, h=30, cena=self.cena)
        self.sm_ke = Elemento(SMILE, x=347, y=-1000+58, w=25, h=18, cena=self.cena, style={'transform': 'rotate(-25deg)'})
    def ri_ke(self, *_):
            yy, yk = self.sm_ym.y, self.sm_ke.y
            yy += 1000 if yy < 0 else 0
            yk -= 1000 if yk > 0 else 0
            self.sm_ym.y = yy
            self.sm_ke.y = yk
    def ri_ym(self, *_):
                yy, yk = self.sm_ym.y, self.sm_ke.y
                self.sm_ym.y -= 1000 if yy > 0 else 0
                self.sm_ke.y += 1000 if yk < 0 else 0
    def ri_no(self, *_):
                    yy, yk = self.sm_ym.y, self.sm_ke.y
                    self.sm_ym.y -= 1000 if yy > 0 else 0
                    self.sm_ke.y -= 1000 if yk > 0 else 0
    def foi(self, *_):
                        yy, yk = self.sm_ym.y, self.sm_ke.y
                        self.sm_ym.y += 1000 if yy < 0 else 0
                        self.sm_ke.y += 1000 if yk < 0 else 0

Sorrisos()
                        #Guerreiras()
