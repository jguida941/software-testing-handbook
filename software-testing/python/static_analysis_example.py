"""Example module for demonstrating static analysis tools - INTENTIONALLY FLAWED VERSION."""

# Missing proper imports organization
from dataclasses import dataclass
import math

# Unused import (pylint will flag this)
import os

# Class without proper documentation
@dataclass
class Order:
    order_id: int
    subtotal: float
    discount_rate = 0.0  # Missing type hint

    def __init__(self, order_id, subtotal, discount_rate=0.0):  # Still intentionally under-documented
        self.order_id = order_id
        self.subtotal = subtotal
        self.discount_rate = discount_rate

    # Method without docstring
    def validate(self):
        if self.subtotal < 0:
            raise ValueError("Subtotal cannot be negative")
        if self.discount_rate < 0 or self.discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1")

# Function with missing type hints and poor variable names
def calculate_total(o, t):  # Poor parameter names
    """Calculate total."""  # Inadequate docstring
    o.validate()

    # Magic numbers without explanation
    d = o.subtotal * o.discount_rate  # Single letter variable
    s = o.subtotal - d  # Single letter variable
    tax = s * t

    # Overly complex expression that could be simplified
    total = s + tax

    # Unnecessary variable assignment
    result = total

    # Line too long - exceeds 79 characters recommended by PEP 8
    if result > 1000000:  # This is a very long comment that makes the line exceed the recommended character limit for Python code according to PEP 8 style guide
        print(f"Large order detected: ${result:.2f}")

    # Missing proper error handling
    return result

# Function missing return type hint
def process_order(order_data: dict):
    """Process an order from raw data."""
    # TODO: This is a placeholder that should be implemented
    pass

# Global variable (bad practice)
GLOBAL_COUNTER = 0

# Function with too many branches (complexity issue)
def categorize_order(total):  # Missing type hints
    global GLOBAL_COUNTER  # Using global variable
    GLOBAL_COUNTER += 1

    # Too many if/elif branches (high cyclomatic complexity)
    if total < 10:
        category = "tiny"
    elif total < 50:
        category = "small"
    elif total < 100:
        category = "medium"
    elif total < 500:
        category = "large"
    elif total < 1000:
        category = "xlarge"
    elif total < 5000:
        category = "huge"
    else:
        category = "massive"

    return category

# Unused variable
unused_var = 42

# Main execution block without proper guard
print("This will execute when imported!")  # Bad practice

# Missing if __name__ == "__main__": guard
order1 = Order(1, 100.0, 0.1)
total1 = calculate_total(order1, 0.08)
print(f"Order total: ${total1:.2f}")

# Class with inconsistent naming
class order_processor:  # Should be CamelCase
    def ProcessOrder(self, order):  # Should be snake_case
        pass


def risky_parse(payload):
    """Intentionally unsafe eval usage to show lint/type findings."""
    return eval(payload)  # noqa: S307 - intentionally insecure for training
