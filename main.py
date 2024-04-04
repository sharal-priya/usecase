import random 
import string

def get_length():
    """ask user for password length."""
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_options():
    """Prompt user for password options."""
    use_symbols = input("Can the password include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Can the password include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Can the password include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Can the password include lowercase letters? (y/n): ").lower() == 'y'
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
