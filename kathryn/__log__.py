
{'date': 'Sat May 26 2018 09:34:35.150 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  x=
     ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat May 26 2018 10:04:14.446 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  x=
     ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat May 26 2018 10:25:36.569 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print(1
       ^
SyntaxError: Unbalanced bracket (
'''},
{'date': 'Mon Sep 05 2022 16:31:13.311 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''1
Traceback (most recent call last):
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
  module <module> line 4
    with urllib.urlopen(link) as f:
NameError: name 'urllib' is not defined
'''},
{'date': 'Mon Sep 05 2022 16:31:34.857 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''1
Traceback (most recent call last):
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
  module <module> line 5
    with urllib.urlopen(link) as f:
AttributeError: 'module' object has no attribute 'urlopen'
'''},
{'date': 'Mon Sep 05 2022 16:33:06.720 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''1
Traceback (most recent call last):
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
  module <module> line 5
    with urlopen(link) as f:
AttributeError: 'FileIO' object has no attribute '__exit__'
'''},
{'date': 'Mon Sep 05 2022 17:38:02.522 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''1

Exception: A network error occurred.
  module '$exec_336' line 5
f = urlopen(link)
'''},
{'date': 'Mon Sep 05 2022 17:39:14.913 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''1

Exception: A network error occurred.
  module '$exec_338' line 5
f = urlopen(link)
'''},