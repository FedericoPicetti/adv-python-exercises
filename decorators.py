"""Useful decorators"""
def logging(F):
    def logegr (*args):
        with open('decoratedlog.txt', 'a') as log:
            log.write(F.__name__ + str(args) + '\n')
        return F(*args)
    return logger

def memoization(F):
"""Accelerate function execution by caching values. Useful for recursive functions."""
    F.memory = dict()
    def wrapper(*args):
        if args not in F.memory:
            F.memory[args] = F(*args)
        return F.memory[args]
    return wrapper

def decorator(F):
    def wrapper(*args):
        print("executing {0}{1}".format(F.__name__,args))
        return F(*args)
    return wrapper


@memoization
def f(a,b):
    print(a,b)

@memoization
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

if __name__=="__main__":
    print(fact(5))
    print(fact(10))

