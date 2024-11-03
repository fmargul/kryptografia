from scripts import *

class PublicKey:
  def __init__(self, e, n):
    self.e = e
    self.n = n
  
class PrivateKey:
  def __init__(self, d, p, q):
    self.d = d
    self.p = p
    self.q = q

def ext_euclidean(a, b):
  if b == 0:
    return a, 1, 0
  else:
    gcd, x1, y1 = ext_euclidean(b, a%b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def rsa_get_private_key_primes(bits):
  confirmed_primes = []
  while True and len(confirmed_primes)<2:
    potential_prime = random.getrandbits(bits)
    if is_prime_by_probability(potential_prime,50):
      confirmed_primes.append(potential_prime)
  
  return confirmed_primes[0], confirmed_primes[1]

def rsa_get_private_exponent(e, euler_n):         # d = e^-1 mod phi(n)
  gcd, x, y = ext_euclidean(e, euler_n)
  if gcd != 1:
    print("Exponent e is not coprime with totient(n)")
    return -1
  else:
    return x % euler_n



# TEST

p, q = rsa_get_private_key_primes(32)
print(p, q)
n = p*q
print(n)
euler_n = (p-1)*(q-1)
print(euler_n)
e = 65537
d = rsa_get_private_exponent(e, euler_n)
print(e, d)

test_public = PublicKey(e,n)
test_private = PrivateKey(d,p,q)

message = 420
encrypted = pow(message,test_public.e, test_public.n)
print(encrypted)
decrypted = pow(encrypted,test_private.d,(test_private.p*test_private.q))
print(decrypted)

