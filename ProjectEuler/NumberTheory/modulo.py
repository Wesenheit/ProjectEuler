import math

__all__ = ['leg_sym', 'modular_sqrt', 'inverse', 'ext_euc', 'chin']


def leg_sym(a, p):
    ls = pow(a, (p - 1) // 2, p)
    if ls == p-1:
        return -1
    else:
        return ls


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def inverse(a, n):
    t = 0
    nt = 1
    r = n
    nr = a
    while nr != 0:
        q = r//nr
        r, nr = [nr, r - q * nr]
        t, nt = [nt, t - q * nt]
    if r > 1:
        return 0
    if t < 0:
        t = t+n
    return t


def ext_euc(a, b):
    ol_r, r = [a, b]
    ol_s, s = [1, 0]
    while r != 0:
        q = ol_r // r
        ol_r, r = [r, ol_r - q * r]
        ol_s, s = [s, ol_s - q * s]
    if b != 0:
        bez_t = (ol_r - ol_s * a) // b
    else:
        bez_t = 0
    return [ol_r, ol_s, bez_t]


def chin(M, ytab, ntab):
    tab = []
    for i in ntab:
        Mi = M // i
        gi = ext_euc(i, Mi)[2]
        tab.append(Mi * gi)
    wyn = 0
    for i in range(0, len(ytab)):
        wyn += tab[i]*ytab[i]
    return wyn % M
