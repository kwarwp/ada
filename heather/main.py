# ada.heather.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
from math import sqrt
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.blue #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600
'''
silv = dict(color=color.white, opacity=0.4)
hull = dict(color=color.yellow)
#s = shapes.rectangle(width=10, height=6)
h1=sphere(pos=(1.5, -0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.black)
h2=sphere(pos=(1.5, 0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.black)
#pyramid(pos=(1, -0.5, 0),size=(0.5,0.1,1), axis=(0,1,0), color=color.black)
# --- hull ---
aft=sphere(pos=(2, 0, 0), size=(1,1,2), color=color.yellow)
fr=sphere(pos=(6, 0, 0), size=(1,1,2), color=color.yellow)
body=cylinder(pos=(2, 0, 0), size=(4,1,2) , color=color.yellow)
# --- cockpit ---
caft=sphere(pos=(5, 0.2, 0), size=(1,1,2), **silv)
cfor=sphere(pos=(6.2, 0.2, 0), size=(1,1,2), **silv)
cbody=cylinder(pos=(5, 0.2, 0), size=(1.2,1,2) , **silv)
# --- periscope ---
paft=sphere(pos=(5, 2, 0), size=(0.4,0.4,0.4), **hull)
pfor=sphere(pos=(5.2, 2, 0), size=(0.3,0.5,0.5), **silv)
ptub=cylinder(pos=(5.0, 2, 0), size=(0.2,0.4,0.4), **hull)
pbody=cylinder(pos=(5, 0, 0), axis=(0,1,0), size=(2,0.4,0.4) , **hull)
per = [paft, pfor, ptub, pbody]
# --- portholes ---
phs = [sphere(pos=(x/2+2.2, 0.15, 0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
php = [sphere(pos=(x/2+2.2, 0.15, -0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
pts = [h1, h2, aft, fr, body, caft, cfor, cbody]+per+php+phs
sup = compound(pts, pos=(-1,0,0))

def sail():
    rate(2, sail)
    sup.pos += vec(0.2,0,0)
    sup.rotate(angle=0.02,
           axis=vec(0,1,0))

#sail()
'''

"""
##################
Marujos Pe e Xis
##################
:Author: Carlo E. T. Oliveira
:Contact: carlo no nce
:Date: $Date: 2009/02/14  $
:Status: This is a "work in progress"
:Revision: $Revision: 1.00 $
:Home: `LABASE <http://labase.nce.ufrj.br/>`__
:Copyright: ÂÂ©2009, `GPL <http://is.gd/3Udt>`__
"""
'''
Os marujos Pe e Xis são dois peixes que querem ser grandes empresários e montar  um grande centro de divertimento para criaturas do mar. No momento são apenas peixes comuns e atrapalhados que precisam de muita ajuda para seguir em frente. Eles vão ser desafiados pelas mais simples circunstâncias de seu ambiente natural a cada passo do seu caminho. A obtenção de suas metas vai ser um grande aprendizado para todos nós.
'''
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
EIXO_Z= (0,0,1)
EIXO_NE= (1,1,0)
EIXO_SE= (1,-1,0)
EIXO_SSE= (2,-1,1)
EIXO_SSO= (2,-1,-1)


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
        self.tamanho = t = 4
        self.cor_do_corpo=color.cyan
        self.cor_cauda = cor_cauda = color.red
        self.corpo = self.desenha_o_corpo(self.cor_do_corpo,l=t)
        self.cauda_superior=self.desenha_o_corpo(cor_cauda,l=t*1/PHI**2,d= (t*1.5/PHI,t*1/PHI4))
        self.cauda_inferior=self.desenha_o_corpo(cor_cauda,l=t*1/PHI**2,d= (t*1.5/PHI,t*-1/PHI4))
        return [self.corpo, self.cauda_superior, self.cauda_inferior]
        self.cauda_superior.rotate(angle=GRAUS_30, axis=EIXO_Z)
        self.cauda_inferior.rotate(angle=-GRAUS_30, axis=EIXO_Z)
        self.labio_superior= self.desenha_o_labio(eixo= EIXO_NE)
        self.labio_inferior= self.desenha_o_labio(eixo= EIXO_SE)
        self.olho_esquerdo = self.desenha_o_olho(l=t,d=(-t*0.7/PHI,t*1/PHI4,t*1.2/PHI4))
        self.olho_direito = self.desenha_o_olho(l=t,d=(-t*0.7/PHI,t*1/PHI4,-t*1.2/PHI4))
        self.barbatana_dorsal= self.desenha_a_barbatana(l=t,d=(-t*0.1/PHI,t*1/PHI4),eixo= EIXO_NE)
        self.nadadeira_direita= self.desenha_a_nadadeira(l=t,d=(-t*0.2/PHI,-t*0.1/PHI4),eixo= EIXO_SSE)
        self.nadadeira_esquerda= self.desenha_a_nadadeira(l=t,d=(-t*0.2/PHI,-t*0.1/PHI4),eixo= EIXO_SSO)

    def desenha_a_barbatana(self,l=1,eixo=(0,0),d=(0,0)):
        return pyramid(
           frame=self.esqueleto,size=(l,l/PHI,l/PHI4),pos=d,color=self.cor_cauda, axis=eixo
        )

    def desenha_a_nadadeira(self,l=1,eixo=(0,0),d=(0,0)):
        return pyramid(
           frame=self.esqueleto,size=(l,l/PHI4,l/PHI),pos=d,color=self.cor_cauda, axis=eixo
        )

    def desenha_o_labio(self,eixo):
        t = self.tamanho
        return ring(
            frame=self.esqueleto,pos=(t*-1.1/PHI,0), axis=eixo,
            radius=t*0.15, thickness=t*0.07,color = self.cor_cauda
        )

    def desenha_o_corpo(self,cor,l=1,d=(0,0)):
        return ellipsoid(
                size=(PHI*l,l,l/PHI),pos=d,color=cor
            )

    def desenha_o_olho(self,l=1,d=(0,0)):
        globo = l/PHI3
        return ellipsoid(
                frame=self.esqueleto,size=(globo,globo,globo),pos=d,color=color.blue
            )

if __name__ == "__main__":
    cenario= Cenario()
    cenario.principal()
