
{'date': 'Thu Mar 17 2022 19:06:47.317 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 49
    Arvore().make_nodes()
  module <module> line 21
    self.pecas = [make_piece(index) for index in range(9)]
  module <module> line 13
    pc.siz(180, 180)
TypeError: 'list' object is not callable
'''},