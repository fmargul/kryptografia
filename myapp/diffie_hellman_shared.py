import random
import math
from .diffie_hellman_public import modular_exponentiation, is_prime_by_probability

# Obliczenie wspólnego sekretu
def calculate_shared_secret(other_public_key, private_key, p):
    other_public_key = int(other_public_key)
    private_key = int(private_key)
    p = int(p)
    return modular_exponentiation(other_public_key, private_key, p)

# Walidacja danych
def validate_dh_data_shared(p, other_public_key=None, private_key=None):
    if not p or not other_public_key or not private_key:
        return False, "Wszystkie pola formularza muszą być uzupełnione!"

    try:
        p = int(p)
        other_public_key = int(other_public_key)
        private_key = int(private_key)
    except ValueError:
        return False, "Liczba p oraz klucz publiczny i prywatny muszą być liczbami całkowitymi!"

    # Sprawdzanie, czy p jest liczbą pierwszą
    if not is_prime_by_probability(p, 50):
        return False, "Liczba p musi być liczbą pierwszą!"

    # Sprawdzanie, czy p spełnia warunek 2q + 1
    if (p - 1) % 2 != 0:
        return False, "Liczba p musi mieć postać 2 * q + 1!"

    q = (p - 1) // 2
    if not is_prime_by_probability(q, 50):
        return False, "Liczba q = (p - 1) / 2 musi być liczbą pierwszą!"

    # Sprawdzanie zakresu klucza publicznego
    if not (1 <= other_public_key <= p - 1):
        return False, "Klucz publiczny drugiej strony musi być w zakresie [1, p-1]!"

    # Sprawdzanie zakresu klucza prywatnego
    if not (1 <= private_key <= p - 2):
        return False, "Twój klucz prywatny musi być w przedziale [1, p-2]!"

    return True, None
