from scripts import *
import time
import math
from constants import BLOCK_SIZE

class PublicKey:
  def __init__(self, e, n):
    self.e = e
    self.n = n
  
class PrivateKey:
  def __init__(self, d, p, q):
    self.d = d
    self.p = p
    self.q = q
    #self.dp = d % p-1
    self.dp = modular_exponentiation(d,1,p-1)
    #self.dq = d % q-1
    self.dq = modular_exponentiation(d,1,q-1)

def ext_euclidean(a, b):
  if b == 0:
    return a, 1, 0
  else:
    gcd, x1, y1 = ext_euclidean(b, a%b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def rsa_get_private_key_primes(bits):
  confirmed_primes = []
  while True and len(confirmed_primes)<2:
    potential_prime = random.getrandbits(bits)
    if is_prime_by_probability(potential_prime,50):
      confirmed_primes.append(potential_prime)
  
  return confirmed_primes[0], confirmed_primes[1]

def rsa_get_private_exponent(e, euler_n):         # d = e^-1 mod phi(n)
  gcd, x, y = ext_euclidean(e, euler_n)
  if gcd != 1:
    print("Exponent e is not coprime with totient(n)")
    return -1
  else:
    return x % euler_n

def get_RSA_key_pair():
  p, q = rsa_get_private_key_primes(8*BLOCK_SIZE)
  #print(p, q)
  n = p*q
  #print(n)
  euler_n = (p-1)*(q-1)
  #print(euler_n)
  e = 65537
  d = rsa_get_private_exponent(e, euler_n)
  #print(e, d)
  return PublicKey(e,n), PrivateKey(d,p,q)

def chinese_remainder_theorem_decryption(m, p, q, dp, dq):
  m1 = modular_exponentiation(m,dp,p)
  m2 = modular_exponentiation(m,dq,q)
  q_inv = rsa_get_private_exponent(q,p) #this function performs modular inversion
  h = (q_inv * (m1 - m2)) % p
  m = m2 + h * q
  return m

def test_RSA_number(test_public, test_private, using_CRT):
  print("\nRSA TEST ON NUMBER\n")


  message = 420
  print("Encrypting number '" + str(message) + "'...")
  encrypted = modular_exponentiation(message,test_public.e, test_public.n)
  print("Result: " + str(encrypted))
  print("Decrypting (with CRT)..." if using_CRT else "Decrypting (without CRT)...")
  t1 = 0
  t2 = 0
  if not using_CRT:
    t1 = time.time()
    decrypted = modular_exponentiation(encrypted,test_private.d,(test_private.p*test_private.q))
    t2 = time.time()
  else:
    t1 = time.time()
    decrypted = chinese_remainder_theorem_decryption(encrypted, test_private.p,test_private.q,test_private.dp,test_private.dq)
    t2 = time.time()
  print("Decrypted number: " + str(decrypted))
  print("Decryption - time elapsed: " + str(round(t2-t1,3)) + " seconds.")

def test_RSA_text(test_public, test_private, using_CRT):
  print("\nRSA TEST ON TEXT\n")

  text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  print("Encrypting text '" + text + "'...")
  # Conversion of text into numbers (block division)
  #numbers = convert_text_to_numbers(text)
  #print("Blocks in figures:", numbers)

  # Conversion back from numbers to text
  #recovered_text = convert_numbers_to_text(numbers)
  #print("Recovered text:", recovered_text)


  # RSA test on a text message ("Lorem Ipsum" using 128-bit keys)

  
  blocks_encr_RSA = []
  numbers_to_encrypt = convert_text_to_numbers(text)
  #print("Blocks in figures:", numbers_to_encrypt, "\n")
  for block in numbers_to_encrypt:
      blocks_encr_RSA.append(modular_exponentiation(block, test_public.e, test_public.n))

  print("Encrypted blocks: ", blocks_encr_RSA,"\n")
  blocks_decr_RSA = []
  print("Decrypting (with CRT)..." if using_CRT else "Decrypting (without CRT)...")
  t1 = time.time()
  for block in blocks_encr_RSA:
      if not using_CRT:
        blocks_decr_RSA.append(modular_exponentiation(block,test_private.d,(test_private.p*test_private.q)))
      else:
        blocks_decr_RSA.append(chinese_remainder_theorem_decryption(block, test_private.p,test_private.q,test_private.dp,test_private.dq))
  

  print("Decrypted blocks: ", blocks_decr_RSA,"\n")

  decrypted_text = convert_numbers_to_text(blocks_decr_RSA)
  t2 = time.time()
  print("Recovered text:", decrypted_text,"\n")
  print("Decryption - elapsed time: " + str(round(t2-t1,3)) + " seconds.")

def run_RSA_tests():
  test_public, test_private = get_RSA_key_pair()
  print("Public Key details:\ne="+str(test_public.e)+"\nn="+str(test_public.n))
  print("Private Key details:\nd="+str(test_private.d)+"\np="+str(test_private.p)+"\nq="+str(test_private.q))
  test_RSA_number(test_public, test_private, False)
  test_RSA_number(test_public, test_private, True)
  test_RSA_text(test_public, test_private, False)
  test_RSA_text(test_public, test_private, True)