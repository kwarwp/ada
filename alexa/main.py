# ada.alexa.main.py
# from _spy.vpython.main import *
from random import shuffle
class A:
    valor = 1
    def __init__(self, um_valor):
        self.um_valor = um_valor
    def incrementa(self):
        self.um_valor += 1
    def muda(self):
        self.um_valor *= 2
class B(A):
    valor = 1
    def __init__(self, um_valor):
        super().__init__(um_valor)
    def muda(self):
        super().muda()
        self.um_valor *= 3
    
a0 = A(4)
a1 = B(4)
v01 = [A((lambda v: v+valor)(valor)) for valor in [1,2]]+[B(valor) for valor in [1,2]]
print(v01)
# shuffle(v01)
for a in v01:
    a.muda()
    print(a.um_valor)
'''
print(a0, a1, a0 == a1, isinstance(a0, A), a0.um_valor, a1.um_valor)
a1.incrementa()
a0.incrementa()
print(a0, a1, a0 == a1, isinstance(a0, A), a0.um_valor, a1.um_valor)
a1.muda()
a0.muda()
print(a0, a1, a0 == a1, isinstance(a0, A), a0.um_valor, a1.um_valor)
'''