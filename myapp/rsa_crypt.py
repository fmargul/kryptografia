from .scripts import *
import time
from .constants import BLOCK_SIZE
import base64
import json
from binascii import Error
from math import log2, floor
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

def rsa_get_prime(bits):
  while True:
    potential_prime = random.getrandbits(bits)
    if is_prime_by_probability(potential_prime,50):
      return potential_prime

def rsa_get_private_key_primes(bits):
  print(bits)
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

def rsa_get_random_e(p,q):
  bits = len(bin((p-1)*(q-1))[2:])
  
  while True:
    potential_prime = random.getrandbits(bits-1)
    if is_prime_by_probability(potential_prime,50):
      d = rsa_get_private_exponent(potential_prime, (p-1)*(q-1))
      if d != -1:
        return potential_prime, d

def generate_p_q_e(bits):
  p, q = rsa_get_private_key_primes(bits//2)
  e = rsa_get_random_e(p,q)
  return p,q,e

def validate_p_q(p,q):
  if p == None or q == None:
    return False, "p i q muszą być podane!"
  elif not is_prime_by_probability(p, 50):
    return False, f"p nie jest liczbą pierwszą!"
  elif not is_prime_by_probability(q, 50):
    return False, f"q nie jest liczbą pierwszą!"
  else:
    return True, f"git"

def validate_p_q_e(p,q,e):
  valid, error = validate_p_q(p,q)
  
  if not valid:
    return valid, error
  else:
    totient = (p-1)*(q-1)
    if e == None:
      return False, "Wszystkie pola muszą być uzupełnione!"
    elif not is_prime_by_probability(e, 50):
      return False, f"e nie jest liczbą pierwszą!"
    elif not (1 < e < totient):
      return False, f"e musi być większe od 1 i mniejsze od (p-1)*(q-1)!"
    else:
      d = rsa_get_private_exponent(e, totient)
      if d == -1:
        return False, f"e musi być względnie pierwsze z (p-1)*(q-1)!"
      else:
        return True, f"git", d

def validate_rsa(p,q,e,msg):
  valid, error, *d = validate_p_q_e(p,q,e)
  if not valid:
    return valid, error
  else:
    if msg == "":
      return False, "Wszystkie pola muszą być uzupełnione!"
    else:
      return True, f"git"

def get_RSA_key_pair(size_multiplier):
  print("Generating " + str(int(8*size_multiplier*BLOCK_SIZE)) + "-bit keys...")
  p, q = rsa_get_private_key_primes(int(4*size_multiplier*BLOCK_SIZE))
  #print(p, q)
  n = p*q
  #print(n)
  euler_n = (p-1)*(q-1)
  #print(euler_n)
  e = 65537
  d = rsa_get_private_exponent(e, euler_n)
  #print(e, d)
  return PublicKey(e,n), PrivateKey(d,p,q)

def get_pub_key_from_data(p,q,e):
  n = p*q
  return PublicKey(e,n)

def get_priv_key_from_data(p,q,e):
  d = rsa_get_private_exponent(e, (p-1)*(q-1))
  return PrivateKey(d,p,q)

def chinese_remainder_theorem_decryption(m, p, q, dp, dq):
  m1 = modular_exponentiation(m,dp,p)
  m2 = modular_exponentiation(m,dq,q)
  q_inv = rsa_get_private_exponent(q,p) #this function performs modular inversion
  h = (q_inv * (m1 - m2)) % p
  m = m2 + h * q
  return m

def rsa_encrypt_message(text, n,e):
  print("Encrypting text '" + text + "'...")
  #block_size = len(bin(n)[2:])
  block_size = floor(log2(n) / 8) 
  #pub_key = get_pub_key_from_data(p,q,e)

  blocks_encr_RSA = []
  numbers_to_encrypt = convert_text_to_numbers(text, block_size)
  for block in numbers_to_encrypt:
      blocks_encr_RSA.append(modular_exponentiation(block, e, n))

  json_data = json.dumps(blocks_encr_RSA)
  json_bytes = json_data.encode('utf-8')
  base64_encoded = base64.b64encode(json_bytes)
  return base64_encoded.decode('utf-8')

def rsa_decrypt_message(b64, p,q,d):
  
  #priv_key = get_priv_key_from_data(p,q,e)

  try:
    json_bytes = base64.b64decode(b64)
    json_data = json_bytes.decode('utf-8')
    blocks_encr_RSA = json.loads(json_data)
  except Error:
    return -1

  blocks_decr_RSA = []
  print("Decrypting...")
  for block in blocks_encr_RSA:
      blocks_decr_RSA.append(chinese_remainder_theorem_decryption(block,p,q,modular_exponentiation(d,1,p-1),modular_exponentiation(d,1,q-1)))
      #blocks_decr_RSA.append(modular_exponentiation(block,d,(p*q)))
      
  print("Decrypted blocks: ", blocks_decr_RSA,"\n")

  try:
    decrypted_text = convert_numbers_to_text(blocks_decr_RSA)
  except UnicodeDecodeError:
    return -1
  
  print("Recovered text:", decrypted_text,"\n")
  return decrypted_text












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
  return t2-t1

def run_RSA_tests():
  test_public, test_private = get_RSA_key_pair(1)
  print("Public Key details:\ne="+str(test_public.e)+"\nn="+str(test_public.n))
  print("Private Key details:\nd="+str(test_private.d)+"\np="+str(test_private.p)+"\nq="+str(test_private.q))
  test_RSA_number(test_public, test_private, False)
  test_RSA_number(test_public, test_private, True)
  test_RSA_text(test_public, test_private, False)
  test_RSA_text(test_public, test_private, True)

