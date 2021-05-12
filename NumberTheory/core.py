import math


__all__ = ['sito', 'fact', 'tot', 'primes', 'nwd', 'primo', 'nTyFibb',
           'mniejszyRownyFibb', 'isPrime', 'nextPrime', 'tableOfPrimes']


def sito(u):
    tab = [0 for i in range(u+1)]
    for i in range(2, u+1):
        tab[i] = i
    for i in range(4, u+1, 2):
        tab[i] = 2
    for i in range(3, math.floor(math.sqrt(u))):
        if tab[i] == i:
            for j in range(i*i, u+1, i):
                if (tab[j] == j):
                    tab[j] = i
    return tab


def fact(x, licz):
    primes = []
    counts = []
    primes.append(licz[x])
    counts.append(1)
    x = x // licz[x]
    while x > 1:
        if licz[x] == primes[-1]:
            counts[-1] += 1
            x = x // licz[x]
        else:
            primes.append(licz[x])
            counts.append(1)
            x = x // licz[x]
    wyn = [primes, counts]
    return wyn


def primes(x, licz):
    primes = []
    while x > 1:
        if licz[x] in primes:
            x = x // licz[x]
        else:
            primes.append(licz[x])
            x = x // licz[x]
    return primes


def tot(x, licz):
    p = primes(x, licz)
    if x == 0:
        return 0
    else:
        wyn = x
        for i in p:
            wyn *= (1-1/i)
        return int(wyn)


def nwd(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


def primo(x):
    licz = sito(x)
    wyn = []
    for i in range(2, x):
        if i == licz[i]:
            wyn.append(i)
    return wyn


def nTyFibb(n):
    """Zwraca n--tą liczbę Fibbonacciego"""
    if n <= 1:
        return 1
    f = 1
    fm1 = 0
    for ii in range(1, n):
        pom = f
        f = fm1+f
        fm1 = pom
    return f


def mniejszyRownyFibb(n):
    """Zwraca NUMER największej liczby Fibbonacciego mniejszej lub równej n"""
    if n <= 1:
        return 0
    numer = 0
    fibb = 1
    fibbm1 = 0
    while fibb <= n:
        pom = fibb
        fibb = fibb+fibbm1
        fibbm1 = pom
        numer += 1
    return numer


def isPrime(n):
    """Szybko sprawdza czy liczba jest pierwsza, algorytm z 
    https://github.com/bzglinicki/python-training/blob/main/Rozwiazania-zadan/1_Podstawy/nextPrime.py
    """
    if n <= 1:
        return False   # Te dwie instrukcje można zapisać łącznie:
    if n <= 3:
        return True  # if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def nextPrime(n):
    """Zwraca najbliższą liczbę pierwszą, większą od n"""
    # Nie wiem jak szybko ona działa, tzn. czy nie da się szybciej
    if (n <= 1):
        return 2

    k = n
    prime = False

    while not prime:
        k += 1
        prime = isPrime(k)

    return k


def tableOfPrimes(n):
    """Zwraca tablicę wypełnioną liczbami pierwszymi <= n"""
    if n <= 1:
        return []
    if n == 2:  # Sprawdzam to po to, że chcę robić skok o 2 zamiast o 1, zwiększam szybkość dwukrotnie
        return [2]
    last = 3
    res = [2]
    while not last > n:
        if isPrime(last):
            res.append(last)
        last += 2
    return res
