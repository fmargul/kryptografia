from scripts import *
import random

def add_points(P, Q, p, a, b):
  xp, yp = P
  xq, yq = Q
  if xp == xq and yp == yq:
    s = (3 * xp * xq + a) * pow(2 * yp, -1, p)
  else:
    s = (yq - yp) * pow(xq - xp, -1, p)

  xr = (s*s - xp - xq) % p
  yr = (s * (xp - xr) - yp) % p

  is_on_curve(P, p, a, b)

  return xr, yr


def is_on_curve(P, p, a, b):
  x, y = P
  assert (y*y) % p == (pow(x, 3, p) + a*x + b) % p
  

def apply_double_and_add_method(G, k, p, a, b):
  target_point = G

  k_binary = bin(k)[2:]

  for i in range(1, len(k_binary)):
    current_bit = k_binary[i:i+1]

    target_point = add_points(target_point, target_point, p, a, b)

    if current_bit == "1":
      target_point = add_points(target_point, G, p, a, b)
  
  is_on_curve(target_point, p, a, b)

  return target_point


def generate_public_key(a, b, c, G, p):
  p = find_prime_by_probability(p, 5)
  C = apply_double_and_add_method(G, c, p, a, b)
  return C


def generate_shared_key(a, b, c, D, p):
  p = find_prime_by_probability(p, 5)
  cdG = apply_double_and_add_method(D, c, p, a, b)
  return cdG


def test_ECDH():
    p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - pow(2, 0)
    a = 0  # Parametr A w secp256k1
    b = 7  # Parametr B w secp256k1
    G = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424)
    print(f"Prime nubmer: {p}")
    print(f"Curve: y**2 = x**3 + {a}x + {b}")
    print(f"Generator: {G}")

    c = random.getrandbits(int(math.log2(p)))
    d = random.getrandbits(int(math.log2(p)))

    print()
    print(f"Private key (Alice): {c}")
    print(f"Private key (Bob): {d}")
    
    # Wyliczanie wartości publicznego klucza dla alice i boba
    
    C = generate_public_key(a, b, c, G, p)
    D = generate_public_key(a, b, d, G, p)
    print()
    print(f"Public key (Alice): {C}")
    print(f"Public key (Bob): {D}")

    # Obliczenie wspólnego sekretu
    alice_shared_secret = generate_shared_key(a, b, d, C, p)
    bob_shared_secret = generate_shared_key(a, b, c, D, p)

    print()
    print(f"Shared secret (Alice): {alice_shared_secret}")
    print(f"Shared secret (Bob): {bob_shared_secret}")
    
    # Sprawdzenie, czy oba sekrety są równe
    print()
    if alice_shared_secret == bob_shared_secret:
        print("The shared secret is the same for Alice and Bob.")
    else:
        print("Error - the shared secret is not the same.")