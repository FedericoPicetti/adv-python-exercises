"""Extending the Polynomial class from 'polynomials' module by using a metaclass. The extension leave the module 'polynomials' untouched.
This extension add to Polynomial methods to calculate possible rational roots, to get the effective roots and to get all the polynomials that factorize 'self'"""

from polynomials import *
from functools import reduce

def proots(self):
    a0 = self.c[-1]
    an = self.c[0]
    # p = list of integer divisors of a0
    p = list(filter(lambda x: a0 % x == 0, range(1, abs(a0)+1)))
    q = list(filter(lambda x: an % x == 0, range(1, abs(an)+1)))
    r = list(set(x//y for x in p for y in q))
    # r = [int(x) for x in r if int(x)-x==0]
    r += [-x for x in r]
    return r
            
def roots(self):
    return list(filter(lambda x: self % Polynomial(1, -x) == 0, self.proots()))
    
def pfactors(self):
    res = list(map(lambda r: Polynomial(1, -r), self.roots()))
    remainder = reduce(Polynomial.__truediv__, [self] + res)
    if not (len(remainder.c) == 1 and remainder.c[0] == 1):
        res += [remainder]
    return res
        
class ExtendedPolynomial(type):
    def __init__(meta, classname, supers, attr):
        meta.proots = proots
        meta.roots = roots
        meta.pfactors = pfactors
        
Polynomial = ExtendedPolynomial('Polynomial', (), dict(Polynomial.__dict__))

if __name__=='__main__':
    import functools
    p = Polynomial(1, 2, -1, -2)

    print('Potential roots for {} are :- {}'.format(p, p.proots()))
    print('Rational roots for {} are :- {}'.format(p, p.roots()))
    print('The factors for {} are:'.format(p))
    for q in p.pfactors():
        print("   · {}".format(q))
    print('Counterprove: {} = '.format(p), end='')
    print(functools.reduce(Polynomial.__mul__, p.pfactors()))

    p = Polynomial(2,-3,1,-2,-8)

    print('Potential roots for {} are :- {}'.format(p, p.proots()))
    print('Rational roots for {} are :- {}'.format(p, p.roots()))
    print('The factors for {} are:'.format(p))
    for q in p.pfactors():
        print("   · {}".format(q))
    print('Counterprove: {} = '.format(p), end='')
    print(functools.reduce(Polynomial.__mul__, p.pfactors()))
