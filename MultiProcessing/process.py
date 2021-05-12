import os
import multiprocessing as mp
from ctypes import *
__all__ = ['Manager']


class Manager:

    def __init__(self, tab, fun):
        self.name = self
        self.tab = tab
        self.fun = fun
        self.n = n = mp.cpu_count()

    def __call__(self):

        def pom(tab, v, fun):
            wyn = 0
            for a in tab:
                wyn += fun(a)
            with v.get_lock():
                v.value += wyn

        v = mp.Value(c_longlong, 0)
        processes = []
        for c in range(0, n):
            temp = [self.tab[i] for i in range(c, len(self.tab), self.n)]
            p = mp.Process(target=pom, args=(temp, v, self.fun))
            processes.append(p)

        for p in processes:
            p.start()

        for p in processes:
            p.join()
        return v.value
