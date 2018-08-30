
{'date': 'Thu Aug 30 2018 14:24:50.247 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 164
  figura = Element(ABELHA, style = dict(top = 100, left = 50, height = 50, width = 50) cena = fundo)
                                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Aug 30 2018 14:25:57.248 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 5
    class Elemento(Element):
  module <module> line 8
    def __init__(self, img="", vai=None, style=NDCT, tit="", alt="",
NameError: name 'NDCT' is not defined
'''},