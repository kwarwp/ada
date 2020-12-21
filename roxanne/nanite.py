# ada.roxanne.nanite.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Game Resgate dos Nanites.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.12
        Mapa da região.

"""
class Nanite:
    IMGUR = "ig/{}"
    CENAS = [
    'q308L34', 'v1CVsjO', '7cXtyqA', 'jHnybc0', 'WyiiE0T', 'KZoXpRI',
    'iILubFM', 'regZ51L', 'fUDoUc0', 'CljPeMU', 'bDqM8oP', 'SghQp9q',
    'o8Hj2F4', 'ctDxOKA', 'gWvkAiR', 'SJ428kZ', 'kQWpngJ']
    def __init__(self, j):
        from random import shuffle
        cenas = self.CENAS[:]
        self.setores = [
        ['CO', 'CF', 'CP'],
        ['EE', 'RE', 'SN'],
        ['TE', 'DI', 'CA'],
        ['TO', 'EC', 'EA'],
        ['MM', 'EX', 'RX'],
        ['SE', 'SC', 'SA']]
        self.quadrantes = [
        ['OV', 'ON', 'NO', 'NV'],
        ['OS', 'OM', 'NM', 'NL'],
        ['SO', 'SM', 'LM', 'LN'],
        ['SV', 'SL', 'LS', 'LV']]
        quads = []
        self.mundo = {}
        setores = [s for l in self.setores for s in l]
        quadrantes = [s for l in self.quadrantes for s in l]
        for setor in setores:
            for quadrante in quadrantes:
                shuffle(cenas)
                quad = cenas[:4]
                while quad in quads:
                    shuffle(cenas)
                    quad = cenas[:4]
                quads.append(quad)
                self.mundo.update({setor+quadrante:{
                p_cardeal:self.IMGUR.format(img)for p_cardeal, img in zip("nlso", quad)}})
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    import re
    #print([l.split()  for l in Nanite(Jogo).quadrantes.split(",")])
    print(Nanite(Jogo).mundo)
