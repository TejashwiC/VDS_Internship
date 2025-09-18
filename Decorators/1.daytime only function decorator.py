from functools import wraps

def daytime_only(func):
    @wraps(func)
    def wrapper():
        current_hour = int(input("Enter current hour (0-23): "))
        
        if 6 <= current_hour < 18:
            return func()
        else:
            print("Function can only run during daytime (6 AM to 6 PM).")
    return wrapper

@daytime_only
def greet():
    print("Good day! Function executed.")

greet()
