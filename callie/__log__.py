
{'date': 'Wed Apr 13 2022 15:55:07.356 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  GOGHIntru2 = 
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Apr 13 2022 15:55:24.668 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module browser.aio line 1
  <!DOCTYPE html>
  ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Apr 18 2022 14:56:50.57 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 32
    Cubos(CENAS)
  module <module> line 28
    cubos = [Cubo(inx=inx, faces=faces) for inx in range(12)]
NameError: name 'faces' is not defined
'''},