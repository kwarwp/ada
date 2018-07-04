# ada.amanda.main.py
# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 699

TutorialInterativo = "https://i.imgur.com/tfatd8y.png"
Cena_direita = "https://i.imgur.com/yWH5AGZ.png"
Cena_esquerda = "https://i.imgur.com/AegnKJL.png"
comousarelemento = "https://i.imgur.com/amn4taQ.png"

#cretaceo_l = "https://i.imgur.com/O3o9Oqx.jpg"
#cretaceo_s = "https://i.imgur.com/c9lK8Vm.jpg"
#cretaceo_o = "https://i.imgur.com/QFLlccY.jpg"
#cretaceo_n = "https://i.imgur.com/k1LChZw.jpg"
class CenaTutorialInterativo():
  def __init__(self):
    
    self.cena_t = Cena(img = TutorialInterativo)
    
    self.cena_d = Cena(Cena_direita, esquerda=self.cena_t)

    self.cena_e  = Cena(Cena_esquerda, direita=self.cena_t)

    
    #self.cena_t = Cena(img = TutorialInterativo)
    
    self.cena_t.direita = self.cena_d
    self.cena_t.esquerda = self.cena_e
    
    self.cena_t.meio = Cena(vai=self.cena_o)
    self.cena_t.vai()
    
    
#  def vai(self, *_):
#    self.cena_t.vai()
    
    
    
#class CenaCretaceo():
#  def __init__(self):
#    self.cena_n = Cena(img = cretaceo_n)
#    self.cena_o = Cena(cretaceo_o, direita=self.cena_n)
#    self.cena_s  = Cena(cretaceo_s, direita=self.cena_o)
#    self.cena_l  = Cena(cretaceo_l, direita=self.cena_s,
#    esquerda = self.cena_n)
#    self.cena_n.esquerda = self.cena_o
#    self.cena_n.direita = self.cena_l
#    self.cena_o.esquerda = self.cena_s
#    self.cena_s.esquerda = self.cena_l
#    self.cena_s.meio = Cena(vai=self.vai_sul)
    #cena2 = Cena2()
    #self.cena1.direita = cena2

#    self.cena_n.vai()
#  def vai(self, *_):
#    self.cena_o.vai()
#  def vai_sul(self, *_):
#    from anastasia.main import go_anhanguera
#    go_anhanguera()

#def go_cretaceo():
#  cena_cretaceo = CenaCretaceo()
#  cena_cretaceo.vai()

#if __name__ == "__main__":
#	go_cretaceo()
