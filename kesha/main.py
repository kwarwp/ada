from _spy.vitollino.main import Sala, Labirinto

imn = "https://upload.wikimedia.org/wikipedia/commons/1/1e/Est%C3%BAdio_-_TV_Cultura_Montenegro.jpg"
iml = "http://mochilaotrips.com/wp-content/uploads/2013/03/IMG_1447.jpg"
ims = "https://upload.wikimedia.org/wikipedia/commons/0/01/Morro_de_Castelo_Branco,_aspectos_1,_Castelo_Branco,_concelho_da_Horta,_ilha_do_Faial,_A%C3%A7ores,_Portugal.JPG"
imo = "http://www.unicos.cc/wp-content/uploads/2014/12/jornalismo-1-951x476.jpg"
        
irl = "http://www.vipcomm.com.br/site/upload/sbHulk_GN_150614026.jpg"
irs = "http://www.boulevardshopping.com.br/novo/wp-content/uploads/2012/02/Mcdonalds.jpg"
iro = "http://imagens.canaltech.com.br/38560.54878-Tirar-fotos.jpg"
irn = "http://7diasverdes.com.br/wp-content/uploads/2013/07/Bicicleta-de-passeio.jpg"


class teste():

    def __init__(self):
        pass
        
    def monta(self):
       NONE = [None] * 4

       sala1 = Sala(imn,iml ,ims,imo,NONE)
       sala2 = Sala(irl,iro, irn, irs,NONE)
       #salas = [sala1,sala2]
        
       labirinto = teste.SETOR = Labirinto([sala1, sala2])
        

if __name__ == "__main__":
    teste().monta()
