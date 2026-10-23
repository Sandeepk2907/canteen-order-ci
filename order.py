"""Order module for the Campus Canteen Pre-Order System."""

GST_RATE = 0.05
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 200  # discount applies only when subtotal is ABOVE this (in rupees)


def calculate_total(subtotal: float) -> float:
    """Return the final payable amount for an order.

    Rules:
      1. A 10% discount applies if the subtotal is above Rs. 300.
      2. 5% GST is then charged on the (discounted) amount.
      3. The result is rounded to 2 decimal places.

    Raises:
        ValueError: if subtotal is negative.
    """
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")

    amount = subtotal
    if subtotal > DISCOUNT_THRESHOLD:
        amount = subtotal * (1 - DISCOUNT_RATE)

    total = amount * (1 + GST_RATE)
    return round(total, 2)
