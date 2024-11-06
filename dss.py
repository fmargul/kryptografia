import math
import random
import hashlib
from scripts import find_prime_by_probability

# 1.  Generating public and private keys
def generate_keys(prime_length=512, accuracy=10):
    # Generating prime numbers
    q = find_prime_by_probability(random.getrandbits(160), accuracy)
    p = find_prime_by_probability(random.getrandbits(prime_length), accuracy)
    while (p - 1) % q != 0:
        p = find_prime_by_probability(random.getrandbits(prime_length), accuracy)
    
    # Choice of generator g
    h = random.randint(2, p - 2)
    g = pow(h, (p - 1) // q, p)
    while g == 1:
        h = random.randint(2, p - 2)
        g = pow(h, (p - 1) // q, p)
    
    # Generation of private key x and public key y
    x = random.randint(1, q - 1)  # Private key
    y = pow(g, x, p)  # Public key
    
    return (p, q, g, y), x

# 2. Signing messages
def sign_message(message, private_key, params):
    p, q, g, _ = params
    x = private_key
    
    # Message digest calculation - to be implemented primitively?
    hash_object = hashlib.sha256()
    hash_object.update(message.encode('utf-8'))
    h_m = int(hash_object.hexdigest(), 16)
    
    # Selection of a random number k
    k = random.randint(1, q - 1)
    while math.gcd(k, q) != 1:
        k = random.randint(1, q - 1)
    
    # Calculation of the r and s signature
    r = pow(g, k, p) % q
    k_inv = pow(k, -1, q)
    s = (k_inv * (h_m + x * r)) % q
    
    return r, s

# 3. Verification of signature
def verify_signature(message, signature, public_key, params):
    p, q, g, y = params
    r, s = signature
    
    # Validation of r and s
    if not (0 < r < q and 0 < s < q):
        return False
    
    # Calculation of the message digest
    hash_object = hashlib.sha256()
    hash_object.update(message.encode('utf-8'))
    h_m = int(hash_object.hexdigest(), 16)
    
    # Calculation of w, u1, u2, v
    w = pow(s, -1, q)
    u1 = (h_m * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    
    # Verification of compliance
    return v == r

