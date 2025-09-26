import random
import string


def generate_password(length=12, use_numbers=True, use_symbols=True):
    """Generate a random password"""
    characters = string.ascii_letters  # Always include letters

    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if len(characters) == 0:
        return "Please select at least one character type"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    """Check the strength of a password"""
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Add numbers")

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        strength += 1
    else:
        feedback.append("Add symbols")

    # Strength rating
    if strength == 5:
        rating = "Very Strong"
    elif strength >= 3:
        rating = "Strong"
    elif strength >= 2:
        rating = "Moderate"
    else:
        rating = "Weak"

    return strength, rating, feedback


def main():
    print("=== Password Generator & Strength Checker ===")

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            try:
                length = int(
                    input("Enter password length (default 12): ") or 12)
                use_numbers = input(
                    "Include numbers? (y/n, default y): ").lower() != 'n'
                use_symbols = input(
                    "Include symbols? (y/n, default y): ").lower() != 'n'

                password = generate_password(length, use_numbers, use_symbols)
                print(f"\nGenerated Password: {password}")

                # Check strength
                strength, rating, feedback = check_password_strength(password)
                print(f"Password Strength: {rating} ({strength}/5)")

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            password = input("Enter password to check: ")
            strength, rating, feedback = check_password_strength(password)

            print(f"\nPassword Strength: {rating} ({strength}/5)")
            if feedback:
                print("Suggestions:")
                for item in feedback:
                    print(f"  {item}")
            else:
                print("✓ Great password!")

        elif choice == "3":
            print("Goodbye! Stay secure!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
