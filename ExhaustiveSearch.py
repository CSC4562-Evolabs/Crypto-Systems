# +--------------------------------------------+
# |       Created by: Sean R Chappell          |
# |For: CSC4562 - Project 2 - Exhaustive Search|
# |       On: April 24th, 2023                 |
# +--------------------------------------------+

import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def factorize_n(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None

def find_private_key(e, n):
    start_time = time.time()

    p, q = factorize_n(n)
    if not p:
        raise ValueError("Factorization of n failed")
    
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    time_cost = time.time() - start_time
    return d, p, q, time_cost

# Example public key
e = 926933
n = 1185137

d, p, q, time_cost = find_private_key(e, n)
print(f"Private key d: {d}")
print(f"Prime factors p: {p}, q: {q}")
print(f"Time cost: {time_cost:.6f} seconds")
