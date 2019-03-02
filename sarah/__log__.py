
{'date': 'Sat Mar 02 2019 12:57:56.624 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  class Batalha
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Mar 02 2019 12:59:15.297 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 14
    _ = Batalha()
  module <module> line 9
    cena = Cena(ARENA)
  module _spy.vitollino.main line 780
    self._cria_divs(width)
  module _spy.vitollino.main line 785
    divesq.style.width = width // 3  # 100
TypeError: unsupported operand type(s) for //: 'str' and 'int'
'''},