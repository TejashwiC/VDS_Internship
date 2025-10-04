def simple_decorator(func):
    def wrapper():
        print(" Function Decorator ")
        print("Before function")
        func()
        print("After function")
    return wrapper

def arg_decorator(func):
    def wrapper(*args, **kwargs):
        print("\nDecorator with Arguments ")
        result = func(*args, **kwargs)
        print(f"Result = {result}")
        return result
    return wrapper

class ClassDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("\n Class Decorator ")
        return self.func(*args, **kwargs)

class Demo:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def greet():
        print("\n Built-in Decorators ")
        print("Hello from static method!")

    @classmethod
    def from_value(cls, v):
        return cls(v)

@simple_decorator
def greet():
    print("Hello!")

@arg_decorator
def add(a, b):
    return a + b

@ClassDecorator
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    val = int(input("Enter a value for Demo class: "))

    greet()
    add(x, y)
    say_hello(name)
    d = Demo.from_value(val)
    Demo.greet()
