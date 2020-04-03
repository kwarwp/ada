# ada.mickey.main.py
from browser import doc, html
from _spy.vpython.main import *
from math import sqrt, pi
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.blue #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600

PHI= (1+sqrt(5))/2
PHI2= PHI**2
PHI3= PHI**3
PHI4= PHI**4
GRAUS_30= pi/6.0
EIXO_Z= vec(0,0,1)
EIXO_NE= vec(1,1,0)
EIXO_SE= vec(1,-1,0)
EIXO_SSE= vec(2,-1,1)
EIXO_SSO= vec(2,-1,-1)


class Cenario:
    def __init__(self):
        '''
        scene2 = display(title='Peexis',
            width=150, height=150,
            center= (0,0,0),
            x=0, y=0)
        scene2.x, scene2.y =0,0
        scene2.select()
        scene2.autoscale = 1
        '''
        self.quadro = 0
    def principal(self):
        peixinho=Peixe()


class Peixe():
    def __init__(self):
        "Construtor do ser marinho, definindo um esqueleto(frame) e desenhando"
        self.esqueleto=compound(self.desenha())

    def desenha(self):
        self.tamanho = t = 4.0
        self.cor_do_corpo=color.cyan
        self.cor_cauda = cor_cauda = color.red
        self.corpo = self.desenha_o_corpo(self.cor_do_corpo,l=t)
        self.cauda_superior=self.desenha_o_corpo(cor_cauda,l=t*1/PHI**2,d= (t*1.5/PHI,t*1/PHI4))
        self.cauda_inferior=self.desenha_o_corpo(cor_cauda,l=t*1/PHI**2,d= (t*1.5/PHI,t*-1/PHI4))
        self.cauda_superior.rotate(angle=GRAUS_30, axis=EIXO_Z)
        self.cauda_inferior.rotate(angle=-GRAUS_30, axis=EIXO_Z)
        self.labio_superior= self.desenha_o_labio(eixo= EIXO_NE)
        self.labio_inferior= self.desenha_o_labio(eixo= EIXO_SE)
        self.olho_esquerdo = self.desenha_o_olho(l=t,d=(-t*0.7/PHI,t*1/PHI4,t*1.2/PHI4))
        self.olho_direito = self.desenha_o_olho(l=t,d=(-t*0.7/PHI,t*1/PHI4,-t*1.2/PHI4))
        self.barbatana_dorsal= self.desenha_a_barbatana(l=t,d=(-t*0.1/PHI,t*1/PHI4),eixo= EIXO_NE)
        self.nadadeira_direita= self.desenha_a_nadadeira(l=t,d=(-t*0.2/PHI,-t*0.1/PHI4),eixo= EIXO_SSE)
        self.nadadeira_esquerda= self.desenha_a_nadadeira(l=t,d=(-t*0.2/PHI,-t*0.1/PHI4),eixo= EIXO_SSO)
        return [self.cauda_superior, self.cauda_inferior, self.corpo, 
        self.labio_superior, self.labio_inferior,
        self.olho_esquerdo, self.olho_direito, self.barbatana_dorsal,
        self.nadadeira_direita ,self.nadadeira_esquerda ]

    def desenha_a_barbatana(self,l=1,eixo=(0,0),d=(0,0)):
        return pyramid(
           size=(l,l/PHI,l/PHI4),pos=d,color=self.cor_cauda, axis=eixo
        )

    def desenha_a_nadadeira(self,l=1,eixo=(0,0),d=(0,0)):
        return pyramid(
           size=(l,l/PHI4,l/PHI),pos=d,color=self.cor_cauda, axis=eixo
        )

    def desenha_o_labio(self,eixo):
        t = self.tamanho
        return ring(
            pos=(t*-1.1/PHI-t*0.05,0), axis=eixo,
            radius=t*0.15, thickness=t*0.07,
            size=(t*0.07 ,t*0.3,t*0.3),
            color = self.cor_cauda
        )

    def desenha_o_corpo(self,cor,l=1,d=(0,0)):
        return ellipsoid(
                size=(PHI*l,l,l/PHI),pos=d,color=cor
            )

    def desenha_o_olho(self,l=1,d=(0,0)):
        globo = l/PHI3
        return ellipsoid(
                size=(globo,globo,globo),pos=d,color=color.blue
            )

if __name__ == "__main__":
    cenario= Cenario()
    cenario.principal()
    t = 4.0
