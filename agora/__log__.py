
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
{'date': 'Fri Dec 20 2019 12:41:47.377 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 139
    main()
  module <module> line 133
    [print(a.nome, [h.nome for h in a.horarios]) for a in Turma.LISTA]
AttributeError: 'Item' object has no attribute 'nome'
'''},
{'date': 'Sun Dec 22 2019 07:09:16.328 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    t = [Turma(nome, [Horario(choice("stqnx"), choice(HS), sala=choice(SS)) for _ in range(3)]) for nome in TS]
  module <module> line 86
    super().__init__(nome)
  module <module> line 57
    self.adiciona(self)
  module <module> line 60
    self.lista.append(Item)
AttributeError: 'method' object has no attribute 'append'
'''},
{'date': 'Sun Dec 22 2019 07:09:57.975 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 137
    main()
  module <module> line 131
    [print(a.nome, [h.nome for h in a.horarios]) for a in  Turma.LISTA]
AttributeError: 'Item' object has no attribute 'nome'
'''},
{'date': 'Sun Dec 22 2019 07:44:41.945 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''a ['U-q-8-X-I', 'U-s-0-X-F', 'U-t-6-X-K']
b ['U-q-2-X-K', 'U-t-7-X-B', 'U-s-9-X-A']
c ['U-t-7-X-N', 'U-n-6-X-H', 'U-x-0-X-N']
d ['U-x-0-X-B', 'U-t-4-X-C', 'U-t-0-X-L']
e ['U-x-5-X-K', 'U-s-5-X-F', 'U-s-9-X-D']
f ['U-s-2-X-K', 'U-x-3-X-F', 'U-n-4-X-K']
g ['U-s-0-X-L', 'U-q-5-X-L', 'U-n-0-X-M']
h ['U-s-3-X-N', 'U-t-7-X-N', 'U-q-6-X-F']
i ['U-x-5-X-B', 'U-x-1-X-L', 'U-n-8-X-J']
j ['U-x-1-X-K', 'U-n-3-X-B', 'U-x-6-X-J']
k ['U-t-6-X-F', 'U-s-7-X-C', 'U-t-3-X-K']
l ['U-n-1-X-J', 'U-n-5-X-H', 'U-x-1-X-L']
m ['U-x-3-X-F', 'U-t-5-X-H', 'U-s-7-X-M']
n ['U-x-0-X-G', 'U-x-7-X-G', 'U-x-4-X-D']
Adriana b
Ana c
Maria e
Sandra d
Juliana l
Antônio f
Carlos e
Francisco l
João e
José f
Bruna c
Camila c
Jéssica b
Letícia a
Amanda b
Lucas h
Luiz d
Mateus d
Guilherme h
Pedro k
Traceback (most recent call last):
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
  module <module> line 151
    main()
  module <module> line 146
    [print(a.nome, [s.nome for s in a.turmas]) for a in Sala.LISTA]
AttributeError: 'Item' object has no attribute 'nome'
'''},
{'date': 'Sun Dec 22 2019 07:46:50.184 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''a ['U-t-7-X-C', 'U-s-2-X-D', 'U-t-8-X-I']
b ['U-n-5-X-K', 'U-x-8-X-A', 'U-n-9-X-A']
c ['U-t-7-X-L', 'U-n-4-X-J', 'U-q-6-X-N']
d ['U-s-5-X-M', 'U-t-8-X-N', 'U-q-7-X-A']
e ['U-x-4-X-M', 'U-s-8-X-B', 'U-x-5-X-M']
f ['U-n-5-X-A', 'U-s-2-X-E', 'U-q-1-X-F']
g ['U-s-1-X-M', 'U-s-5-X-J', 'U-s-4-X-C']
h ['U-s-2-X-G', 'U-s-0-X-A', 'U-n-4-X-A']
i ['U-t-9-X-I', 'U-n-3-X-B', 'U-n-9-X-C']
j ['U-q-6-X-F', 'U-q-1-X-B', 'U-q-7-X-H']
k ['U-n-2-X-K', 'U-x-8-X-C', 'U-n-2-X-G']
l ['U-s-3-X-K', 'U-x-9-X-E', 'U-t-7-X-G']
m ['U-n-5-X-F', 'U-s-0-X-D', 'U-x-5-X-F']
n ['U-x-6-X-A', 'U-q-0-X-G', 'U-t-8-X-D']
Adriana i
Ana l
Maria d
Sandra m
Juliana j
Antônio h
Carlos a
Francisco d
João b
José g
Bruna j
Camila c
Jéssica l
Letícia l
Amanda a
Lucas b
Luiz h
Mateus c
Guilherme e
Pedro h
Traceback (most recent call last):
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
  module <module> line 151
    main()
  module <module> line 146
    [print(a.nome, [s.nome for s in a.turmas]) for a in Sala.LISTA]
AttributeError: 'Item' object has no attribute 'nome'
'''},
{'date': 'Sun Dec 22 2019 07:53:54.895 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 98
    SEMSALA = Sala(0)   
  module <module> line 84
    [turma.atualiza(self) for turma in turmas]
TypeError: 'NoneType' object is not iterable
'''},
{'date': 'Sun Dec 22 2019 07:54:43.292 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 152
    main()
  module <module> line 141
    t = [Turma(nome, [Horario(choice("stqnx"), choice(HS), sala=choice(s)) for _ in range(3)]) for nome in TS]
NameError: free variable 's' referenced before assignment in enclosing scope
'''},