# ada.roxanne.nanite.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Game Resgate dos Nanites.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.12
        Mapa da região.

"""
class Puzzle:
    def __init__(self, j, img, cena, w=900,h=400,x=100,y=50,dw=3,dh=3):
        swap = self
        class Brilho(j.a):
            def __init__(self):
                super().__init__("https://i.imgur.com/PfodQmT.gif", x=x, y=y, w=20, h=20, o=0.1, cena=cena)
                self.elt.style.transition= "opacity 1s 1s"
                self.elt.ontransitionend = togg
                self.elt.onclick = game
                self.o = 0
                self.glotim =1
            def blink(self, ev=0):
                self.glotim = 0 if self.glotim else 1
                #self.glow.entra(self.inicio if self.glotim else self.limbo)
                self.glow.entra(self.inicio)
                self.glow.o = 0.4 #self.glotim
            def togg (ev):
                self.glow.o = 0 #self.glotim
            def game (ev):
                Swap(j,"https://i.imgur.com/GtQUoA5.png",inicio, dw=4)
        self.glow = Brilho()

class Swap:
    def __init__(self, j, img, cena, w=900,h=400,x=100,y=50,dw=3,dh=3):
        swap = self
        class Peca(j.a):
            def __init__(self, local, indice):
                self.indice = indice
                pw, ph = w//dw, h//dh
                lx, ly = x+local%dw*pw, y+local//dw*ph
                px, py = indice%dw*pw, indice//dw*ph
                super().__init__(img, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena)
                self.siz = (w, h)
                self.elt.Id = f"_swap_{local}"
                self.pos = (-px, -py)
                self.elt.ondrop = lambda ev: self.drop(ev)
            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                tit = int(src_id.split('_')[-1])
                print(f"indice -> {tit}")
                self.dropped(ev, tit)
                
            def dropped(self, ev, indice):
                print(f"indice, swap -> {indice}", swap.pecas[indice])
                swap.pecas[indice].pra_la(self, self.x, self.y)
                swap.montou(indice, self.indice)
            def pra_la(self, peca, x, y):
                peca.pra_ca(self.x, self.y)
                self.x, self.y = x, y
            def pra_ca(self, x, y):
                self.x, self.y = x, y
            def __repr__(self):
                return str(self.indice)

        from random import shuffle
        pecas = list(range(dw*dh))
        self.correto = " ".join(pecas)
        shuffle(pecas)
        self.pecas = [Peca(local, indice) for local, indice in enumerate(pecas)]
        self.resultado = [str(peca) for peca in self.pecas]
    def montou(self, origem, destino):
        self.resultado[origem], self.resultado[destino] = self.resultado[destino], self.resultado[origem]
        resultado = " ".join(self.resultado)
        print(resultado, correto)
        return resultado == self.correto
        

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
        self.limbo = j.c("")
        self.minilines = [
            [setor+quadrante for setor in setlinha for quadrante in quadlinha]
            for setlinha in self.setores for quadlinha in self.quadrantes][:4]
        #return
        for y, line in enumerate(self.minilines):
            for x, quad in enumerate(line):
                nome_sala, nome_norte, nome_leste = quad, self.minilines[y-1][x], self.minilines[y][x-1]
                self.mapear(nome_sala, nome_norte, nome_leste)
        def togg (ev):
            #Swap(j,"https://imgur.com/vY0Gdei.png",inicio, dw=4)
            #self.glotim = 0 if self.glotim else 1
            self.glow.entra(self.limbo)
            self.glow.o = 0 #self.glotim
        def game (ev):
            Swap(j,"https://i.imgur.com/GtQUoA5.png",inicio, dw=4)
        self.inicio = inicio = self.salas.COOV.norte
        #Swap(j,"https://imgur.com/vY0Gdei.png",inicio, dw=4)
        self.glow = j.a("https://i.imgur.com/PfodQmT.gif",x=400, y=400, w=20, h=20, o=0.1, cena= self.limbo)
        self.glow.elt.style.transition= "opacity 1s 1s"
        #self.glow.elt.style.transitionProperty= "opacity"
        #self.glow.elt.style.transitionDuration= "1s"
        #self.glow.elt.style.transitionDelay= "4s"
        #glow.elt.setAttribute("style", "transition-duration: 1s;")
        #glow.elt.style.update = {
        #"transition-property":  "opacity","transition-duration": "1s","transition-delay": "4s",}
        self.glow.elt.ontransitionend = togg
        self.glow.elt.onclick = game
        #self.glow.o = 0
        self.glow.o = 0
        self.glotim =1
        inicio.vai()
    def mapear(self, sala, norte, leste):
        sala, norte, leste = getattr(self.salas, sala), getattr(self.salas, norte), getattr(self.salas, leste)
        sala.norte.meio = norte.norte
        norte.sul.meio = sala.sul
        sala.leste.meio = leste.leste
        leste.oeste.meio = sala.oeste
    def blink(self, ev=0):
        self.glotim = 0 if self.glotim else 1
        #self.glow.entra(self.inicio if self.glotim else self.limbo)
        self.glow.entra(self.inicio)
        self.glow.o = 0.4 #self.glotim
        
    
if __name__ == "__main__":
    from _spy.vitollino.main import JOGO, STYLE
    from browser.timer import set_interval as sti
    STYLE.update(width=1150, height="600px")
    n = Nanite(JOGO)
    sti(n.blink, "3000")
    #print([l.split()  for l in Nanite(Jogo).quadrantes.split(",")])
    #print(Nanite(JOGO).mundo)
    #print(n.minilines)
