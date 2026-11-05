"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a pick-list quantity string and return a positive integer.

    Raises ValueError for non-numeric input or quantities less than 1.
    """
    try:
        qty = int(value.strip())
    except ValueError:
        raise ValueError(f"invalid quantity: {value!r}")
    if qty < 1:
        raise ValueError(f"quantity must be at least 1, got {qty}")
    return qty
