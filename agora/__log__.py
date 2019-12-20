
{'date': 'Thu Dec 19 2019 10:34:54.460 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  self.tiles = [html.DIV(Class="tile is-ancestor" Id=f"weekday-{wd}") for wd in "seg ter qua qui sex".split()]
                                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Dec 19 2019 11:50:26.788 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 48
    Application()
  module <module> line 27
    self.calendar()
  module <module> line 42
    [self.calendar <= tile  or tiler(wd, tile) for wd, tile in self.tiles]
  module <module> line 33
    nomes = NOMES[:]
NameError: name 'NOMES' is not defined
'''},
{'date': 'Thu Dec 19 2019 11:52:11.499 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 48
    Application()
  module <module> line 27
    self.calendar()
  module <module> line 42
    [self.calendar <= tile  or tiler(wd, tile) for wd, tile in self.tiles]
  module <module> line 34
    shuffle(nomes)
TypeError: 'str' object does not support item assignment
'''},
{'date': 'Thu Dec 19 2019 11:53:27.646 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 48
    Application()
  module <module> line 27
    self.calendar()
  module <module> line 42
    [self.calendar <= tile  or tiler(wd, tile) for wd, tile in self.tiles]
  module <module> line 33
    nomes = NOMES[:]
NameError: name 'NOMES' is not defined
'''},
{'date': 'Fri Dec 20 2019 12:17:09.944 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 115
  def __init__(self, nome="agora", pessoas=None, turmas=None, salas=None, turmas=None):
                                                                          ^
SyntaxError: duplicate argument 'turmas' in function definition
'''},
{'date': 'Fri Dec 20 2019 12:17:55.975 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 133
    main()
  module <module> line 126
    t = [Turma(nome) for nome in "abcdefgh"]
TypeError: __init__() missing 1 positional argument: horarios
'''},
{'date': 'Fri Dec 20 2019 12:36:36.481 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 138
    main()
  module <module> line 129
    t = [Turma(nome, [Horario(choice("stqnx"), int(choice("0123456789")))]) for nome in "abcdefgh"]
  module <module> line 97
    super().__init__(f"{segmento}-{dia}-{horario}")
  module <module> line 57
    self.adiciona(self)
  module <module> line 60
    self.lista.append(Item)
AttributeError: 'Horario' object has no attribute 'lista'
'''},
{'date': 'Fri Dec 20 2019 12:38:26.856 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''aTraceback (most recent call last):
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
  module <module> line 138
    main()
  module <module> line 132
    [pprint(a.nome, a.horarios) for a in t]
  module pprint line 55
    printer. pprint(object)
  module pprint line 135
    self. _format(object,self. _stream,0,0,{},0)
  module pprint line 163
    write=stream. write
AttributeError: 'list' object has no attribute 'write'
'''},
{'date': 'Fri Dec 20 2019 12:39:46.941 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''aTraceback (most recent call last):
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
  module <module> line 138
    main()
  module <module> line 132
    [pprint(a.nome, [h.nome for h in a.horarios]) for a in t]
  module pprint line 55
    printer. pprint(object)
  module pprint line 135
    self. _format(object,self. _stream,0,0,{},0)
  module pprint line 163
    write=stream. write
AttributeError: 'list' object has no attribute 'write'
'''},
{'date': 'Fri Dec 20 2019 12:40:06.291 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''a ['U-n-4']
b ['U-s-4']
c ['U-s-0']
d ['U-s-4']
e ['U-n-5']
f ['U-q-9']
g ['U-n-6']
h ['U-q-5']
AdrianaTraceback (most recent call last):
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
  module <module> line 138
    main()
  module <module> line 133
    [pprint(a.nome, a.turmas) for a in p]
  module pprint line 55
    printer. pprint(object)
  module pprint line 135
    self. _format(object,self. _stream,0,0,{},0)
  module pprint line 163
    write=stream. write
AttributeError: 'list' object has no attribute 'write'
'''},