from rsa import *
from scripts import *
from dss import *
from diffie_hellman import *
from ecdh import *

# RSA test on a number

test_RSA_number()
test_RSA_text()

# Digital Signature Algorithm (DSA) - Digital Signature Standard (DSS) 

#message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
#public_key, private_key = generate_keys()
#signature = sign_message(message, private_key, public_key)

#is_valid = verify_signature(message, signature, public_key, public_key)
#print("Is the signature correct?", is_valid)

# Uruchomienie testu dla algorytmu Diffiego-Hellmana
if __name__ == "__main__":
    test_diffie_hellman()

print()
test_ECDH()