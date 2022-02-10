
{'date': 'Sat May 26 2018 02:56:10.472 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  Cena(OCEANO)vai()
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Feb 09 2022 23:05:03.211 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 21
  r = svg.rect(
                                                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Feb 09 2022 23:05:49.791 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 31
    Retangulos().make_rects(1000, 800)
  module <module> line 10
    self.cache = self.create_script_tag(LIXAO)
AttributeError: 'Retangulos' object has no attribute 'create_script_tag'
'''},