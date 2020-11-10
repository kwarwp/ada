# ada.roxanne.velha.py
#  -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Velha para ensino de classes Python.

    .. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

    Classes neste módulo:
        - :py:class:`Tabuleiro` Contém uma matriz de casas.
        - :py:class:`Casa`      Local onde se pode colocar um pino.
        - :py:class:`Pino`      Marcador que ocupa uma casa no tabuleiro.

    Changelog
    ---------
         
    .. versionadded::    20.10
        classe Tabuleiro Casa e Pino.

"""


class Tabuleiro():
    """ Contém uma matriz de casas.
    
    :param matriz: Uma tupla com número de colunas e linhas - default (3, 3).
    """   
    def __init__(self, matriz = (3, 3)):
        _col, _lin = matriz
        self.tabuleiro = [[Casa(self, (col, lin)) for col in range(_col)] for lin in range(_lin)]
        
    def joga(self, tipo, casa):
        """ Coloca opino de um tipo em uma casa.

            :param tipo: tipo do pino que será colocado.
            :param casa: Uma tupla com a ordem da coluna e da linha da casa a ocupar.
        """    
        _col, _lin = casa
        _casa = self.tabuleiro[_col][_lin]
        _casa.joga(tipo)
    def __repr__(self):
        return "\n".join([str(lin) for lin in self.tabuleiro])
        # return str([str(lin)+"\n" for lin in self.tabuleiro])
        
    def vencedor(self):
        vence_linha = any(all(casa.pino.tipo for casa in lin) for lin in self.tabuleiro)
        vence_coluna = any(all(casa.pino.tipo for casa in lin) for lin in zip(*self.tabuleiro))
        return vence_linha or vence_coluna
        
        


class Casa():
    """ Local onde se pode colocar um pino.

        :param tabuleiro: a referencia do tabuleiro.
        :param posicao: Uma tupla com a ordem da coluna e da linha.
    """    
    def __init__(self, tabuleiro, posicao):
        self.tabuleiro, self.posicao = tabuleiro, posicao
        self.pino = None
        
    def joga(self, tipo):
        """ Coloca o pino de um tipo nesta casa.

            :param tipo: tipo do pino que será colocado.
        """    
        self.pino = Pino(tipo, self)
    def __repr__(self):
        return str(self.pino)
       


class Pino():
    """ Marcador que ocupa uma casa no tabuleiro.
    
        :param tipo: o modelo ou dono deste pino.
        :param casa: A casa onde ele foi colocado.
    """   
    def __init__(self, tipo, casa=None):
        self.tipo, self.casa = tipo, casa
    def __repr__(self):
        return str(self.tipo)



def main():
    """ Coloca pinos aleatoriamente nas casas.
    
    """
    jogo = Tabuleiro()
    _col, _lin = (3, 3)
    casas = [(col, lin)  for col in range(_col) for lin in range(_lin)]
    from random import shuffle
    shuffle(casas)
    tipo = True
    while casas:
        jogo.joga(tipo, casas.pop())
        tipo = not tipo
    print(jogo)
    print(jogo.vencedor())


from _spy.vpython.main import *

def main():
    """ Coloca pinos aleatoriamente nas casas.
    
    """
    from browser import doc
    
    doc["pydiv"].html = ""
    _gs=Glow("pydiv")
    cena = canvas()
    cena.width = 900
    cena.height = 600
    box(pos=(0, 0, 0), size=(300, 300, 20), texture="https://i.imgur.com/X1mxjn2b.jpg") #"https://i.imgur.com/0ezlRYUb.jpg")
    cylinder(pos=(0, 0, 30), size=(20, 70, 70), axis=(0, 0, 1), texture="https://i.imgur.com/IPcmVFnb.jpg")
    box(pos=(100, 100, 30), size=(60, 60, 60), texture="https://i.imgur.com/d5fWaoab.jpg")
    box(pos=(-100, -100, 30), size=(20, 70, 20), axis=(1, 1, 0), texture="https://i.imgur.com/d5fWaoab.jpg")
    box(pos=(100, 100, 30), size=(70, 20, 20), axis=(1, 1, 0), texture="https://i.imgur.com/d5fWaoab.jpg")


if __name__ == "__main__":
    main()
