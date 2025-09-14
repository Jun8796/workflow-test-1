#!/usr/bin/env python3
"""
Demo script to demonstrate the math_module functionality.
"""

from math_module import add_numbers


def main():
    """Main function to demonstrate the add_numbers function."""
    print("Math Module Demo")
    print("================")
    
    # Test cases
    test_cases = [
        (2, 3),
        (10, 15),
        (-5, 8),
        (0, 7),
        (2.5, 3.7)
    ]
    
    for a, b in test_cases:
        result = add_numbers(a, b)
        print(f"add_numbers({a}, {b}) = {result}")


if __name__ == '__main__':
    main()