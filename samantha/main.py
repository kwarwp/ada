from _spy.vitollino.main import Cena, Texto, Elemento, STYLE

################################################TAKE1##########################################################

STYLE['width'] = 1200
STYLE['height'] = "100px"

entrada = "https://media-cdn.tripadvisor.com/media/photo-s/07/94/9a/9a/primeiro-portao-instalado.jpg"
pixacao = "https://interartive.org/wp-content/uploads/pixo1.jpg"
lagodastartarugas = "https://image.slidesharecdn.com/jardimbotnico-rj-121110093756-phpapp02/95/jardim-botnico-rj-27-638.jpg?cb=1352540459"
portao = "https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline"
ALPHA = "https://imgur.com/bePU7Xn.jpg"
SPD = "https://imgur.com/jnqSHOh.gif"  # https://i.imgur.com/f0C5HdL.png"
FIR = "https://imgur.com/BJCG0jB.gif"
WAT = "https://imgur.com/IqLSYQ9.gif"
GAS = "https://i.imgur.com/nLM66LY.gif"
SND = "https://imgur.com/EbHrNju.gif"
STR = "https://imgur.com/3LJN7lT.gif"
OBS = "https://i.imgur.com/MsE46fE.png"
GLD = "https://i.imgur.com/hk2OfjS.png"
TUR = "https://i.imgur.com/C1Es3kB.png"
EX0 = "https://i.imgur.com/4PsMLZz.png"
def qualquernome():

    cena1 = Cena(img = entrada)
    elm = Elemento(ALPHA, w=1200, h=800, cena=cena1)
    spd = Elemento(SPD, x=200, y=100, w=200, h=100, cena=cena1)
    fir = Elemento(STR, x=0, y=0, w=1200, h=800, o=0.6, cena=cena1)
    elm.siz = (2400, 2400)
    ex0 = Elemento(EX0, x=300, y=400, w=100, h=240, cena=cena1)
    ex0 = Elemento(EX0, x=400, y=450, w=100, h=240, cena=cena1)
    ex0 = Elemento(EX0, x=500, y=400, w=100, h=240, cena=cena1)
    ex0 = Elemento(EX0, x=600, y=450, w=100, h=240, cena=cena1)
    ex0 = Elemento(EX0, x=700, y=400, w=100, h=240, cena=cena1)
    obs = Elemento(OBS, x=800, y=500, w=100, h=100, cena=cena1)
    tum = Elemento(TUR, x=900, y=550, w=100, h=100, cena=cena1)
    tur = Elemento(TUR, x=900, y=500, w=100, h=100, cena=cena1)
    gol = Elemento(GLD, x=1000, y=550, w=100, h=100, cena=cena1)
    gld = Elemento(GLD, x=1000, y=500, w=100, h=100, cena=cena1)

    '''
    elemento1 = Elemento(img = pixacao, style = dict(left=0, top=95,height= '505px', width= 250,bottom=20,))
    elemento2 = Elemento(img = portao, style = dict(left= 215, top=0,height= '600px', width= 575,bottom=0))
    lago = Cena(img = lagodastartarugas)
    elemento1.entra(cena1)
    elemento2.entra(cena1)
    txtcena1 = Texto(cena1, "O portao esta trancado")
    elemento2.vai = txtcena1.vai
    elemento1.vai=lago.vai'''
    cena1.vai()

qualquernome()