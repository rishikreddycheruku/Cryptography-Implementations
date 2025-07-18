c = input("Enter 1 to verify the theorem or 2 to find the modular inverse: ")

print("\n--- Fermat's Little Theorem ---")

if c == '1':
    a = int(input("Enter an integer (a): "))
    p = int(input("Enter a prime number (p): "))
    
    r = pow(a, p - 1, p)
    
    print(f"\nVerifying a^(p-1) ≡ 1 (mod p)")
    print(f"Result for {a}^({p}-1) mod {p} is: {r}")
    if r == 1:
        print("The theorem holds true.")
    else:
        print("The theorem does not hold (is 'p' a prime number and not a divisor of 'a'?).")

elif c == '2':
    a = int(input("Enter an integer (a) to find its inverse: "))
    p = int(input("Enter the prime modulus (p): "))
    
    i = pow(a, p - 2, p)
    
    print(f"\nFinding inverse: a^(p-2) ≡ a⁻¹ (mod p)")
    print(f"The modular inverse of {a} mod {p} is: {i}")
    print(f"Verification: ({a} * {i}) mod {p} = {(a * i) % p}")

else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")