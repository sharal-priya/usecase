import random 
import string

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
