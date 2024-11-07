import math
import random

from constants import BLOCK_SIZE

def is_prime(n):
  if (n <= 1): return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if(n % i == 0):
      #print(i)
      return False
  return True

def find_prime(n): #fajnie jakby wpisywane liczby były większe od 2 lub nawet wyżej
  if (is_prime(n)): return int(n)
  else:
    next_number = n + 1
    while not is_prime(next_number):
      next_number += 1
    return int(next_number)

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
      x = pow(x, 2, n)        # tutaj zmienione w potędze 'x' zamiast 'a'
      if x == n - 1:
        break
    else:                     # else tutaj powinien być do fora (nie wiedziałem że tak można) zamiast do ifa
      return False
  return True

def find_prime_by_probability(n, accuracy):
  if (is_prime_by_probability(n, accuracy)): return int(n)
  else:
    next_number = n + 1
    while not is_prime_by_probability(next_number, accuracy):
      next_number += 1
    return int(next_number)

def text_to_blocks(text, block_size=BLOCK_SIZE):
    # Divides the text into blocks of a specified size and converts each block into a number
    blocks = []
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        block_number = int.from_bytes(block.encode('utf-8'), 'big')
        blocks.append(block_number)
    return blocks

def blocks_to_text(blocks):
    # Converts a list of numbers (blocks) into text
    text = ''
    for block in blocks:
        byte_length = (block.bit_length() + 7) // 8
        text += block.to_bytes(byte_length, 'big').decode('utf-8')
    return text

def convert_text_to_numbers(text):
    # Converts text into a list of numbers in block form
    blocks = text_to_blocks(text)
    return blocks

def convert_numbers_to_text(numbers):
    # Converts a list of numbers (blocks) into full text
    text = blocks_to_text(numbers)
    return text

# Funkcja do manualnego potęgowania z modulo (algorytm szybkiego potęgowania)
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result
