
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