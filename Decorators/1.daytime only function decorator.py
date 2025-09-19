from datetime import datetime
import functools
def daytime_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_hour = datetime.now().hour
        if 6 <= current_hour < 18:
            return func(*args, **kwargs)
        else:
            return f"Function '{func._name_}' can only run between 6 AM and 6 PM."
    return wrapper
print("Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
@daytime_only
def greet():
    return "Good day! The function is running."
print(greet())
