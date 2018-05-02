# ada.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto

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
    
teorias()