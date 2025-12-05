"""
Unit tests for the calculator module.
"""

import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
    
    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(5, -3), 8)
    
    def test_subtract_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 6), 30)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
    
    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
    
    def test_divide_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()
