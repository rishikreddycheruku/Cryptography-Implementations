# Cryptography & Number Theory Scripts 🐍

Welcome to this collection of Python scripts designed for demonstrating classical cryptographic ciphers and fundamental number theory concepts. Each script is a self-contained command-line tool that allows you to encrypt, decrypt, or perform mathematical verifications.

This project is perfect for students, hobbyists, or anyone interested in the basics of cryptography and its underlying mathematics.

## ✨ Algorithms and Ciphers

This repository includes implementations of the following algorithms:

  * **Shift Cipher**: One of the simplest and most widely known encryption techniques.
  * **Substitution Cipher**: A method of encryption where units of plaintext are replaced with ciphertext.
  * **Affine Cipher**: A type of monoalphabetic substitution cipher, using a linear function.
  * **Vigenère Cipher**: A method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
  * **Extended Euclidean Algorithm**: An algorithm to find the greatest common divisor (GCD) of two integers and their Bezout coefficients.
  * **Fermat's Little Theorem**: A script to verify the theorem and find modular inverses.

-----

## 📜 Script Details

### Affine Cipher (`affine_cipher.py`)

This script encrypts and decrypts text using an Affine cipher, which relies on the formula $C = (aP + b) \\pmod{26}$ for encryption. For this cipher to work, the key `a` must be coprime with 26 (i.e., their greatest common divisor must be 1).

**Usage Example (Encryption):**

```
Enter 1 to Encrypt or 2 to Decrypt: 1

--- Affine Cipher ---
Enter the plaintext: HELLO
Enter key 'a' (must be coprime to 26): 5
Enter key 'b': 8
Encrypted Text: RCLLA
```

### Extended Euclidean Algorithm (`extended_euclidean.py`)

This script calculates the greatest common divisor (GCD) of two integers, `a` and `b`. It also demonstrates the steps of the Extended Euclidean Algorithm, which finds integers `u` and `v` such that $au + bv = \\text{gcd}(a, b)$. The steps are displayed in a clear table format.

**Usage Example:**

```
Enter the value of A : 99
Enter the value of B : 78
The GCD of 99 , 78 is 3
   q  r(n-1)  r(n)  r(n+1) u(n-1) u(n) u(n+1) v(n-1) v(n) v(n+1)
1  1      99    78      21      1    0       1      0    1      -1
2  3      78    21      15      0    1      -3      1   -1       4
3  1      21    15       6      1   -3       4     -1    4      -5
4  2      15     6       3     -3    4     -11      4   -5      14
5  2       6     3       0      4  -11          -5   14
```

### Fermat's Little Theorem (`fermats_little_theorem.py`)

This utility script has two modes based on Fermat's Little Theorem:

1.  **Verify the theorem**: Checks if $a^{p-1} \\equiv 1 \\pmod{p}$, where `p` is a prime number.
2.  **Find modular inverse**: Calculates the modular multiplicative inverse of `a` modulo `p` using the property that $a^{p-2} \\equiv a^{-1} \\pmod{p}$.

**Usage Example (Finding Inverse):**

```
Enter 1 to verify the theorem or 2 to find the modular inverse: 2

--- Fermat's Little Theorem ---
Enter an integer (a) to find its inverse: 3
Enter the prime modulus (p): 13

Finding inverse: a^(p-2) ≡ a⁻¹ (mod p)
The modular inverse of 3 mod 13 is: 9
Verification: (3 * 9) mod 13 = 1
```

### Shift Cipher (`shift_cipher.py`)

This script implements the Shift Cipher (also known as the Caesar Cipher). It substitutes each letter in the plaintext with a letter a fixed number of positions down the alphabet.

**Usage Example (Decryption):**

```
Enter 1 to encrypt or 2 to decrypt: 2

--- Shift Cipher ---
Enter the ciphertext: Khoor Zruog
Enter the shift key (an integer): 3
Decrypted Text: Hello World
```

### Substitution Cipher (`substitution_cipher.py`)

This script performs a simple substitution cipher using a predefined key where each letter of the alphabet is mapped to another letter. The alphabet `ABCDEFGHIJKLMNOPQRSTUVWXYZ` is mapped to the key `QWERTYUIOPASDFGHJKLZXCVBNM`.

**Usage Example (Encryption):**

```
Enter 1 to encrypt or 2 to decrypt: 1

--- Substitution Cipher ---
Enter the plaintext: HELLO WORLD
Encrypted Text: ITSSG VGKSR
```

### Vigenère Cipher (`vigenere_cipher.py`)

This script implements the Vigenère cipher, a polyalphabetic substitution cipher that uses a keyword to create a series of interwoven shift ciphers. The script provides a detailed, step-by-step view of the encryption process.

**Usage Example (Encryption):**

```
Enter 1 to encrypt or 2 to decrypt: 1

--- Vigenère Cipher ---
Enter the plaintext: ATTACK AT DAWN
Enter the keyword: LEMON

Encryption Process:
Plaintext:      A T T A C K   A T   D A W N
Repeating Key:  L E M O N L   E M   O N L E
Ciphertext:     L X F O P V   E F   R L P H

Final Encrypted Text: LXFOVEFR LPH
```
