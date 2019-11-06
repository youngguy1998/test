from functools import reduce
def prod(a):
    m = reduce(f, a)
    print(m)
def f(x, y):
    return x*y
c = map(int, input().split(','))
prod(c)
