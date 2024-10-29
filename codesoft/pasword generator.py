import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    
    # Prompt user for desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length should be at least 4 characters for complexity. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    password_generator()

