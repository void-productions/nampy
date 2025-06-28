import numpy as np
from typing import Dict, List, Optional

s_ = np.s_

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
        new_axes = list(self._axes.keys())
        l = [np.s_[:]] * len(self._inner.shape)
        axes_to_remove = []
        for (key, v) in kwargs.items():
            i = self._axes[key]
            l[i] = v 
            if isinstance(i, int):
                axes_to_remove.append(i)
        axes_to_remove.sort(reverse=True)
        for i in axes_to_remove: del new_axes[i]
        return array(self._inner[tuple(l)], new_axes)

    def __repr__(self):
        return repr(self._inner)

a = zeros(dict(x=3, y=2, z=5))
print(a())
print(a(x=1))
print(a(x=1,y=1))
print(a(x=0)(y=1))
print(a(x=0)(y=1)(z=s_[1:3]))
