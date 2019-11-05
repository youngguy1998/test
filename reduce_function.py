from functools import reduce
def prod(a):
    m = reduce(f, a)
    print(m)
def f(x, y):
    return x*y
c = [1,2,3,4]
prod(c)