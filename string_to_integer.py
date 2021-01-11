import pytest


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        number_start = self._find_number_start(s)
        if number_start == -1:
            return 0

        number_end = self._find_number_end(s, number_start)
        is_positive = self._get_is_positive(s, number_start)
        out_of_bounds = self._get_out_of_bounds(s, number_start, number_end, is_positive)
        if out_of_bounds and is_positive:
            return 2 ** 31 - 1
        elif out_of_bounds and not is_positive:
            return -2 ** 31
        else:
            atoi = self._atoi(s, number_start, number_end, is_positive)
            return atoi

    def _find_number_start(self, s):
        i = 0
        while i < len(s):
            if s[i] not in ['+', ' ', '-'] + [str(n) for n in range(10)]:
                return -1
            if s[i] in [str(n) for n in range(10)]:
                return i
            i += 1
        if i >= len(s):
            return - 1

    def _find_number_end(self, s, number_start):
        i = number_start + 1
        number_chars = [str(n) for n in range(10)]

        while i < len(s):
            if s[i] not in number_chars:
                return i
            i += 1
        return i

    def _get_is_positive(self, s, number_start):
        if number_start == 0:
            return True

        if s[number_start - 1] == '-':
            return False
        else:
            return True

    def _get_out_of_bounds(self, s, number_start, number_end, is_positive):
        integer = int(s[number_start:number_end])
        if is_positive and integer > 2 ** 31 - 1:
            return True
        elif not is_positive and - integer < -2 ** 31:
            return True
        else:
            return False

    def _atoi(self, s, number_start, number_end, is_positive):
        number_string = s[number_start:number_end]
        if is_positive:
            return int(number_string)
        else:
            return - int(number_string)

tests = [
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("3.14159", 3),
    (".1", 0),
    ("", 0),
    ("-", 0),
    ("+1", 1),
]


@pytest.mark.parametrize('input,expected', tests)
def test_atoi(input, expected):
    number = Solution().myAtoi(input)

    assert number == expected