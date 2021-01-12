import pytest


class Solution:
    ROMAN_TO_INT_MAP = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        integer = 0
        i = 0
        while i < len(s):
            digit_end = self._get_digit_end(s, i)
            digit = self._parse_digit(s, i, digit_end)
            integer += digit
            i = digit_end
        return integer

    def _get_digit_end(self, s, digit_start):
        current = s[digit_start]
        next_idx = digit_start + 1
        while next_idx < len(s):
            next_numeral = s[next_idx]
            if self.ROMAN_TO_INT_MAP[next_numeral] > self.ROMAN_TO_INT_MAP[current]:
                current = next_numeral
                next_idx += 1
            else:
                break
        return next_idx

    def _parse_digit(self, s, start, end):
        i = end - 1
        value = self.ROMAN_TO_INT_MAP[s[i]]
        if i == start:
            return value

        i -= 1
        while i >= start:
            value -= self.ROMAN_TO_INT_MAP[s[i]]
            i -= 1
        return value





        # numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        # values = [1, 5, 10, 50, 100, 500, 1000]
        #
        # number = 0
        # i = 0
        # while i < len(s):
        #     numeral_index = numerals.index(s[i])
        #     next_index = numerals.index(s[i + 1]) if len(s) > i + 1 else None
        #     if next_index:
        #         if next_index > numeral_index:
        #             number += values[next_index] - values[numeral_index]
        #             i = next_index + 1
        #         else:
        #             number += values[numeral_index]
        #             i += 1
        #     else:
        #         number += values[numeral_index]
        #         i += 1
        #
        # return number


tests = [
    ("III", 3),
    ("IV", 4),
    ("MCMXCIV", 1994),
]


@pytest.mark.parametrize('test_case,expected', tests)
def test_roman_to_int(test_case, expected):
    r_to_i = Solution().romanToInt(test_case)
    assert r_to_i == expected