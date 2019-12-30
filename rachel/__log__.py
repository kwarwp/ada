
{'date': 'Thu Dec 12 2019 10:00:07.572 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 116
    Controlador()
  module <module> line 106
    self.cesta_topo, self.cesta_base = self.cesta_esquerda, self.cesta_direita
AttributeError: 'Controlador' object has no attribute 'cesta_esquerda'
'''},
{'date': 'Thu Dec 12 2019 10:01:35.326 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 116
    Controlador()
  module <module> line 102
    self.cesta_esquerda = Cesta(CEST, controlador = self, destino=self.base_topo, cena=self.base, x=1)
AttributeError: 'Controlador' object has no attribute 'base_topo'
'''},
{'date': 'Thu Dec 12 2019 10:02:05.974 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 117
    Controlador()
  module <module> line 103
    self.cesta_esquerda = Cesta(CEST, controlador = self, destino=self.base_topo, cena=self.base, x=1)
TypeError: __init__() got an unexpected keyword argument 'controlador'
'''},
{'date': 'Thu Dec 12 2019 10:06:28.68 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 113
    self.doggie = Personagem(DOG, controlador=self, destino=self.cesta.fundo, cena=cena)
  module <module> line 36
    senf.entra(controlador.base1)
NameError: name 'senf' is not defined
'''},
{'date': 'Thu Dec 12 2019 10:09:03.426 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 113
    self.doggie = Personagem(DOG, controlador=self, destino=self.cesta.fundo, cena=cena)
  module <module> line 35
    super().__init__(imagem, cena=cena,  tit = "10kg", x=(controlador.casa.h + 1), y=y, w=80, h=50)
AttributeError: 'Predio' object has no attribute 'h'
'''},
{'date': 'Thu Dec 12 2019 10:13:57.394 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 105
    self.base1 = Plataforma(BASE, x=710, y=640, cena=cena, h=10)
TypeError: __init__() got an unexpected keyword argument 'h'
'''},
{'date': 'Thu Dec 12 2019 10:14:52.636 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 114
    self.menina = Personagem2(GIRL, destino=self.cesta.fundo, cena=cena)
  module <module> line 51
    super().__init__(imagem, cena=cena,  tit = "20kg", x=controlador.base1.x, y=y, w=60, h=80)
NameError: name 'controlador' is not defined
'''},
{'date': 'Thu Dec 12 2019 10:16:56.69 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 114
    self.menina = Personagem2(GIRL, destino=self.cesta.fundo, cena=cena)
  module <module> line 51
    super().__init__(imagem, cena=cena,  tit = "20kg", x=controlador.base1.x, y=y, w=60, h=80)
NameError: name 'controlador' is not defined
'''},
{'date': 'Thu Dec 12 2019 10:19:16.991 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 105
    self.base1 = Plataforma(BASE, x=710, y=540, cena=cena, h=10)
TypeError: __init__() got an unexpected keyword argument 'h'
'''},
{'date': 'Thu Dec 12 2019 10:26:37.161 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 123
    Controlador()
  module <module> line 115
    self.doggie = Personagem(DOG, controlador=self, cena=cena, tit="10kg")
TypeError: __init__ missing 1 positional argument: 'destino'
'''},
{'date': 'Thu Dec 12 2019 10:29:30.38 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 123
    Controlador()
  module <module> line 116
    self.menina = Personagem2(GIRL, destino=self.cesta.fundo, cena=cena)
AttributeError: 'Controlador' object has no attribute 'cesta'
'''},
{'date': 'Thu Dec 12 2019 10:43:26.301 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 108
  self.base_telhado = Plataforma(BASE, x=640, y=150, h=400cena=cena)
                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 12 2019 11:03:14.672 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 109
    Controlador()
  module <module> line 94
    self.doggie = Personagem(DOG, controlador=self, cena=cena, tit="10kg", h=50, w=80)
  module <module> line 39
    self.destino = self.controlador.cesta_topo
AttributeError: 'Controlador' object has no attribute 'cesta_topo'
'''},
{'date': 'Thu Dec 12 2019 11:28:02.902 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 114
    Controlador()
  module <module> line 96
    self.cesta_topo,
AttributeError: 'Controlador' object has no attribute 'cesta_topo'
'''},
{'date': 'Thu Dec 12 2019 11:28:29.790 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 96
  self.cesta_top = *-
                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 12 2019 11:28:40.394 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 114
    Controlador()
  module <module> line 99
    self.doggie = Personagem(DOG, controlador=self, destino=self.cesta_topo, cena=cena, tit="10kg", h=50, w=80)
AttributeError: 'Controlador' object has no attribute 'cesta_topo'
'''},
{'date': 'Thu Dec 12 2019 11:35:26.83 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 104
  else
       ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 12 2019 11:38:45.712 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 105
    Controlador()
  module <module> line 93
    self.doggie = Personagem(DOG, controlador=controlador, destino=self.cesta_topo, cena=cena, tit="10kg", h=50, w=80)
AttributeError: 'Controlador' object has no attribute 'cesta_topo'
'''},
{'date': 'Thu Dec 12 2019 12:23:50.989 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 65
  if self.nome <> "":
                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 12 2019 12:24:10.658 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 65
  if self.nome,lenght() > 0:
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 12 2019 14:29:27.923 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 122
    Controlador()
  module <module> line 104
    self.cesta_esquerda = Cesta(CEST, destino=self.base1, cena=self.base0, x=0, nome="esquerda", controlador=controlador)
  module <module> line 56
    self.fundo = Elemento(img = imagem,cena=self, x=0, y=0, w=170)
  module _spy.vitollino.main line 551
    _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
  module _spy.vitollino.main line 475
    cena <= self
  module _spy.vitollino.main line 458
    self.elt <= other.elt
AttributeError: 'Cesta' object has no attribute 'elt'
'''},
{'date': 'Thu Dec 12 2019 14:51:48.221 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 121
    Controlador()
  module <module> line 105
    self.cesta_esquerda.outro, self.cesta_direita.outro = self.cesta_direita.outro, self.cesta_esquerda.outro
AttributeError: 'Cesta' object has no attribute 'outro'
'''},
{'date': 'Thu Dec 12 2019 15:06:54.673 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 118
    Controlador()
  module <module> line 103
    self.cesta_esquerda = Cesta(CEST, destino=self.base1, cena=self.base0, x=0, nome="esquerda", controlador=controlador)
  module <module> line 59
    self.fundo.vai = self.mover
AttributeError: 'Cesta' object has no attribute 'fundo'
'''},
{'date': 'Fri Dec 13 2019 14:38:00.728 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 129
  self.base1 = Plataforma(BASE, y=440,x=10 cena=cena)
                                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 13 2019 16:29:40.215 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 117
  class Controlador:
  ^
IndentationError: expected an indented block
'''},
{'date': 'Fri Dec 13 2019 17:46:42.907 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  def __init__(self, imagem, cena, x=390, y=0, h=200, w=570, h=200):
                                                             ^
SyntaxError: duplicate argument 'h' in function definition
'''},
{'date': 'Fri Dec 13 2019 18:08:01.662 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 150
  self.base_solo = Plataforma(BASE, x=460, y=350,, w=250,cena=cena)
                                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Dec 14 2019 22:58:46.544 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 183
    Controlador()
  module <module> line 150
    self.corda_telhado = Elemento(CORDA, x=520, y=-12,w=270,h=150, cena=todos, vai=self.sobe_desce)
NameError: name 'todos' is not defined
'''},
{'date': 'Sat Dec 14 2019 22:59:21.624 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 183
    Controlador()
  module <module> line 150
    self.corda_telhado = Elemento(CORDA, x=520, y=-12,w=270,h=150, cena=cena, vai=self.sobe_desce)
AttributeError: 'Controlador' object has no attribute 'sobe_desce'
'''},
{'date': 'Sat Dec 14 2019 23:00:05.923 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 183
    Controlador()
  module <module> line 158
    self.corda_direita = Elemento(CORDA, x=660, y=130,w=280,h=180, cena=todos, vai=self.sobe_desce)
NameError: name 'todos' is not defined
'''},
{'date': 'Sun Dec 15 2019 00:00:47.223 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 147
  eh = 
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Dec 15 2019 00:09:18.370 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 181
    Controlador()
  module <module> line 153
    self.corda_direita._maior.elt.style.opacity = 0.5
AttributeError: 'Controlador' object has no attribute 'corda_direita'
'''},
{'date': 'Sun Dec 15 2019 00:50:24.913 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 193
    Controlador()
  module <module> line 157
    self.corda_direita_maior.elt.style.opacity = 0
AttributeError: 'Controlador' object has no attribute 'corda_direita_maior'
'''},
{'date': 'Sun Dec 15 2019 00:55:52.95 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 132
  def inverte_corda(self):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Sun Dec 15 2019 00:57:34.975 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 193
    Controlador()
  module <module> line 157
    self.opacity_esuuerda, self.corda_esquerda_maior.elt.style.opacity = 0
TypeError: 'int' object is not iterable
'''},
{'date': 'Mon Dec 16 2019 23:06:35.40 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 238
    Controlador()
  module <module> line 232
    self.sair = Elemento(SAIR, x=570, y=470,w=180,h=120, cena=cena, vai = self.mostradia)
AttributeError: 'Controlador' object has no attribute 'mostradia'
'''},
{'date': 'Tue Dec 17 2019 12:07:48.828 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 197
  self.predioq2 = Elemento(PREDIOQ, x=440, y=150,w=450,h=350, cena =cena)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Dec 30 2019 08:05:23.189 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 264
    Controlador()
  module <module> line 256
    self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
NameError: name 'todos' is not defined
'''},
{'date': 'Mon Dec 30 2019 08:06:58.944 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 264
    Controlador()
  module <module> line 256
    self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
NameError: name 'todos' is not defined
'''},
{'date': 'Mon Dec 30 2019 08:07:26.268 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 264
    Controlador()
  module <module> line 256
    self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=cena, vai=self.toca)
AttributeError: 'Controlador' object has no attribute 'toca'
'''},
{'date': 'Mon Dec 30 2019 08:09:29.595 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    Controlador()
  module <module> line 262
    self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=cena, vai=self.toca)
