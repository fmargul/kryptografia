import random
import math
from .diffie_hellman_public import modular_exponentiation, is_prime_by_probability

# Generowanie klucza prywatnego drugiej strony
def generate_partners_private_key(p):
    return random.randint(1, p - 2)

# Generowanie klucza publicznego drugiej strony
def generate_partners_public_key(g, p): 
    partners_private_key = generate_partners_private_key(p)
    return modular_exponentiation(g, partners_private_key, p)

# Obliczenie wspólnego sekretu
def calculate_shared_secret(p, private_key, partners_public_key):
    return modular_exponentiation(partners_public_key, private_key, p)

# Walidacja danych
def validate_dh_data_shared(p, g, partners_public_key=None, private_key=None):
    if p is None or g is None or partners_public_key is None or private_key is None:
        return False, "Wszystkie pola formularza muszą być uzupełnione!"
    
    if not isinstance(p, int) or not isinstance(g, int):
        return False, "Liczby p i g muszą być liczbami całkowitymi!"

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

    if partners_public_key is not None:
        if not (1 <= partners_public_key <= p - 1):
            return False, "Klucz publiczny drugiej strony musi być w zakresie [1, p-1]!"

    if private_key is not None:
        if not (1 <= private_key <= p - 2):
            return False, "Klucz prywatny musi być w przedziale [1, p-2]!"
    
    return True, None
