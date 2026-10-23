from fractions import Fraction
from functools import reduce
from operator import mul


def product(fracs):
    t = reduce(mul, fracs, Fraction(1))
    return t.numerator, t.denominator