AttributeError: 'Controlador' object has no attribute 'toca'
'''},
{'date': 'Mon Dec 30 2019 08:11:11.260 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 180
  def pause(self, ev=0):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Dec 30 2019 08:13:47.329 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 60
  def elevador(self, ev=0):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Dec 30 2019 08:14:01.882 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 60
  def elevador(self, ev=0):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Dec 30 2019 08:14:27.882 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 60
  def elevador(self, ev=0):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Dec 30 2019 14:40:04.62 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    gameInicio()
  module <module> line 43
    self.musA = Elemento(SOMA, x=1200, y=420,w=70,h=70, cena=cena, vai=self.toca)
NameError: name 'cena' is not defined
'''},
{'date': 'Mon Dec 30 2019 14:40:22.768 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    gameInicio()
  module <module> line 43
    self.musA = Elemento(SOMA, x=1200, y=420,w=70,h=70, cena=cena, vai=self.toca)
NameError: name 'cena' is not defined
'''},
{'date': 'Mon Dec 30 2019 14:40:31.723 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    gameInicio()
  module <module> line 43
    self.musA = Elemento(SOMA, x=1200, y=420,w=70,h=70, cena=cena, vai=self.toca)
NameError: name 'cena' is not defined
'''},
{'date': 'Mon Dec 30 2019 14:41:08.287 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 270
    gameInicio()
  module <module> line 43
    self.musA = Elemento(SOMA, x=1200, y=420,w=70,h=70, cena=cena, vai=self.toca)
NameError: name 'cena' is not defined
'''},
{'date': 'Mon Dec 30 2019 14:46:42.261 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 276
    gameInicio()
  module <module> line 42
    self.toca(self)
  module <module> line 55
    self.musA.x = -1200
AttributeError: 'gameInicio' object has no attribute 'musA'
'''},
{'date': 'Mon Dec 30 2019 14:46:54.448 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 276
    gameInicio()
  module <module> line 42
    self.toca(self)
  module <module> line 55
    self.musA.x = -1200
AttributeError: 'gameInicio' object has no attribute 'musA'
'''},
{'date': 'Mon Dec 30 2019 14:47:00.432 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 276
    gameInicio()
  module <module> line 42
    self.toca(self)
  module <module> line 55
    self.musA.x = -1200
AttributeError: 'gameInicio' object has no attribute 'musA'
'''},