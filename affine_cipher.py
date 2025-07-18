def e_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = e_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inv(a, m):
    g, x, y = e_gcd(a, m)
    if g != 1:
        return None
    return x % m

def affine_cipher(t, a, b, op):
    r = ""
    if op == 2: # decrypt
        a_inv = mod_inv(a, 26)
        if a_inv is None:
            return "Error: 'a' has no modular inverse. Decryption is not possible."
        for char in t.upper():
            if char.isalpha():
                c = ord(char) - ord('A')
                p = (a_inv * (c - b)) % 26
                r += chr(p + ord('A'))
            else:
                r += char
    else: # encrypt
        for char in t.upper():
            if char.isalpha():
                p = ord(char) - ord('A')
                c = (a * p + b) % 26
                r += chr(c + ord('A'))
            else:
                r += char
    return r

choice = input("Enter 1 to Encrypt or 2 to Decrypt: ")

print("\n--- Affine Cipher ---")

if choice == '1':
    pt = input("Enter the plaintext: ")
    a = int(input("Enter key 'a' (must be coprime to 26): "))
    b = int(input("Enter key 'b': "))
    
    if e_gcd(a, 26)[0] != 1:
        print(f"Error: 'a' ({a}) is not coprime to 26. Please choose another 'a'.")
    else:
        et = affine_cipher(pt, a, b, 1)
        print(f"Encrypted Text: {et}")
    
elif choice == '2':
    ct = input("Enter the ciphertext: ")
    a = int(input("Enter key 'a': "))
    b = int(input("Enter key 'b': "))

    if e_gcd(a, 26)[0] != 1:
         print(f"Error: 'a' ({a}) is not coprime to 26. Decryption is not possible with this key.")
    else:
        dt = affine_cipher(ct, a, b, 2)
        print(f"Decrypted Text: {dt}")
    
else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")