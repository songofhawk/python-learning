from moduel_x import a

def b():
    print('b running')

def replace():
    a.__code__ = b.__code__

if __name__ == '__main__':
    replace()
    a()
    