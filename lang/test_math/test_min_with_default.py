from decimal import Decimal
from typing import Iterable


def min_with_none(*args, default=None):
    """返回可迭代对象中的最小值，如果可迭代对象为空，返回默认值"""
    if len(args) == 0 or len(args) == 1 and args[0] is None:
        return default
    iterable = args[0] if isinstance(args[0], Iterable) else args
    return min((item for item in iterable if item is not None), default=default)

print(min_with_none(Decimal('0.012'), Decimal('0.005')))
print(min_with_none(Decimal('0.012'), None, default=None))
print(min_with_none((Decimal('0.012'), None, Decimal('0.005')), default=None))


print(min(filter(lambda x: x is not None, (Decimal('0.012'), None, Decimal('0.005')))))

print(min(filter(lambda x: x is not None, (None, None)), default=None))
