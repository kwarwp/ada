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
    def __init__(j):
        self.quadrantes = """
occipital CO 	frontal CF 	parietal CP
endocrino menor EE 	respiratório RE 	sensorial SN
tegumentar TE 	digestório DI 	cardiovascular CA
torso muscular TO 	endócrino EC 	endócrino maior EA
membro muscular MM 	excretor EX 	reprodutor RX
esquelético menor SE 	esquelético SC 	esquelético maior SA
"""
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    print([[x[-2:] for x in l.split(" 	")] for l in Nanite(j).quadrantes.split()])
