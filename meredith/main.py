# ada.meredith.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 699

cretaceo_l = "https://i.imgur.com/O3o9Oqx.jpg"
cretaceo_s = "https://i.imgur.com/c9lK8Vm.jpg"
cretaceo_o = "https://i.imgur.com/QFLlccY.jpg"
cretaceo_n = "https://i.imgur.com/k1LChZw.jpg"

class CenaTutorialInterativo():
    CENA_TUTORIAL = None
    def __cria(self):
        def _vai_tutorial():
            try:
                cti().vai()
            except:
                from amanda.main import CenaTutorialInterativo as cti
                cti().vai()
        volta_tut = Cena(vai=_vai_tutorial)
        self.cena_t = Cena(cretaceo_l, volta_tut, volta_tut, volta_tut)
        return self
    def vai(self):
        cti = CenaTutorialInterativo.CENA_TUTORIAL
        if cti is None:
            cti =  CenaTutorialInterativo.CENA_TUTORIAL = CenaTutorialInterativo().__cria()
        cti.cena_t.vai()
        return cti

    
if __name__ == "__main__":
    CenaTutorialInterativo().vai()
