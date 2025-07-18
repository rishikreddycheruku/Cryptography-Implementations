def generate_vigenere_key(t, k):
    """Generates a key of the same length as the text."""
    k = list(k.upper())
    fk = ""  # Full key
    ki = 0   # Key index
    for c in t.upper():
        if c.isalpha():
            fk += k[ki % len(k)]
            ki += 1
        else:
            fk += " "
    return fk

def vigenere_cipher(t, k, m):
    """Encrypts or decrypts text using the Vigenère cipher."""
    t = t.upper()
    fk = generate_vigenere_key(t, k)
    r = ""  # Result
    
    for i in range(len(t)):
        c = t[i]
        kc = fk[i] # Key character
        
        if c.isalpha():
            p_val = ord(c) - ord('A')
            k_val = ord(kc) - ord('A')
            
            if m == 2: # decryption
                c_val = (p_val - k_val + 26) % 26
            else: # encryption
                c_val = (p_val + k_val) % 26
            
            r += chr(c_val + ord('A'))
        else:
            r += c
    return r

ch = input("Enter 1 to encrypt or 2 to decrypt: ")

print("\n--- Vigenère Cipher ---")

if ch == '1':
    pt = input("Enter the plaintext: ")
    kw = input("Enter the keyword: ")
    
    et = vigenere_cipher(pt, kw, 1) # Encrypted text
    fk = generate_vigenere_key(pt, kw) # Full key
    
    print("\nEncryption Process:")
    print(f"Plaintext:      {' '.join(list(pt.upper()))}")
    print(f"Repeating Key:  {' '.join(list(fk))}")
    print(f"Ciphertext:     {' '.join(list(et))}\n")
    print(f"Final Encrypted Text: {et}")

elif ch == '2':
    ct = input("Enter the ciphertext: ")
    kw = input("Enter the keyword: ")
    
    dt = vigenere_cipher(ct, kw, 2) # Decrypted text
    print(f"\nDecrypted Text: {dt}")

else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")