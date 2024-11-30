import random

def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def is_prime_by_probability(n, accuracy):
  if (n <= 1): return False
  if n == 2 or n == 3: return True
  if (n % 2 == 0): return False

  s = 0
  d = n - 1
  while d % 2 == 0:
    d //= 2
    s += 1

  for _ in range(accuracy):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
      continue

    for _ in range(s - 1):
      x = pow(x, 2, n)        # tutaj zmienione w potędze 'x' zamiast 'a'
      if x == n - 1:
        break
    else:                     # else tutaj powinien być do fora (nie wiedziałem że tak można) zamiast do ifa
      return False
  return True

def find_prime_by_probability(n, accuracy):
  if (is_prime_by_probability(n, accuracy)): return int(n)
  else:
    next_number = n + 1
    while not is_prime_by_probability(next_number, accuracy):
      next_number += 1
    return int(next_number)
  
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

def generate_ecdh_public(curve):
    if curve == "NIST256p":
        p = int('0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff', 16)
        a = int('0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc', 16)
        b = int('0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b', 16)
        gx = int('0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296', 16)
        gy = int('0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5', 16)
        n = int('0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551', 16)
    elif curve == "NIST384p":
        p = int('0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff', 16)
        a = int('0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc', 16)
        b = int('0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef', 16)
        gx = int('0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab7', 16)
        gy = int('0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f', 16)
        n = int('0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973', 16)
    elif curve == "NIST521p":
        p = int('0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 16)
        a = int('0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc', 16)
        b = int('0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00', 16)
        gx = int('0x00c6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66', 16)
        gy = int('0x011839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650', 16)
        n = int('0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa51868783bf2f966b7fcc0148f709a5d03bb5c9b8899c47aebb6fb71e91386409', 16)

    A = random.randint(1, n)
    return p, a, b, gx, gy, A

def is_point_on_curve(x, y, a, b, p):
    left = (y * y) % p
    right = (x * x * x + a * x + b) % p
    print(left)
    print(right)
    return left == right

def find_next_point(a, b, p, x):
    while True:
        y = get_y_in_curve(x, a, b, p)
        
        if y is not None:
            return (x, y)

        x += 1
        if x >= p:
            x = 0

def get_y_in_curve(x, a, b, p):
    y2 = x**3 + a*x + b
    y_int = modular_sqrt(y2, p)
    if y_int and ((y_int * y_int) % p) == (y2 % p):
        return y_int
    return None


def validate_ecdh_public(p, a, b, X, Y, A):
    if p == None or a == None or b == None:
        return False, "Pola przechowujące liczby p, a i b muszą być uzupełnione!"
    p2 = find_prime_by_probability(p, 50)
    if (p != p2):
        return False, f"{p} nie jest liczbą pierwszą spróbuj {p2}"
    if not (1 < a < p):
       return False, "Liczba a musi być większa od 1 i mniejsza od p!"
    if not (1 < b < p):
       return False, "Liczba b musi być większa od 1 i mniejsza od p!"
    if not (1 < b < p):
       return False, "Liczba b musi być większa od 1 i mniejsza od p!"
    if Y != None and X == None:
        return False, "Jeśli podałeś drugą współrzędną generatora to podaj też współrzędną X!"
    if Y != None and X != None:
        if ((Y*Y) % p != (pow(X, 3, p) + a*X + b) % p):
            new_point = find_next_point(a, b, p, X)
            return False, f"Punkt ({X}, {Y}) nie należy do krzywej. Następny punkt na krzywej: {new_point}"
    if X != None and Y == None:
        Y = get_y_in_curve(X, a, b, p)
        if Y == None:
            new_point = find_next_point(a, b, p, X)
            return False, f"Punkt o współrzędnej równej {X} nie należy do krzywej. Następny punkt na krzywej: {new_point}"

    if A == None:
       A = random.randint(1, p)   
    if not (1 < A < p):
       return False, "Liczba A musi być większa od 1 i mniejsza od p!"

    return True, [p, a, b, X, Y, A]

def calculate_ecdh_public(p, a, b, X, Y, A):
    G = X, Y
    C = apply_double_and_add_method(G, A, p, a, b)
    cx, cy = C
    return p, a, b, X, Y, A, cx, cy

