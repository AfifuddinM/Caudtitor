import sqlite3
import hashlib

def login(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    
    user = cursor.fetchone()
    connection.close()
    
    if user:
        print("Login successful")
    else:
        print("Login failed")

def store_password(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"Storing hashed password: {hashed_password}")

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)
store_password(password)