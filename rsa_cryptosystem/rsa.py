import math
import stdrandom

def keygen(lo, hi):
    primes = _primes(lo, hi)
    p, q = _sample(primes, 2)
    n = p * q
    m = (p - 1) * (q - 1)
    e_list = _primes(2, m)
    for e in e_list:
        if m % e != 0:
            break
    d = 1
    while d < m:
        if (e * d) % m == 1:
            break
        d = d + 1
    return(n, e, d)

def encrypt(x, n, e):
    result = 1
    for i in range(e):
        result = (result * x) % n
    return result

def decrypt(y, n, d):
    result = 1
    for i in range(d):
        result = (result * y) % n
    return result

def _primes(lo, hi):
    primes = []
    p = lo
    for p in range(lo, hi):
        if _is_prime(p):
            primes.append(p)
    return primes

def _sample(a, k):
    b = a[:]
    result = []
    for i in range(k):
        item = stdrandom.choice(b)
        result.append(item)
        b.remove(item)
    return result

def _choice(a):
    return stdrandom.choice(a)

def _is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def bitLength(n):
    return n.bit_length()

def dec2bin(n, width):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    while len(result) < width:
        result = "0" + result
    return result

def bin2dec(n):
    result = 0
    for i in range(len(n)):
        if n[i] == '0' or n[i] == '1':
            result = result * 2 + int(n[i])
    return result


