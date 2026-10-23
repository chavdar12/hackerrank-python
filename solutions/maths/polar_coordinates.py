import cmath


def polar(z):
    r, phi = cmath.polar(complex(z))
    return round(r, 3), round(phi, 3)
