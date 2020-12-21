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
    CENAS = [
    'q308L34', 'v1CVsjO', '7cXtyqA', 'jHnybc0', 'WyiiE0T', 'KZoXpRI',
    'iILubFM', 'regZ51L', 'fUDoUc0', 'CljPeMU', 'bDqM8oP', 'SghQp9q',
    'o8Hj2F4', 'ctDxOKA', 'gWvkAiR', 'SJ428kZ', 'kQWpngJ']
    def __init__(self, j):
        self.setores = [
        ['CO', 'CF', 'CP'],
        ['EE', 'RE', 'SN'],
        ['TE', 'DI', 'CA'],
        ['TO', 'EC', 'EA'],
        ['MM', 'EX', 'RX'],
        ['SE', 'SC', 'SA']]
        self.quadrantes = "OV ON NO NV, OS O N NL, SO S L LN, SV SL LS LV"
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    import re
    print([re.findall(r" ([A-Z]+)",l) for l in Nanite(Jogo).quadrantes.split("\n")])
