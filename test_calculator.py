"""
Unit tests for the calculator module.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 4), 40)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_multiply_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_decimal_result(self):
        """Test division that results in a decimal."""
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
