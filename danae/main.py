from _spy.vitollino.main import Cena, Texto, Elemento, STYLE, Codigo

STYLE['width'] = 1000
STYLE['height'] = "600px"

entrada = "https://media-cdn.tripadvisor.com/media/photo-s/07/94/9a/9a/primeiro-portao-instalado.jpg"
pixacao = "https://interartive.org/wp-content/uploads/pixo1.jpg"
lagodastartarugas = "https://image.slidesharecdn.com/jardimbotnico-rj-121110093756-phpapp02/95/jardim-botnico-rj-27-638.jpg?cb=1352540459"
portao = "https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline"
def qualquernome():

    cena1 = Cena(img = entrada)
    elemento1 = Codigo(img = pixacao, style = dict(left=0, top=95,height= '505px', width= 250,bottom=20,))
    elemento2 = Elemento(img = portao, style = dict(left= 215, top=0,height= '600px', width= 575,bottom=0))
    lago = Cena(img = lagodastartarugas)
    elemento1.entra(cena1)
    elemento2.entra(cena1)
    txtcena1 = Texto(cena1, "O portao esta trancado")
    elemento2.vai = txtcena1.vai
    elemento1.vai=lago.vai
    cena1.vai()

qualquernome()