import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def get_password_criteria():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be greater than 0. Please try again.")
                continue
            complexity = input("Enter the desired complexity level (low/medium/high): ").lower()
            if complexity not in ['low', 'medium', 'high']:
                print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
                continue
            return length, complexity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Password Generator!")
    length, complexity = get_password_criteria()
    password = generate_password(length, complexity)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()