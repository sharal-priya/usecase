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
