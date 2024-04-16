from pymep.realParser import parse
from pymep.realParser import eval

class function:
    def __init__(self, input=""):
        self.data = input
    
    def input(self):
        info = input("Nhap ham f(x)= ")
        self.data = info
    
    def __call__(self, input):
        return eval(self.data, input)
    
a = function()
a.input()
print(a(9))