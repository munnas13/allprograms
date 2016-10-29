import numpy as np
is_prime = np.ones(100, dtype=bool)
is_prime[:2] = 0
nmax = int(np.sqrt(len(is_prime)))
for i in range(2, nmax):
    is_prime[2*i::i] = False
print(np.nonzero(is_prime))


