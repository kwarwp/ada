# ada.morgan.main.py
from _spy.vitollino.main import Cena, Sala, Elemento, Texto

imagem_agua  = "https://i.imgur.com/1dk9Wlv.jpg"
imagem_terra = "https://i.imgur.com/x1iprjI.jpg"
imagem_fogo  = "https://i.imgur.com/bNAPjf9.jpg"
imagem_ar    = "https://i.imgur.com/KCpS1wS.jpg"

peixe = "https://i.imgur.com/fdz6m5h.jpg" 


cenaAgua = Cena(imagem_agua)
cenaTerra = Cena(imagem_terra)
cenaFogo = Cena(imagem_fogo)
cenaAr = Cena(imagem_ar)

elemento_peixe = Elemento(peixe, tit = "peixe dory", x = 100, y = 110, cena = cenaAgua)

sala4Elementos = Sala(n = cenaAgua, s = cenaTerra, l = cenaFogo, o = cenaAr)

sala4Elementos.norte.vai()
sala4Elementos.sul.vai()
sala4Elementos.leste.vai()
sala4Elementos.oeste.vai()


