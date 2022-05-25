# ada.morgan.main.py
from _spy.vitollino.main import Cena,Elemento

flor= "https://i.imgur.com/hCXeRVX.jpg"
abelha="https://i.imgur.com/tS7w2FU.jpg"

pegarpoli=Cena(flor)
elementoabelha=Elemento(abelha,tit="mel",cena=pegarpoli)

pegarpoli.vai()


