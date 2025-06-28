import numpy as np
from typing import Dict, List, Optional

def zeros(shape: Dict[str, int]):
    axes = list(shape.keys())
    np_shape = list(shape.values())
    return array(np.zeros(np_shape), axes)

class array:
    def __init__(self, l, axes: List[str]):
        self._inner = np.array(l)
        n = len(self._inner.shape)
        self._axes = dict(zip(axes, range(n)))

    def __call__(self, **kwargs):
        l = [np.s_[:]] * len(self._inner.shape)
        for (key, v) in kwargs.items():
            i = self._axes[key]
            l[i] = v 
        return self._inner[tuple(l)]

    def __repr__(self):
        return repr(self._inner)

a = zeros(dict(x=3, y=2))
print(a())
print(a(x=1))
print(a(x=1,y=1))
