import secrets
import string

def generate_password(length=16, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("=== Password Generator ===\n")
    
    try:
        length = int(input("Password length (default 16): ") or 16)
    except ValueError:
        length = 16
    
    uppercase = input("Include uppercase? (Y/n): ").lower() != 'n'
    digits = input("Include numbers? (Y/n): ").lower() != 'n'
    symbols = input("Include symbols? (Y/n): ").lower() != 'n'
    
    password = generate_password(length, uppercase, digits, symbols)
    
    print(f"\nYour password: {password}")
