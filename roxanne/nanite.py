# ada.roxanne.nanite.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Game Resgate dos Nanites.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.12
        Mapa da região.

"""
class Swap:
    def __init__(self, j, img, cena, w=900,h=400,x=100,y=50,dw=3,dh=3):
        swap = self
        class Peca(j.a):
            def __init__(self, local, indice):
                pw, ph = w//dw, h//dh
                lx, ly = x+local%dw*pw, y+local//dw*ph
                px, py = x+indice%dw*pw, y+indice//dw*pw
                super().__init__(img, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena)
                self.siz = (pw, ph)
                self.elt.Id = f"_swap_{indice}"
                self.pos = (-px, -py)
            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                tit = int(src_id.split('_')[-1])
                self.dropped(ev, tit)
                
            def dropped(self, ev, indice):
                swap[indice].pra_la(self, self.x, self.y)
            def pra_la(self, peca, x, y):
                peca.pra_ca(self.x, self.y)
                self.x, self.y = x, y
            def pra_ca(self, x, y):
                self.x, self.y = x, y

        def cria_peca(indice):
            px, py = x+indice%dw, y+indice//dw
            peca = Peca(img, x=px, y=py, w=pw, h=ph, drag=True)
            peca.siz = (w, h)
            peca.elt.Id = "_swap_{indice}"
            peca.pos = (-px, -py)
            return peca
        from random import shuffle
        pecas = list(range(dw*dh))
        nomes = [chr(c) for c  in range(10496,10496+dw*dh)]
        shuffle(pecas)
        #self.dropper = {nome:self.swap for nome in nomes}
        #pw, ph = w//dw, h //dh
        self.pecas = [Peca(local, indice) for local, indice in enumerate(pecas)]
        

class Nanite:
    IMGUR = "https://i.imgur.com/{}.jpg"
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
        self.salas = j.q(**self.mundo)
        self.minilines = [
            [setor+quadrante for setor in setlinha for quadrante in quadlinha]
            for setlinha in self.setores for quadlinha in self.quadrantes][:4]
        #return
        for y, line in enumerate(self.minilines):
            for x, quad in enumerate(line):
                nome_sala, nome_norte, nome_leste = quad, self.minilines[y-1][x], self.minilines[y][x-1]
                self.mapear(nome_sala, nome_norte, nome_leste)
        inicio = self.salas.COOV.norte
        Swap(j,"https://imgur.com/vY0Gdei.png",inicio)
        inicio.vai()
    def mapear(self, sala, norte, leste):
        sala, norte, leste = getattr(self.salas, sala), getattr(self.salas, norte), getattr(self.salas, leste)
        sala.norte.meio = norte.norte
        norte.sul.meio = sala.sul
        sala.leste.meio = leste.leste
        leste.oeste.meio = sala.oeste
    
if __name__ == "__main__":
    from _spy.vitollino.main import JOGO, STYLE
    STYLE.update(width=1150, height="600px")
    n = Nanite(JOGO)
    #print([l.split()  for l in Nanite(Jogo).quadrantes.split(",")])
    #print(Nanite(JOGO).mundo)
    print(n.minilines)
