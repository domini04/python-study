# helper.py
a = 'apple'
b = 'orange'

def test1():
  print('test1 called')
def test2():
  print('test2 called')
  

__all__ = ['a', 'test1']  #This means that only a and test1 are available when we import helper.py