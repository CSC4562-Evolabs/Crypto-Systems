# +--------------------------------------------+
# |       Created by: Sean R Chappell          |
# |For: CSC4562 - Project 2 - Exhaustive Search|
# |       On: April 24th, 2023                 |
# +--------------------------------------------+

import time

# Define a function to find the Greatest Common Divisor (GCD) 
# of two numbers using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Define a function to find the Extended GCD of two numbers
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# Define a function to find the modular inverse of two 
# numbers e and phi
def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Define a function to factorize a number n into its two 
# prime factors
def factorize_n(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None

# Define a function to find the private key (d) from the 
# public key (e, n)
def find_private_key(e, n):
    start_time = time.time()

    p, q = factorize_n(n)
    if not p:
        raise ValueError("Factorization of n failed")
    
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    time_cost = time.time() - start_time
    return d, p, q, time_cost

e = 926933
n = 1185137

# Find the private key (d) and prime factors (p, q) for 
# the given public key (e, n)
d, p, q, time_cost = find_private_key(e, n)
print(f"Private key d: {d}")
print(f"Prime factors p: {p}, q: {q}")
print(f"Time cost: {time_cost:.6f} seconds")
