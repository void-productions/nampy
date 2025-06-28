#!/usr/bin/python3 -B

import nampy as np

a = np.zeros(dict(x=3, y=2, z=5))
print(a())
print(a(x=1))
print(a(x=1,y=1))
print(a(x=0)(y=1))
print(a(x=0,y=1,z=np.s_[1:3]))
