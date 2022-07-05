from moduel_x import a
from moduel_y import c

def b(x):
    print('b running '+x)

def replace():
    a.__code__ = b.__code__

if __name__ == '__main__':
    c('before')
    replace()
    c('after')
    