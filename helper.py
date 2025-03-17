# helper.py
a = 'apple'
b = 'orange'

def test1():
  print('test1 called')
def test2():
  print('test2 called')
  
def helper_function():
  print('helper function has been called')

# print('test test test')

# __all__ = ['a', 'test1', 'helper_function']  #This means that only the specified variables/functions are available when we import helper.py

if __name__ == '__main__':
  print('test test test')
