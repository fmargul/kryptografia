import random
import math

# Funkcja do obliczeń modularnych (szybkie potęgowanie)
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

# Sprawdzanie liczby pierwszej przy użyciu probabilistycznego testu
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
      x = pow(x, 2, n)        
      if x == n - 1:
        break
    else:                     
      return False
  return True

# Znalezienie liczby pierwszej przy użyciu probabilistycznego testu
def find_prime_by_probability(n, accuracy):
  if (is_prime_by_probability(n, accuracy)): return int(n)
  else:
    next_number = n + 1
    while not is_prime_by_probability(next_number, accuracy):
      next_number += 1
    return int(next_number)
    
# Warunek p = 2q + 1
def generate_safe_prime(bits, accuracy):
    # Losowe rozpoczęcie poszukiwań liczby q
    start = random.randint(2**(bits - 1), 2**bits - 1)
    q = find_prime_by_probability(start, accuracy)

    p = 2 * q + 1

    # Sprawdzenie, czy p jest liczbą pierwszą
    while not is_prime_by_probability(p, accuracy):
        # Losowanie kolejnego q
        start = random.randint(2**(bits - 1), 2**bits - 1)
        q = find_prime_by_probability(start, accuracy)
        p = 2 * q + 1
    
    return p

# Generowanie generatora (g)
def generate_generator(p):
    while True:
        g = random.randint(1, p - 1)
        if pow(g, 2, p) != 1 and pow(g, (p - 1) // 2, p) != 1:
            return g

# Generowanie klucza prywatnego
def generate_private_key(p):
    return random.randint(1, p - 2)

# Obliczenie klucza publicznego
def calculate_public_key(g, private_key, p):
    p = int(p)
    return modular_exponentiation(g, private_key, p)

# Walidacja danych
def validate_dh_data_public(p, g, private_key=None):    
    if p is None or g is None or private_key is None:
        return False, "Wszystkie pola formularza muszą być uzupełnione!"
    
    try:
        p = int(p)
        g = int(g)
        private_key = int(private_key)
    except ValueError:
        return False, "Liczby p, g i klucz prywatny muszą być liczbami całkowitymi!"
    
    if not is_prime_by_probability(p, 50):
        return False, "Liczba p musi być liczbą pierwszą!"
    
    if (p - 1) % 2 != 0:
        return False, "Liczba p musi mieć postać 2 * q + 1!"
    
    q = (p - 1) // 2
    
    if not is_prime_by_probability(q, 50):
        return False, "Liczba q = (p - 1) / 2 musi być liczbą pierwszą!"
    
    if not (1 < g < p):
        return False, "Generator g musi być większy od 1 i mniejszy od p!"
    
    if pow(g, 2, p) == 1 or pow(g, (p - 1) // 2, p) == 1:
        return False, "Generator g nie spełnia właściwości generatora grupy modulo p!"
    
    if private_key is not None:
        if not (1 <= private_key <= p - 2):
            return False, "Klucz prywatny musi być w przedziale [1, p-2]!"

    return True, None
