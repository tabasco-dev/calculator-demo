# calculator-demo

A simple Python calculator that provides basic arithmetic operations.

## Features

The calculator supports the following operations:
- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero division error handling)

## Usage

### As a Module

You can import the calculator functions in your Python code:

```python
from calculator import add, subtract, multiply, divide

# Perform calculations
result = add(5, 3)        # Returns 8
result = subtract(10, 4)  # Returns 6
result = multiply(6, 7)   # Returns 42
result = divide(20, 4)    # Returns 5.0
```

### Running the Demo

Run the main script to see a demonstration of all calculator operations:

```bash
python main.py
```

### Running Tests

Run the test suite to verify all operations work correctly:

```bash
python test_calculator.py
```

Or use unittest discovery:

```bash
python -m unittest test_calculator.py
```

## API Reference

### `add(a, b)`
Returns the sum of two numbers.

### `subtract(a, b)`
Returns the difference when b is subtracted from a.

### `multiply(a, b)`
Returns the product of two numbers.

### `divide(a, b)`
Returns the quotient when a is divided by b.
- Raises `ValueError` if b is zero.

## Examples

```python
from calculator import add, subtract, multiply, divide

# Basic operations
print(add(10, 5))       # Output: 15
print(subtract(10, 5))  # Output: 5
print(multiply(10, 5))  # Output: 50
print(divide(10, 5))    # Output: 2.0

# Works with negative numbers
print(add(-5, 3))       # Output: -2
print(multiply(-3, 4))  # Output: -12

# Works with floating point numbers
print(add(2.5, 3.5))    # Output: 6.0
print(divide(7.5, 2.5)) # Output: 3.0

# Error handling
try:
    divide(10, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
```