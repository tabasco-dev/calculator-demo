# calculator-demo

A basic calculator implementation in Python that provides fundamental arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division error handling)

## Usage

### As a Module

```python
from calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(10, 5)  # Returns 15

# Subtraction
result = calc.subtract(10, 5)  # Returns 5

# Multiplication
result = calc.multiply(10, 5)  # Returns 50

# Division
result = calc.divide(10, 5)  # Returns 2.0

# Division by zero raises ValueError
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

### Running the Demo

```bash
python3 calculator.py
```

## Testing

Run the unit tests with:

```bash
python3 -m unittest test_calculator.py -v
```

## Requirements

- Python 3.x