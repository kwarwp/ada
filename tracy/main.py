# ada.tracy.main.py
from _spy.vitollino.main  import Cena,Elemento
from _spy.vitollino.main  import INVENTARIO as inv
CANADA= "https://image.freepik.com/fotos-gratis/porto-vancouver-em-por-do-sol-columbia-britanica-canada_67340-69.jpg"
JUNGKOOK= "https://img1.gratispng.com/20180423/afe/kisspng-jungkook-2017-bts-live-trilogy-episode-iii-the-wi-spring-day-5ade62b93a30b3.5168236115245237052384.jpg"
class vkook():
    canada= Cena(img=CANADA)
    jungkook= Elemento(img=JUNGKOOK)
    jungkook.entra(canada)
    canada.vai()
vkook()