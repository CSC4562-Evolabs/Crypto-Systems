# John Hudnall
# CSC 4562 Project 2
# RSA Encryption and Decryption Algorithms

import random
import math

# Function to find the greatest common divsor of phi(n) for use in finding e
def gcd(e, phi):
    while phi != 0:
        temp = e
        e = phi
        phi = temp % phi
    return e

# This function is the Extended Euclidean Algorithm which is used to find the 
# multiplicative inverse of e and phi
def eeAlgorithm(e, phi):
        if phi == 0:
            return 1, 0, e
        else:
            quotient = e // phi
            remainder = e % phi
            x, y, is1Check = eeAlgorithm(phi, remainder)
            return y, x - quotient * y, is1Check

# Function to find the multiplicative inverse of e mod phi(n) for use in finding d
def multiplicativeInverse(e, phi):
     x, y, is1Check = eeAlgorithm(e, phi)
     if is1Check == 1:
          return x % phi

# Fucntion that will use the numbers found in the above functions to generate the 
# public and private key pairs
def generateKeys(p, q):
     n = p * q
     phi = (p - 1) * (q - 1)
     e = random.randint(2, phi - 1)
     # To find e, a random number is generated until one is found that is prime
     # within the range of numbers from 2 to phi-1 using the while loop below
     while True:
          e = random.randint(2, phi - 1)
          if gcd(e,phi) == 1:
            break

     d = multiplicativeInverse(e, phi)
     return ((e, n), (d, p, q))

# Function to encrypt a given plaintext
# For our implmentation, the ciphertext will output a number for each letter of input
# If there are spaces in the input, each space will also output a number as well
def encryptMessage(key, plaintext):
     e, n = key
     # The number related to each letter from input is calculated here
     # Using ord(), each letter is mapped a-z to 0-25 using the letter's ASCII value - 97,
     # that value is then plugged into the cipher formula: C = M^e % n
     # Spaces are also mapped using their ASCII code - 97, if spaces are used
     ciphertext = [(pow((ord(char) - 97), e, n)) for char in plaintext]

     return ciphertext

# Function to decrypt a given ciphertext, output is the original message
def decryptMessage(key, ciphertext):
     d, p, q = key
     n = p * q
     # to get plaintext we do the opposite of what was done in encryptMessage
     # Decipher formula: M = C^d % n
     plaintext = [chr(pow(char, d, n) + 97) for char in ciphertext]

     return ''.join(plaintext)

# Encrypt and decrypt a message using public and private keys, respectively
if __name__ == '__main__':
     # p and q are the 10th and 19th prime numbers from primeFinder.py, respectively
     p = 1061
     q = 1117
     publicKey, privateKey = generateKeys(p, q)
     inputMessage = "rsa"
     ciphertext = encryptMessage(publicKey, inputMessage)
     plaintext = decryptMessage(privateKey, ciphertext)

     print("\nPublic Key (e, n): " + "".join(str(publicKey)))
     print("Private Key (d, p, q): " + "".join(str(privateKey)))
     print("\nMessage: " + inputMessage)
     print("Encrypt message output: " + str(ciphertext))
     print("Decrypt message output: " + plaintext + "\n")