"""
Basic Calculator Module

This module provides a simple calculator with basic arithmetic operations.
"""


class Calculator:
    """A basic calculator class that performs arithmetic operations."""

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Basic Calculator Demo")
    print("=" * 30)
    
    # Addition
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Subtraction
    result = calc.subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # Multiplication
    result = calc.multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Division
    result = calc.divide(10, 5)
    print(f"10 / 5 = {result}")
    
    # Division by zero handling
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
