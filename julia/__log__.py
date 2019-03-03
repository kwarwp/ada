
{'date': 'Wed Dec 05 2018 18:47:51.238 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print "Estou aqui";
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Wed Dec 05 2018 18:48:12.622 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print (Estou aqui);
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Dec 05 2018 18:48:31.565 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print Estou aqui
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Wed Dec 05 2018 18:48:43.567 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print "Estou aqui"
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Sun Mar 03 2019 09:34:22.609 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: bases[i].$dict is undefined>
'''},
{'date': 'Sun Mar 03 2019 09:34:50.225 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 25
    _ = Project()
  module <module> line 14
    STYLE["width"] = 800
NameError: name 'STYLE' is not defined
'''},
{'date': 'Sun Mar 03 2019 09:52:37.928 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 8
  style = dict(position="relative",left=f"-{index*80}px", width=IMGSIZE, height="IMGSIZE)
                                                                                         ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Sun Mar 03 2019 09:59:43.579 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 28
    _ = Project()
  module <module> line 22
    b0 = Sprite(10, 10, Buttons, 7, cena = cena)
TypeError: __init__() got an unexpected keyword argument 'cena'
'''},
{'date': 'Sun Mar 03 2019 10:00:51.57 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 28
    _ = Project()
  module <module> line 22
    b0 = Sprite(10, 10, Buttons, 7, cena = cena)
TypeError: __init__() got multiple values for argument 'cena'
'''},
{'date': 'Sun Mar 03 2019 10:19:57.315 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 39
    _ = Project()
  module <module> line 33
    b0 = Button(10, 10, Buttons, cena, 0).create()
  module <module> line 23
    Button.BUTTONS = [Button(randint(800), randint(800), self.image, self.cena, index) for index in range(9)]
TypeError: randint missing 1 positional argument: 'b'
'''},
{'date': 'Sun Mar 03 2019 11:08:41.184 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  return -dx * pull, -dy * pull
                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Mar 03 2019 11:11:19.804 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  return -dx * pull, -dy * pull
                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Mar 03 2019 11:47:14.579 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  CODE = Codigo("", style=dict(left=0, top=650)
                                                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Mar 03 2019 11:47:46.305 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 72
    _ = Project()
  module <module> line 66
    b0.CODE.entra(cena)
AttributeError: 'list' object has no attribute 'CODE'
'''},
{'date': 'Sun Mar 03 2019 11:52:21.476 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 73
    _ = Project()
  module <module> line 67
    b0[0].CODE._code.text("https://i.imgur.com/v6JS64Y.png")
TypeError: 'str' object is not callable
'''},
{'date': 'Sun Mar 03 2019 11:53:39.27 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 73
    _ = Project()
  module <module> line 67
    b0[0].CODE._area.text("https://i.imgur.com/v6JS64Y.png")
TypeError: 'str' object is not callable
'''},
{'date': 'Sun Mar 03 2019 11:57:24.658 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 74
    _ = Project()
  module <module> line 66
    b0[0].CODE.entra(cena)
UnboundLocalError: local variable 'b0' referenced before assignment
'''},
{'date': 'Sun Mar 03 2019 12:16:54.330 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 16
    class Button(Sprite):
  module <module> line 18
    SHOW = Codigo("oi", style=dict(left=0, top=560, width=600))
NameError: name 'Codigo' is not defined
'''},