from rsa import *
from scripts import *
from dss import *
from diffie_hellman import *
from ecdh import *

# RSA test on a number

p, q = rsa_get_private_key_primes(128)
print(p, q)
n = p*q
print(n)
euler_n = (p-1)*(q-1)
print(euler_n)
e = 65537
d = rsa_get_private_exponent(e, euler_n)
print(e, d)

test_public = PublicKey(e,n)
test_private = PrivateKey(d,p,q)

message = 420
encrypted = pow(message,test_public.e, test_public.n)
print(encrypted)
decrypted = pow(encrypted,test_private.d,(test_private.p*test_private.q))
print(decrypted)


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# Conversion of text into numbers (block division)
numbers = convert_text_to_numbers(text)
print("Blocks in figures:", numbers)

# Conversion back from numbers to text
recovered_text = convert_numbers_to_text(numbers)
print("Recovered text:", recovered_text)


# RSA test on a text message ("Lorem Ipsum" using 128-bit keys)

print("RSA TEST\n")
blocks_encr_RSA = []
numbers_to_encrypt = convert_text_to_numbers(text)
print("Blocks in figures:", numbers_to_encrypt, "\n")
for block in numbers_to_encrypt:
    blocks_encr_RSA.append(pow(block, test_public.e, test_public.n))

print("Encrypted blocks:", blocks_encr_RSA,"\n")
blocks_decr_RSA = []
for block in blocks_encr_RSA:
    blocks_decr_RSA.append(pow(block,test_private.d,(test_private.p*test_private.q)))
print("Decrypted blocks:", blocks_decr_RSA,"\n")

decrypted_text = convert_numbers_to_text(blocks_decr_RSA)
print("Recovered text:", decrypted_text,"\n")


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