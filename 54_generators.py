def gen(n):
    for i in range(n):
        yield i


def fib(n):
    for i in range(n):
        yield ((i-1) + (i-2))


g = fib(10)

for i in g:
    print(i)
