
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