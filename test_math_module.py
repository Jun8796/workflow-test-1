"""
Test file for the math_module.
"""

import unittest
from math_module import add_numbers


class TestMathModule(unittest.TestCase):
    """Test cases for math_module functions."""
    
    def test_add_numbers_positive(self):
        """Test adding positive numbers."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
        
    def test_add_numbers_negative(self):
        """Test adding negative numbers."""
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)
        
    def test_add_numbers_mixed(self):
        """Test adding positive and negative numbers."""
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)
        
    def test_add_numbers_zero(self):
        """Test adding with zero."""
        result = add_numbers(0, 5)
        self.assertEqual(result, 5)
        
    def test_add_numbers_float(self):
        """Test adding floating point numbers."""
        result = add_numbers(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2, places=1)


if __name__ == '__main__':
    # Example usage of the module
    print("Testing math_module...")
    print(f"add_numbers(2, 3) = {add_numbers(2, 3)}")
    print(f"add_numbers(5, 7) = {add_numbers(5, 7)}")
    print(f"add_numbers(-1, 4) = {add_numbers(-1, 4)}")
    
    # Run the unit tests
    unittest.main()