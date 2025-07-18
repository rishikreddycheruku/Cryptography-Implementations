def shift_cipher(t, k, m):
    """A function to perform a shift cipher."""
    r = ""
    if m == 2:  # Set key for decryption
        k = -k
        
    for c in t:
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            sc = chr((ord(c) - start + k) % 26 + start)
            r += sc
        else:
            r += c
    return r

ch = input("Enter 1 to encrypt or 2 to decrypt: ")

print("\n--- Shift Cipher ---")

if ch == '1':
    pt = input("Enter the plaintext: ")
    try:
        k = int(input("Enter the shift key (an integer): "))
        et = shift_cipher(pt, k, 1) # Mode 1 for encrypt
        print(f"Encrypted Text: {et}")
    except ValueError:
        print("Invalid key. Please enter an integer.")

elif ch == '2':
    ct = input("Enter the ciphertext: ")
    try:
        k = int(input("Enter the shift key (an integer): "))
        dt = shift_cipher(ct, k, 2) # Mode 2 for decrypt
        print(f"Decrypted Text: {dt}")
    except ValueError:
        print("Invalid key. Please enter an integer.")
    
else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")