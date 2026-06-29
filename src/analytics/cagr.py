"""
Sprint 2 - Day 10
CAGR Engine
"""

from math import pow


def calculate_cagr(start, end, years):
    """
    CAGR Formula:
    ((End / Start) ** (1 / Years) - 1) * 100
    """

    if years <= 0:
        return None, "INVALID_PERIOD"

    if start == 0:
        return None, "ZERO_BASE"

    if years < 3:
        return None, "INSUFFICIENT"

    if start > 0 and end > 0:
        value = (pow(end / start, 1 / years) - 1) * 100
        return round(value, 2), "NORMAL"

    if start > 0 and end < 0:
        return None, "DECLINE_TO_LOSS"

    if start < 0 and end > 0:
        return None, "TURNAROUND"

    if start < 0 and end < 0:
        return None, "BOTH_NEGATIVE"

    return None, "UNKNOWN"