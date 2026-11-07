"""tinystats: tiny statistics helpers."""


def mean(values):
    """The arithmetic mean of a list of numbers."""
    return sum(values) / len(values)


def median(values):
    """The middle value of a list of numbers."""
    if not values:
        raise ValueError("median() of an empty list")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
