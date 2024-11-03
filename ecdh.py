from scripts import *

# krzywa eliptyczna ma postac y^2 = x^3 + ax + b
# Funckja sprawdza, czy argument X należy do krzywej eliptycznej nad ciałem o wielkości p
# Jeśli nie to bierzę następną liczbę całkowitą, która należy do krzywej eliptycznej
def check_X(a, b, p, X, positive):
  X = int(X) % p
  Y2 = (X**3 + a*X + b) % p
  Y = math.sqrt(Y2)
  if Y % 1 == 0:
    if (positive): return X, int(Y)
    else:
      Y = -Y
      Y = Y % p
      return X, int(Y)
  else:
    if pow(Y2, int((p-1)/2), p) == 1:
      if p % 4 == 3:
        Y = pow(Y2, int((p+1)/4), p)
        if (positive): return X, int(Y)
        else:
          Y = -Y
          Y = Y % p
          return X, int(Y)
      else: return check_X(a, b, p, X+1, positive)
    else: return check_X(a, b, p, X+1, positive)

def point_to_point(P, Q, k, p, a):
  R = Q
  xp, yp = P
  for _ in range(k-1):
    Q = R
    if (Q != P):
      xq, yq = Q
      s = (yq - yp) * pow(xq - xp, -1, p) % p
      xr = (s**2-xq-xp) % p
      yr = (s*(xq-xr)-yq) % p
      R = xr, yr
    else:
      s = (3 * xp ** 2 + a) * pow(2 * yp, -1, p) % p
      xr = (s**2-2*xp) % p
      yr = (s*(xp - xr) - yp) % p
      R = xr, yr
  return R

def generate_public_key(a, b, c, p, X, positive):
  p = find_prime(p)
  G = check_X(a, b, p, X, positive)
  C = point_to_point(G, G, c, p, a)
  return C

def generate_private_key(a, b, d, p, C):
  p = find_prime(p)
  cdG = point_to_point(C, C, d, p, a)
  return cdG

def generate_private_key_rightaway(a, b, c, d, p, X, positive):
  C = generate_public_key(a, b, c, p, X, positive)
  cdG = generate_private_key(a, b, d, p, C)
  return cdG
