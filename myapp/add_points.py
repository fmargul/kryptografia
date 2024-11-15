from .scripts import find_prime_by_probability

def is_point_on_curve(x, y, a, b, p):
    left = (y * y) % p
    right = (x * x * x + a * x + b) % p
    print(left)
    print(right)
    return left == right

def find_next_point(a, b, p, x):
    while True:
        rhs = (x * x * x + a * x + b) % p
        y = None
        for potential_y in range(p):
            if (potential_y * potential_y) % p == rhs:
                y = potential_y
                break
        
        if y is not None:
            return (x, y)

        x += 1
        if x >= p:
            x = 0
        
def add_points(P, Q, p, a):
  xp, yp = P
  xq, yq = Q
  if xp == xq and yp == yq:
    s = (3 * xp * xq + a) * pow(2 * yp, -1, p)
  else:
    s = (yq - yp) * pow(xq - xp, -1, p)

  xr = (s*s - xp - xq) % p
  yr = (s * (xp - xr) - yp) % p

  return xr, yr

def ecc_check_data(x1, x2, y1, y2, a, b, p):

    p2 = find_prime_by_probability(p, 10)
    if (p != p2):
        return f"{p} nie jest liczbą pierwszą spróbuj {p2}"
    
    if not (is_point_on_curve(x1, y1, a, b, p)):
        new_point = find_next_point(a, b, p, x1)
        return f"Punkt ({x1}, {y1}) nie należy do krzywej. Następny punkt na krzywej: {new_point}"

    if not (is_point_on_curve(x2, y2, a, b, p)):
        new_point = find_next_point(a, b, p, x2)
        return f"Punkt ({x2}, {y2}) nie należy do krzywej. Następny punkt na krzywej: {new_point}"
    
    P = x1, y1
    Q = x2, y2
    R = add_points(P, Q, p, a)
    xr, yr = R
    return f"Po dodaniu punktu ({x1}, {y1}) i ({x2}, {y2}) na krzywej y<sup>2</sup> = x<sup>3</sup> + {a}x + {b} w Z<sub>{p}</sub> otrzymano ({xr}, {yr})."
