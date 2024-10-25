#Random password Generator
import random
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    """Generates a random password based on user-defined criteria."""

    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """Gets user input for password length and character types."""

    length = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    return length, include_letters, include_numbers, include_symbols

if __name__ == "__main__":
    length, include_letters, include_numbers, include_symbols = get_user_input()
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print("Generated password:", password)