# ada.arvore.main.py
ELIPSE = "https://imgur.com/Gea0Z3c.png"
ARVORE = "https://imgur.com/VkBQmuU.jpg"
PECAS = "https://i.imgur.com/PqKHfTW.png"
MUSICA = "https://activufrj.nce.ufrj.br/file/carlo/Synth-pop_2080.mp3?disp=inline"
from _spy.vitollino.main import Cena, STYLE, Elemento, Musica, INVENTARIO as INV
STYLE.update(width=1350, height="650px")
class Arvore:
    '''Arvore onde pode clicar nos nós e colocar o nome do parente '''
    def __init__(self):
        def make_piece(index):
            pc = Elemento(PECAS, x=0, y=0, w=60, h=60, cena=self.cena)
            pc.siz = (180, 180)
            dx, dy = 60*(index//3), 60*(index%3)
            pc.pos = (-dx, -dy)
            INV.bota(pc)
            return pc
            
        self.cena = Cena(ARVORE)
        INV.inicia()
        self.cena.vai()
        self.pecas = [make_piece(index) for index in range(9)]
        #Musica(MUSICA)
        
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