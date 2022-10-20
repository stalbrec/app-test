import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

l = np.array([1, 2, 3, 4])
print(f'my array: {l}')

sp.init_printing(pretty_print=True)

v = sp.Matrix([0, 1, 2])
sp.pprint(v)

M = sp.Matrix([[1, 2, 3],[3, 2, 1]])
sp.pprint(M)

B = M*v
sp.pprint(B)

np.random.seed(1)
x=np.random.normal(125, 4, 1000)

f,ax=plt.subplots()

ax.hist(x, bins=10, linewidth=0.5, edgecolor='white')
ax.set_xlabel('Enrties')

plt.savefig('normal_distr.pdf')

plt.show()
