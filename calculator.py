def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def division(x, y):
    """Function to divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y