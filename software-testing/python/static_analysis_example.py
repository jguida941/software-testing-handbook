"""Example module for demonstrating static analysis tools."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Order:
    """Lightweight representation of a shopping cart or checkout order."""

    order_id: int
    subtotal: float
    discount_rate: float = 0.0

    def validate(self) -> None:
        """Raise ValueError if totals or discounts fall outside expected ranges."""
        if self.subtotal < 0:
            raise ValueError("Subtotal cannot be negative.")
        if not 0 <= self.discount_rate <= 0.8:
            raise ValueError("Discount rate must be between 0 and 0.8.")


def calculate_total(order: Order, tax_rate: float) -> float:
    """Return the grand total after discounts and tax."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    order.validate()
    discounted = order.subtotal * (1 - order.discount_rate)
    total = discounted * (1 + tax_rate)
    return round(total, 2)


if __name__ == "__main__":
    example_order = Order(order_id=42, subtotal=120.0, discount_rate=0.15)
    print(f"Grand total: ${calculate_total(example_order, tax_rate=0.07)}")
