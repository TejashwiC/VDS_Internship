from functools import wraps

VALID_USERNAME = "teju"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = VALID_USERNAME.lower().strip()

        if username:  
            print(f"Login successful! Welcome, {username}\n")
            return func(username)
        else:
            print("Username authentication failed.\n")
    return wrapper

@login_required
def access_dashboard(username):
    print(f"Welcome to your dashboard, {username}!\n")


access_dashboard()
