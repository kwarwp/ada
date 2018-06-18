from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
jog = int(input('''\033[;32;mSuas opções:
\033[;36;m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
\033[;32;mQual é a sua jogada? '''))
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