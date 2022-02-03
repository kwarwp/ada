
{'date': 'Fri Dec 10 2021 13:29:33.421 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2098' line 27
        self.vai()
'''},
{'date': 'Fri Dec 10 2021 13:29:53.946 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
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
    Gatil(GATIL_MOS).vai()
  module <module> line 28
    c0 = Elemento(img, x=140, y=340, w=200, h=200, cena=self)
NameError: name 'img' is not defined
'''},
{'date': 'Thu Feb 03 2022 18:45:31.150 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 45
    class Sala(SalaVit):
  module <module> line 46
    def __init__(self, n=NADA, l=NADA, s=NADA, o=NADA, nome='', **kwargs):
NameError: name 'NADA' is not defined
'''},