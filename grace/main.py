from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
jog = int(input('''\033[;32;mSuas opções:
\033[;36;m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
\033[;32;mQual e a sua jogada? '''))
print('\033[;31;mJO')
sleep(1)
print('\033[;31;mKEN')
sleep(1)
print('\033[;31;mPO!!!\033[m')
print(11*'\033[;35;m-=','\n\033[;32;mComputador jogou {}\nJogador jogou {}'.format(itens[comp], itens[jog]))
print('\033[;35;m-=\033[m'*11)
if comp == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('Jogador Ganhou')
    elif jog == 2:
        print('Computado Ganhou')
    else:
        print('JOGADA INVALIDA')
if comp == 1:
    if jog == 0:
        print('Computador Ganhou')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('Jogador Ganhou')
    else:
        print('JOGADA INVALIDA')
if comp == 2:
    if jog == 0:
        print('Jogador Ganhou')
    elif jog == 1:
        print('Computador Ganhou')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

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

# qualquernome()