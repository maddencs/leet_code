import pytest


def reverse(num):
    digits = list()
    current = abs(num)
    length = 0
    while current:
        digits.append(int(current % 10))
        current = int(current / 10)
        length += 1
        if length > 10:
            return 0
    reverse_num = 0
    i = 0
    while i < len(digits):
        modifier = digits[::-1][i]*(10**i)
        if num < 0:
            reverse_num -= modifier
        else:
            reverse_num += modifier
        i += 1

    if reverse_num > 2**31 - 1 or reverse_num < -2**31:
        return 0
    return reverse_num


tests = [
    (123, 321),
    (-123, -321),
    (2147483648, 0),
    (-2147483649, 0)
]


@pytest.mark.parametrize('num,expected', tests)
def test_reverse(num, expected):
    assert reverse(num) == expected


