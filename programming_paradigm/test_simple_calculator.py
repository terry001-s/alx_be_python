# test_simple_calculator.py
# Unit tests for SimpleCalculator class

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    # --- Division Tests ---
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None
        self.assertEqual(self.calc.divide(0, 5), 0)

    # --- Additional Edge Cases ---
    def test_large_numbers(self):
        """Test arithmetic operations with large numbers."""
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)
        self.assertEqual(self.calc.multiply(1_000, 1_000), 1_000_000)
        self.assertEqual(self.calc.divide(1_000_000, 1_000), 1_000)

if __name__ == "__main__":
    unittest.main()
