# ada.morgan.main.py
from _spy.vitollino.main import Cena, Sala, Elemento

imagem_agua  = "https://i.imgur.com/1dk9Wlv.jpg"
imagem_terra = "https://i.imgur.com/x1iprjI.jpg"
imagem_fogo  = "https://i.imgur.com/bNAPjf9.jpg"
imagem_ar    = "https://i.imgur.com/KCpS1wS.jpg"

peixe      = "https://i.imgur.com/fdz6m5h.jpg"
formiga    = "https://i.imgur.com/GEuDeN2.jpg"
batataDoce = "https://i.imgur.com/EQ2CMdS.jpg"
passaro    = "https://i.imgur.com/6NAtUxA.jpg"

cenaAgua = Cena(imagem_agua)
cenaTerra = Cena(imagem_terra)
cenaFogo = Cena(imagem_fogo)
cenaAr = Cena(imagem_ar)

elemento_peixe = Elemento(peixe, tit = "peixe dory", x = 100, y = 110, cena = cenaAgua)
elemento_formiga = Elemento(formiga, tit = "formiga trabalhando", x = 100, y = 110, cena = cenaTerra)
elemento_batataDoce = Elemento(batataDoce, tit = "batata doce na fogueira é bom", x = 100, y = 110, cena = cenaFogo)
elemento_passaro = Elemento(passaro, tit = "passaro bonito", x = 100, y = 110, cena = cenaAr)

sala4Elementos = Sala(n = cenaAgua, s = cenaTerra, l = cenaFogo, o = cenaAr)

sala4Elementos.norte.vai()
sala4Elementos.sul.vai()
sala4Elementos.leste.vai()
sala4Elementos.oeste.vai()


