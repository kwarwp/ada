# ada.aventura.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Engenho de aventuras textuais.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------

.. versionadded::    22.06

    Leitura dos dados.
"""
__version__ = "22.06"
from browser import alert

class Cenario:
    CENA = {}
    OBJ = {}
    VERBO = {}
    def __init__(self, adv, hero):
        self.hero = hero
        _, cmd = adv[0]
        loc, desc = cmd.split(":")
        Cenario.CENA[loc] = self
        self.verbo = {"OLHA": self.__repr__}
        self.descreve = desc + " ".join(frase.replace(":", " ") for tipo, frase in adv[::-1] if tipo == "D")
        lro = [ix for ix,(kind,cmd) in enumerate(adv) if kind == "O"]
        self.obj = [Objeto(adv[ini:fim],self) for ini,fim in zip(lro, lro[1:]+[len(adv)])]
        self.objeto = {obj.nome[:4]: obj for obj in self.obj}
        # self.roteiro = rot = [cmd.split("=") for cmd in adv.split("\n")]
    def vai(self):
        texto = self.descreve + "\nVocê pode ver:\n" + "\n".join(ob.mostra() for ob in self.objeto.values())
        fala = input(texto).upper().split()
        fala = [termo[:4] for termo in fala]
        self.interpreta(fala+ ["", ""])
        #input(fala)
    def nop(self, fala, obj=""):
        verbo, substantivo = fala[:2]
        input(f"{obj}: Não deu certo essa de '{verbo} {substantivo}'")
    def interpreta(self, fala):
        verbo, substantivo = [termo[:4] for termo in fala[:2]]
        self.objeto[substantivo].vai(fala) if substantivo in self.objeto else self.nop(fala)
    def __repr__(self):
        #return f"@{self.descreve} <{[ob.nome for ob in self.obj]}>"
        return f"@{self.descreve} <{list(self.objeto.keys())}>"
    

class Objeto:
    def __init__(self, adv, cenario):
        _, cmd = adv[0]
        self.cenario = cenario
        self.nome, self.descreve = cmd.split(":") if ":" in cmd else (cmd,"")
        Cenario.OBJ[self.nome] = self
        lro = [ix for ix,(kind,cmd) in enumerate(adv) if kind == "V"]
        #self.verbo = {adv[ini].split(":")[-2]if ":" in adv[ini] else adv[ini][-1]:
        #Verbo(adv[ini:fim], cenario) for ini,fim in zip(lro, lro[1:]+[len(adv)])}
        verbos = [Verbo(adv[ini:fim], cenario).itens()
         for ini,fim in zip(lro, lro[1:]+[len(adv)])]
        self.verbo = {verbo[:4]: obj for verbo, obj in verbos}
    def vai(self, fala):
        verbo, substantivo = [termo[:4] for termo in fala[:2]]
        self.verbo[verbo].vai(self) if verbo in self.verbo else self.cenario.nop(fala, self.nome)
    def mostra(self):
        return f"{self.descreve}>"
    def __repr__(self):
        return f"@{self.descreve} <{list(self.verbo.keys())}>"
    

class Verbo:
    def __init__(self, adv, cenario):
        def nop(*_):
            self.cenario.nop("açao:", self.verbo)
        self.cenario = cenario
        acoes = {act: nop for act in "QWERTYUIOPASDFGHJKLZXCVBNM"}
        
        acoes.update(M=lambda loc: lambda:move(loc), P=lambda loc: lambda:pega(loc))
        _, cmd = adv.pop(0)
        self.verbo, self.descreve = cmd.split(":") if ":" in cmd else (cmd,"")
        self.acao = [acoes[kind](suplement) for kind, suplement in adv[::-1]]
        Cenario.VERBO[loc] = self
    def vai(self, fala):
        verbo, substantivo = self.verbo, self.descreve or fala.descreve
        [action() for action in self.acao]
        #input(f"Pegando: {substantivo}") if verbo == "PEGU" else self.cenario.nop(fala, self.verbo)
        pass
    def move(self, local):
        local.vai()
    def nega(self):
        return self.verbo
    def pega(self, cmd):
        substantivo, descreve = cmd.split(":") if ":" in cmd else (cmd,"")
        input(f"Pegando: {descreve}\nObjeto {substantivo} guardado")# if verbo == "PEGU" else self.cenario.nop(fala, self.verbo)
        
        return self.descreve
    def itens(self):
        return self.verbo, self
    def __repr__(self):
        return self.descreve
    

class Aventura:
    def __init__(self):
        self.inventario = {}
    def main(self, adv):
        self.roteiro = rot = [cmd.split("=") for cmd in adv.split("\n")]
        i = "\n".join( ini for kind, ini in self.roteiro if kind == "I")
        input(i)
        lro = [ix for ix,(kind,cmd) in enumerate(rot) if kind == "L"]
        locais = [Cenario(rot[ini:fim], self) for ini,fim in zip(lro, lro[1:]+[len(rot)])]
        locais.pop().vai()
        #print([lc for lc in locais])
        #print(Cenario.OBJ)
        return

ADV="""I=
I=VENICE GARDEN SOFT APRESENTA:
I=
I= AS AVENTURAS DE CIBELE PARTE 1
I=
I=ESTAS SAO AS AVENTURAS DE UMA
I=GAROTA LEVADA CHAMADA CIBELE.
I=ELA ESTA DOIDA PARA COMER UMA
I=SALADA DE FRUTA COLHIDA DO PE
I=LA NO SITIO DA VOVO.
I=
I=ELA VAI TER QUE SER MUITO VIVA
I=PARA NAO SE MACHUCAR FAZENDO
I=AS SUAS MOLECAGENS..
I=
I=APERTE <ENTER> P/COMECAR
L=COZI:VOCE ESTA NA COZINHA DA VOVO
D=:AQUI VOCE VAI PREPARAR A SALADA
O=GELA:A GELADEIRA
V=ABRA
F=GELA:COMEU UMA SALADA GELADINHA!
B=GELA:VOCE GUARDOU TODAS AS FRUTAS E
N=ABAC:VOCE NAO PEGOU O ABACATE!
N=GOIA:VOCE NAO PEGOU A GOIABA!
N=MAMA:VOCE NAO PEGOU O MAMAO!
V=OLHE:AQUI VOCE VAI GUARDAR A SALADA
O=ENTR:ENTRADA DO SAGUAO
V=VA
M=SAGU
O=SAGU
V=VA
M=SAGU
L=SALA:VOCE ESTA NA SALA DE JANTAR.
D=:COM UMA MESA E MOVEIS DE VIME
O=PAI:SEU PAI USANDO O COMPUTADOR
O=ARCO:UMA PASSAGEM EM ARCOS
V=VA
M=SAGU
O=SAGU
V=VA
M=SAGU
O=PASS
V=VA
M=SAGU
L=SAGU:O SAGUAO DA VOVO E GRANDE, OS
D=:ESCADA AO SEGUNDO ANDAR
D=:ARCOS LEVAM A SALA DE JANTAR E A
O=PASS
V=VA
M=SALA
O=ARCO:UMA PASSAGEM EM ARCOS
V=VA
M=SALA
O=ESCA:ESCADARIA P/CIMA
V=VA
S=ESCA:NAO DA', ANA LUIZA ESTA' DORMINDO!
O=PORT:PORTAS DA FRENTE
V=VA
M=PATI
O=ENTR:ENTRADA DA COZINHA
V=VA
M=COZI
O=COZI
V=VA
M=COZI
L=LOUR:ESTE E O TERRENO DA TIA LOURDES
O=PE:UM ABACATEIRO
O=PORT:UMA PORTEIRA
V=VA
U=ATIL:
U=RANG:
M=PISC
N=ABAC:O RANGER AMEACA TE MORDER!
O=ATIL:ATILA, O MESTICO BRABO
V=OLHE
E=PORT:
A=ATIL:OS DOIS TE CHEIRAM E SOSSEGAM
S=RANG:ATILA ROSNA DESCONFIADO
A=ATIL
V=CHAM
E=PORT:
A=ATIL:OS DOIS TE CHEIRAM E SOSSEGAM
S=RANG:ATILA LATE E BALANCA O RABO
A=ATIL
O=RANG:RANGER, O BOXER RAJADO
V=CHAM
E=PORT:
A=RANG:OS DOIS TE CHEIRAM E SOSSEGAM
S=ATIL:RANGER PULA E TE LAMBE
V=OLHE
E=PORT:
A=RANG:OS DOIS TE CHEIRAM E SOSSEGAM
S=ATIL:RANGER ROSNA DESCONFIADO
N=ABAC:ELE TEM CIUME DO ABACATE
A=RANG
O=ABAC
V=VA
B=ABAC:AI QUE MEDO, SERA QUE CORRO?
V=OLHE
B=ABAC:E', ABACATE DA' MESMO NO PE!
V=PEGU
E=ABAC:E' DO ABACATEIRO DA TIA LOURDES
P=ABAC:ESTE ESTAVA MESMO NO BAIXO!
S=ABAC:NAO VOU LA,TENHO MEDO DOS CAES
V=CORR
F=ABAC:OS CACHORROS CORREM E TE PEGAM
N=PORT:TANTO ERA O MEDO QUE QUASE QUE
A=ABAC:UFA, QUE CARREIRA DANADA!
O=TIA
V=CHAM
U=ABAC:UM ABACATE RECHONCHUDO
B=TIA:ELA DIZ, RANGER!, PASSA FORA!
S=ABAC:DAQUI A POUCO ELA ACORDA
L=MURO:VOCE SE EQUILIBRA NO MURO
O=MAMO:UM MAMOEIRO JUNTO AO MURO
V=OLHE
D=:E TEM UM MAMAO AMARELINHO NELE
D=:PARECE FIRME PARA SE AGARRAR
V=VA
S=MAMO:VOCE TENTA AGARRAR NELE E NADA!
V=AGAR
A=MAMO:VOCE SE ABRACA NO MAMOEIRO
V=SOLT
B=MAMO:CUIDADO QUE CAI NENEM HEIN!
O=MURO:QUE O MURO ESTA DEBAIXO DOS PES
V=OLHE
D=:AGARRAR EM ALGUMA COISA!
D=:ETA MURO ALTO SO! MELHOR EU ME
V=DESC
M=PISC:TREMENDO TODA, VOCE DESCE
N=MAMO:EU TO E' AGARRADA AQUI
O=MAMA
V=PEGU
A=MAMA:VOCE PEGA FIRME NELE
V=TIRE
A=MAMA:VOU TER QUE PUXAR FORTE!
V=PUXE
F=MAMA:NAO AGARROU EM NADA, VIU, CAIU
N=MAMO:SOLTOU! FIU! QUASE QUE
U=MAMA:UM MAMAO AMARELINHO
P=MAMA:UOUOO! ACHO QUE VOU CAIR!
L=PISC:VOCE ESTA NA ORLA DA PISCINA
O=PORT:UMA PORTEIRA
V=VA
M=LOUR
S=PORT:NAO CONSIGO, PARECE TRAVADA
V=OLHE
B=PORT:A PORTEIRA ESTA TRAVADA AGORA
V=DEST
A=PORT:VOCE DESTRAVOU A PORTEIRA
O=RAMP:RAMPA INDO AO PATIO
V=VA
M=PATI
O=ALAM:A ALAMEDA INDO A CASA DO SEU ZE
V=VA
M=ZE
O=MURO:O MURO ALTO DO SITIO
V=VA
B=MURO:AII!, BATER NESTE MURO DOI!
V=SUBA
M=MURO
N=SAND:DE PE DESCALCO, NEM PENSAR!
O=MAM:UM MAMOEIRO JUNTO AO MURO
V=OLHE
B=MAM:TEM UM MAMAO LA EM CIMA!
V=PEGU
A=MAM:TA MAIS ALTO QUE O MURO!
O=PISC:UMA PISCINA CHEIA DE AGUA
L=ZE:VOCE ESTA EM FRENTE DA CASA
D=:DO SEU ZE, O CASEIRO
O=BAMB:UM BAMBU COMPRIDO
V=USE
T=BAMB:USE PARA DERRUBAR GOIABA
V=PEGU
E=SENA
A=BAMB:COM MEDO DE SE ATRAPALHAR
P=BAMB:VOCE PEGA, E LEVA COM CUIDADO
V=LARG
F=BAMB:E VOCE LEVA UM PUXAO DE ORELHA
B=BAMB:ANA LUIZA ACORDA CHORANDO
B=BAMB:E A CACHORRADA TODA LATE!
T=BAMB:O BAMBU CAI COM UM ESTRONDO,
V=ENCO
U=SENA
B=BAMB:E ENCOSTA O BAMBU NUM CANTO
T=BAMB:VOCE VAI COM TODO O CUIDADO,
V=OLHE
A=BAMB:CAPAZ DE ELE SER MAIOR QUE ELA!
A=BAMB:SE VOCE ENCOSTAR ELE NA CASA,
S=BAMB:E' UM BAMBU COMPRIDO E PESADO
O=ALAM:QUE A ALAMEDA VAI DAR NA PISCINA
V=VA
M=PISC
L=RAMP:VOCE ESTA NA RAMPA QUE LEVA DO
D=:PATIO ATE A PISCINA
O=PATI:O PATIO DA VOVO
V=VA
M=PATI
O=ORLA:A ORLA DA PISCINA
V=VA
M=PISC
O=PE:UM PE DE GOIABA
V=OLHE
B=PE:VOCE CONSEGUE ACHAR ALGUMA?
V=PROC
A=PE:OLHA, TEM UM MONTE ESCONDIDAS!
E=PE:UM PE DE GOIABA, CARREGADINHO!
O=GOIA
V=PEGU
B=GOIA
P=GOIA:ESSA AI' VOCE FATUROU!
S=GOIA:EI, GOIABA, SO' LA EM CIMA!
V=OLHE
B=GOIA:JA PROCUROU PRA VER SE TEM?
V=PROC
B=GOIA:TEM UMA GRANDONA LA EM CIMA!
E=PE:UM PE DE GOIABA, CARREGADINHO!
V=TOMB
E=GOIA:UMA BELEZA DE GOIABA
A=GOIA:UMA GOIABONA DESPENCA DO PE'
S=BAMB:SO SE VOCE FOSSE UMA GIRAFA!
V=BATA
B=GOIA:SO BATER NAO ADIANTA, DERRUBE!
V=DERR
B=GOIA:AQUI NA ROCA SE FALA TOMBE!
V=TIRE
B=GOIA:VOCE TEM QUE FAZER ELA CAIR!
L=PATI:NO PATIO HA UMA JAQUEIRA,A CASA
D=:LEVA 'A PISCINA 'A DIREITA
D=:DA VO E BEM EM FRENTE, UMA RAMPA
O=CASA:A CASA DO SITIO DA VOVO
V=VA
M=SAGU
N=SENA:NAO DEU, TO MEIO ATRAPALHADA
O=RAMP:UMA RAMPA LEVANDO A PISCINA
V=VA
M=RAMP
O=JAQU:UMA GRANDE JAQUEIRA
V=OLHE
B=JAQU:ACHO QUE NAO TEM MAIS NADA LA
O=PORT:O PORTAO AZUL
V=VA
M=RUA
L=RUA:VOCE ESTA NA RUA SAPHIRO ARAUJO,
D=A:NO SITIO DA VOVO...
O=SENA
O=PORT:UM PORTAO AZUL
V=VA
M=PATI:
P=SENA:
V=ENTR
M=PATI:
P=SENA:
S=CASE:O PORTAO ESTA TRANCADO
V=OLHE
B=PORT:O PORTAO ESTA ABERTO
S=CASE:O CASEIRO TRANCOU COM CADEADO
V=ABRA
B=PORT:JA ESTA ABERTO, COISINHA!
S=CASE:AS CHAVES NAO ABREM O CADEADO
O=CASE
V=CHAM
A=CASE:SEU ZE, O CASEIRO, ABRE O PORTAO
L=APAR:VOCE ESTA EM SEU APARTAMENTO NA
D=:CIDADE, LOUCA PARA IR AO SITIO
O=TEVE:UM APARELHO DE TEVE
V=DESL
A=TEVE:A TEVE DESLIGA
U=PAI:SEU PAI ABOBALHADO
V=LIGU
B=TEVE:A TEVE LIGA
U=PAI:SEU PAI VENDO TEVE
O=SAND:UMA SANDALIA DE BORRACHA
V=PEGU
P=SAND:VOCE CALCA A SANDALIA
V=LARG
T=SAND:A SANDALIA FICA LARGADA POR AI
O=PAI:SEU PAI VENDO TEVE
V=PECA
M=RUA:SEU PAI LEVA VOCE AO SITIO...
E=CHAV:AS CHAVES DA MAMAE!
P=CHAV:VOCE PEGA AS TAIS CHAVES E
S=TEVE:SEU PAI ESTA LIGADAO NA TEVE...
O=QUAD:UM QUADRO DE AVISO
V=OLHE:TEM ALGO ESCRITO NELE!
V=LEIA
B=QUAD: PECA AO SEU PAI ASS:JOSANE.
B=QUAD: VOLTO JA, SE VOCE QUISER ALGO,
B=QUAD:CIBELE, FUI COMPRAR REVISTINHAS
O=CHAV:UM MOLHO DE CHAVES
V=PEGU
P=CHAV:OK PEGUEI AS CHAVES!
V=OLHE:XI! SAO DA MAMAE!
V=MOSTR
M=APAR:SUA MAE FICOU DE FORA.. VAMOS!
N=PAI:NINGUEM SE INTERESSOU POR ELAS"""

    
    
if __name__ == "__main__":
    Aventura().main(ADV)
    #print(ADV[:100])
