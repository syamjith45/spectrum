import hashlib
import os

def generate_salt():
    return os.urandom(16)  # 16 bytes provides a good balance of security and performance

def hash_password(password, salt):
    # Use PBKDF2 for password hashing
    iterations = 100000  # Adjust this based on your security requirements
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return hashed_password

def verify_password(stored_password, provided_password, salt):
    # Verify the provided password against the stored hashed password and salt
    return stored_password == hash_password(provided_password, salt)

def main():
    # Example usage
    password = "secure_password"
    
    # Generate a unique salt for each user
    salt = generate_salt()

    # Hash and store the password along with the salt
    hashed_password = hash_password(password, salt)

    # Simulate storing the hashed_password and salt in a database
    stored_password = hashed_password  # In a real-world scenario, this would come from the database

    # User login attempt
    login_password = input("Enter your password: ")

    # Verify the provided password during login
    if verify_password(stored_password, login_password, salt):
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
