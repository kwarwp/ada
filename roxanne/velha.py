# ada.roxanne.velha.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.11
        Descreva o que você adicionou no código.

"""
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


if __name__ == "__main__":
    main()
