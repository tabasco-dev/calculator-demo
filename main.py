"""
Main script to demonstrate calculator functionality.
"""

from calculator import add, subtract, multiply, divide


def main():
    """Demonstrate basic calculator operations."""
    print("=" * 50)
    print("Python Calculator - Basic Operations Demo")
    print("=" * 50)
    
    # Addition examples
    print("\nAddition:")
    print(f"  5 + 3 = {add(5, 3)}")
    print(f"  -2 + 7 = {add(-2, 7)}")
    print(f"  2.5 + 3.5 = {add(2.5, 3.5)}")
    
    # Subtraction examples
    print("\nSubtraction:")
    print(f"  10 - 4 = {subtract(10, 4)}")
    print(f"  5 - 8 = {subtract(5, 8)}")
    print(f"  7.5 - 2.5 = {subtract(7.5, 2.5)}")
    
    # Multiplication examples
    print("\nMultiplication:")
    print(f"  6 * 7 = {multiply(6, 7)}")
    print(f"  -3 * 4 = {multiply(-3, 4)}")
    print(f"  2.5 * 4 = {multiply(2.5, 4)}")
    
    # Division examples
    print("\nDivision:")
    print(f"  20 / 4 = {divide(20, 4)}")
    print(f"  15 / 3 = {divide(15, 3)}")
    print(f"  7.5 / 2.5 = {divide(7.5, 2.5)}")
    
    # Division by zero example
    print("\nDivision by zero (error handling):")
    try:
        result = divide(10, 0)
        print(f"  10 / 0 = {result}")
    except ValueError as e:
        print(f"  10 / 0 = Error: {e}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
