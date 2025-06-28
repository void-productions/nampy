import numpy as np
from typing import List

def zeros(shape, axes: List[str]):
    return array(np.zeros(shape), axes)

class array:
    def __init__(self, l, axes: List[str]):
        self._inner = np.array(l)
        self._axes = axes

    def __call__(self, **kwargs):
        l = [np.s_[:]] * len(self._inner.shape)
        for (key, v) in kwargs.items():
            i = self._axes.index(key)
            l[i] = v 
        return self._inner[tuple(l)]
        

a = zeros((4, 3, 2), ["x", "y", "z"])
print(a())
print(a(x=1))
print(a(x=1,y=1))
