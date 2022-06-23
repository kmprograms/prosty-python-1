
"""
    Napisz program, w którym losujesz dwie liczby całkowite z przedziału [100, 999]
    i wyznaczasz tę, która posiada większą cyfrę jedności.
"""

import random
from typing import Final

def draw_int_number(range_min: int, range_max: int) -> int:
    if range_min > range_max:
        raise ValueError('Range is not correct')
    return random.randint(range_min, range_max)

def get_number_with_bigger_units_digit(n1: int, n2: int) -> int:
    return n1 if n1 % 10 > n2 % 10 else n2

def main() -> None:
    RANGE_MIN: Final = 100
    RANGE_MAX: Final = 999

    n1 = draw_int_number(RANGE_MIN, RANGE_MAX)
    n2 = draw_int_number(RANGE_MIN, RANGE_MAX)
    print(f'{n1 = }, {n2 = }')
    print(get_number_with_bigger_units_digit(n1, n2))

if __name__ == '__main__':
    main()





