import random 
import string

#password generator
def generate_password(length, use_symbols=False, use_numbers=False, use_uppercase=False, use_lowercase=True):
    """Generate a random password."""
    characters = ''
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#end
#Allow User to Specify Length
def get_length():
    """asks user for password length."""
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
#Include Option for Symbols, Numbers, and Uppercase/Lowercase
def get_options():
    """Prompt user for password options."""
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    return use_symbols, use_numbers, use_uppercase, use_lowercase
    
def main():
    """Main function to generate password."""
    length = get_length()
    use_symbols, use_numbers, use_uppercase, use_lowercase = get_options()
    
    try:
        password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
        print("Generated Password:", password)
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
