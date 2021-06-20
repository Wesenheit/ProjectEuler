import os
import multiprocessing as mp
import resource
import time
from ctypes import *
__all__ = ['Manager']


class Manager:

    def __init__(self, tab, fun):
        self.name = self
        self.tab = tab
        self.fun = fun
        self.n = mp.cpu_count()//2
    
    
    def Mes(self,q):
        start=time.time()
        temp=True
        max_usage = 0
        while temp:
            if not q.empty():
                temp=False
            max_usage = max(
                    max_usage,
                    resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                )
            time.sleep(0.1)
        end=time.time()
        print("Elapsed time: {}, memory usage: {} kb".format(end-start,max_usage))

    def __call__(self,measure=False):

        def pom(tab, v, fun):
            wyn = 0
            for a in tab:
                wyn += fun(a)
            with v.get_lock():
                v.value += wyn

        v = mp.Value(c_longlong, 0)
        processes = []
        for c in range(0, self.n):
            temp = [self.tab[i] for i in range(c, len(self.tab), self.n)]
            p = mp.Process(target=pom, args=(temp, v, self.fun))
            processes.append(p)
        if measure:
            q=mp.Queue()
            monitor=mp.Process(target=self.Mes ,args=(q,))
            monitor.start()
        
        for p in processes:
            p.start()

        for p in processes:
            p.join()

        if measure:
            q.put(False)
            monitor.join()
        return v.value
