import string
import secrets

def password_generator():
    print("🔐 Unique Password Generator 🔐")
    length = int(input("Enter password length: "))
    print("Select complexity:\n1. Only Letters\n2. Letters & Digits\n3. Letters, Digits & Symbols")
    choice = input("Your choice (1/2/3): ")

    charset = string.ascii_letters
    if choice == '2':
        charset += string.digits
    elif choice == '3':
        charset += string.digits + string.punctuation
    else:
        print("Defaulting to letters only.")

    password = ''.join(secrets.choice(charset) for _ in range(length))
    print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
