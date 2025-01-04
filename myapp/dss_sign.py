import random
import hashlib

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def is_prime_by_probability(n, accuracy=50):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

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

def find_prime_by_probability(n, accuracy=50):
    while not is_prime_by_probability(n, accuracy):
        n += 1
    return n

def generate_safe_prime(bits=1024, accuracy=50):
    q = find_prime_by_probability(random.randint(2**(bits // 2 - 1), 2**(bits // 2) - 1), accuracy)
    p = 2 * q + 1
    while not is_prime_by_probability(p, accuracy):
        q = find_prime_by_probability(random.randint(2**(bits // 2 - 1), 2**(bits // 2) - 1), accuracy)
        p = 2 * q + 1
    return p, q

def generate_generator_dss(p, q):
    """Generuje generator g dla grupy modulo p."""
    while True:
        h = random.randint(2, p - 2)  # Losuj h zamiast iterować
        g = modular_exponentiation(h, (p - 1) // q, p)
        # Sprawdź, czy g jest poprawnym generatorem
        if g > 1 and modular_exponentiation(g, q, p) == 1:
            return g

def generate_keys(p, q, g):
    private_key = random.randint(1, q - 1)
    public_key = modular_exponentiation(g, private_key, p)
    return private_key, public_key

def generate_signature(message, p, q, g, private_key):
    message_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    while True:
        k = random.randint(1, q - 1)
        r = modular_exponentiation(g, k, p) % q
        if r == 0:
            continue
        k_inv = pow(k, -1, q) 
        s = (k_inv * (message_hash + private_key * r)) % q
        if s != 0:
            return {"r": r, "s": s}

def verify_signature(message, r, s, public_key, p, q, g):
    if not (0 < r < q and 0 < s < q):
        return False

    message_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = pow(s, -1, q)  
    u1 = (message_hash * w) % q
    u2 = (r * w) % q
    v = ((modular_exponentiation(g, u1, p) * modular_exponentiation(public_key, u2, p)) % p) % q

    return v == r

if __name__ == "__main__":
    p, q = generate_safe_prime(bits=512)
    g = generate_generator_dss(p, q)
    print(f"p: {p}\nq: {q}\ng: {g}\n")

    private_key, public_key = generate_keys(p, q, g)
    print(f"Klucz prywatny: {private_key}")
    print(f"Klucz publiczny: {public_key}\n")

    message = "Siema"

    signature = generate_signature(message, p, q, g, private_key)
    print(f"Podpis:\nr: {signature['r']}\ns: {signature['s']}\n")

    is_valid = verify_signature(message, signature['r'], signature['s'], public_key, p, q, g)
    print("Czy podpis jest prawidłowy?", "Tak" if is_valid else "Nie")
