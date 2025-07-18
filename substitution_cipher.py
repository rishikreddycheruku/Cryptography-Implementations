def substitution_cipher(t, ab, ky, m):
    r = ""
    t = t.upper()
    
    if m == 2:  # Mode 2 is for decryption, so we swap ky and ab
        ab, ky = ky, ab
        
    for c in t:
        try:
            i = ab.find(c)
            if i != -1:
                r += ky[i]
            else:
                r += c
        except IndexError:
            r += c
            
    return r

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY_STRING = "QWERTYUIOPASDFGHJKLZXCVBNM"

ch = input("Enter 1 to encrypt or 2 to decrypt: ")

print("\n--- Substitution Cipher ---")

if ch == '1':
    pt = input("Enter the plaintext: ")
    et = substitution_cipher(pt, ALPHABET, KEY_STRING, 1) # Mode 1 for encrypt
    print(f"Encrypted Text: {et}")
    
elif ch == '2':
    ct = input("Enter the ciphertext: ")
    dt = substitution_cipher(ct, ALPHABET, KEY_STRING, 2) # Mode 2 for decrypt
    print(f"Decrypted Text: {dt}")
    
else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")