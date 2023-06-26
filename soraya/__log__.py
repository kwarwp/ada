
{'date': 'Mon Jun 26 2023 12:58:09.239 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 38
    Remedios()
  module <module> line 32
    self.remedio = Elemento(REMEDIOS, x==100, y=100, w=300, h=400, cena=self.cena)
NameError: name 'x' is not defined
'''},
{'date': 'Mon Jun 26 2023 13:06:44.337 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 33
  self.remedio = Elemento(REMEDIOS, x=100, y=100, w=100, h=300, style=style.format(0, 0) cena=self.cena)
                                                                                          ^
SyntaxError: invalid syntax
'''},