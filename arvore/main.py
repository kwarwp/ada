# ada.arvore.main.py
ELIPSE = "https://imgur.com/Gea0Z3c.png"
ARVORE = "https://imgur.com/VkBQmuU.jpg"
MUSICA = "https://activufrj.nce.ufrj.br/file/carlo/Synth-pop_2080.mp3?disp=inline"
from _spy.vitollino.main import Cena, STYLE, Elemento, Musica
STYLE.update(width=1350, height="650px")
class Arvore:
    '''Arvore onde pode clicar nos nós e colocar o nome do parente '''
    def __init__(self):
        self.cena = Cena(ARVORE)
        self.cena.vai()
        Musica(MUSICA)
        
    def make_nodes(self):
        cena = self.cena
        red, green, siena = 0, -33, -66
        '''Seletor de deslocamento do sprite'''
        class Node(Elemento):
            def __init__(self, x, y, w, c, h=33):
                super().__init__(ELIPSE, x=x, y=y, w=w, h=h, o=0.45, cena=cena, vai=self.nomeia)
                self.siz= (w,100)
                self.pos= (0, c)
                self.text = ""
            def nomeia(self, *_):
                from browser import html
                self.text = input("nomei os parentes aqui")
                self.elt.html = ""
                self.elt <= html.PRE(self.text, style=dict(
                    position='relative', top=0, left=0, backgroundColor='transparent', padding="0.5rem 1.5rem"))
                self.o =1
        [Node(x, y, w, c) for x, y, w, c in [
            [85, 479, 180, siena],[410, 493, 180, siena],[850, 458, 180, siena],
            [410, 55, 170, green],[380, 100, 170, green],[425, 145, 190, green],
            [280, 143, 150, red],[560, 120, 150, red],[560, 180, 150, red]
        ]]
        '''Somente alguns nós estão programados. Outros podem ser acrescentados adicionando os parâmetros na lista acima'''


Arvore().make_nodes()