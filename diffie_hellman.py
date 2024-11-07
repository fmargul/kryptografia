import random
from scripts import *

# Warunek p = 2q + 1
def generate_safe_prime(bits, accuracy=5):
    # q - liczba pierwsza
    q = find_prime_by_probability(2**(bits - 1), accuracy)

    p = 2 * q + 1
    
    # Sprawdzenie, czy p jest liczbą pierwszą
    while not is_prime_by_probability(p, accuracy):
        q = find_prime_by_probability(q + 1, accuracy)
        p = 2 * q + 1
        
    return p

# Generowanie klucza publicznego
def generate_public_key(g, private_key, p):
    return modular_exponentiation(g, private_key, p)

# Generowanie klucza prywatnego
def generate_private_key(p):
    return random.randint(1, p - 2)

class DiffieHellmanUser:
    def __init__(self, name, p, g):
        self.name = name
        self.p = p
        self.g = g
        self.private_key = generate_private_key(p)
        self.public_key = generate_public_key(g, self.private_key, p)

    # Obliczenie wspólnego sekretu
    def generate_shared_secret(self, other_public_key):
        return modular_exponentiation(other_public_key, self.private_key, self.p)

# Test
def test_diffie_hellman():
    # Generowanie dużej liczby pierwszej (moduł p) i generatora g
    p = generate_safe_prime(512, accuracy=5)
    g = random.randint(2, p - 1)
    
    print(f"Modulus p: {p}")
    print(f"Generator g: {g}")
    
    # Tworzenie dwóch użytkowników - Alice i Bob
    alice = DiffieHellmanUser("Alice", p, g)
    bob = DiffieHellmanUser("Bob", p, g)
    
    print(f"Alice - Private key: {alice.private_key}, Public key: {alice.public_key}")
    print(f"Bob - Private key: {bob.private_key}, Public key: {bob.public_key}")
    
    # Obliczenie wspólnego sekretu
    alice_shared_secret = alice.generate_shared_secret(bob.public_key)
    bob_shared_secret = bob.generate_shared_secret(alice.public_key)
    
    print(f"Shared secret (Alice): {alice_shared_secret}")
    print(f"Shared secret (Bob): {bob_shared_secret}")
    
    # Sprawdzenie, czy oba sekrety są równe
    if alice_shared_secret == bob_shared_secret:
        print("The shared secret is the same for Alice and Bob.")
    else:
        print("Error - the shared secret is not the same.")
