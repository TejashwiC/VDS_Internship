from functools import wraps
import re

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            username = input("Enter username: ").strip().lower()
            password = input("Enter password: ").strip()

            if (len(password) >= 8 and
                re.search(r"[A-Z]", password) and
                re.search(r"[a-z]", password) and
                re.search(r"[0-9]", password) and
                re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):

                print(f"Login successful! ✅ Welcome, {username}\n")
                return func(username)
            else:
                print("Password must be at least 8 characters and include uppercase, lowercase, number, and special character.\n")
    return wrapper

@login_required
def access_dashboard(username):
    print(f"Welcome to your dashboard, {username}!\n")

access_dashboard()
