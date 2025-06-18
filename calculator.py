#!/usr/bin/env python3
"""
Simple Calculator - A Python program that can calculate given numbers
Supports basic arithmetic operations, trigonometric functions, and more.
"""

import math
import sys

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Calculate a raised to the power of b"""
    return a ** b

def square_root(a):
    """Calculate the square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(a)

def factorial(a):
    """Calculate factorial of a number"""
    if a < 0:
        raise ValueError("Cannot calculate factorial of negative number!")
    if a == 0 or a == 1:
        return 1
    return math.factorial(int(a))

def sin(a):
    """Calculate sine of a number (in radians)"""
    return math.sin(a)

def cos(a):
    """Calculate cosine of a number (in radians)"""
    return math.cos(a)

def tan(a):
    """Calculate tangent of a number (in radians)"""
    return math.tan(a)

def log(a, base=10):
    """Calculate logarithm of a number"""
    if a <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number!")
    return math.log(a, base)

def ln(a):
    """Calculate natural logarithm of a number"""
    if a <= 0:
        raise ValueError("Cannot calculate natural logarithm of non-positive number!")
    return math.log(a)

def get_number_input(prompt):
    """Get a valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main calculator function"""
    print("=" * 50)
    print("           PYTHON CALCULATOR")
    print("=" * 50)
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root (√)")
    print("7. Factorial (!)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Logarithm (log)")
    print("12. Natural Logarithm (ln)")
    print("13. Exit")
    print("=" * 50)
    
    while True:
        try:
            choice = input("\nEnter your choice (1-13): ").strip()
            
            if choice == '13':
                print("Thank you for using the calculator!")
                break
            elif choice == '1':  # Addition
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = add(a, b)
                print(f"{a} + {b} = {result}")
                
            elif choice == '2':  # Subtraction
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = subtract(a, b)
                print(f"{a} - {b} = {result}")
                
            elif choice == '3':  # Multiplication
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = multiply(a, b)
                print(f"{a} * {b} = {result}")
                
            elif choice == '4':  # Division
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = divide(a, b)
                print(f"{a} / {b} = {result}")
                
            elif choice == '5':  # Power
                a = get_number_input("Enter base number: ")
                b = get_number_input("Enter exponent: ")
                result = power(a, b)
                print(f"{a} ** {b} = {result}")
                
            elif choice == '6':  # Square Root
                a = get_number_input("Enter number: ")
                result = square_root(a)
                print(f"√{a} = {result}")
                
            elif choice == '7':  # Factorial
                a = get_number_input("Enter number: ")
                result = factorial(a)
                print(f"{int(a)}! = {result}")
                
            elif choice == '8':  # Sine
                a = get_number_input("Enter angle in radians: ")
                result = sin(a)
                print(f"sin({a}) = {result}")
                
            elif choice == '9':  # Cosine
                a = get_number_input("Enter angle in radians: ")
                result = cos(a)
                print(f"cos({a}) = {result}")
                
            elif choice == '10':  # Tangent
                a = get_number_input("Enter angle in radians: ")
                result = tan(a)
                print(f"tan({a}) = {result}")
                
            elif choice == '11':  # Logarithm
                a = get_number_input("Enter number: ")
                base = get_number_input("Enter base (default 10): ")
                result = log(a, base)
                print(f"log_{base}({a}) = {result}")
                
            elif choice == '12':  # Natural Logarithm
                a = get_number_input("Enter number: ")
                result = ln(a)
                print(f"ln({a}) = {result}")
                
            else:
                print("Invalid choice! Please enter a number between 1 and 13.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 