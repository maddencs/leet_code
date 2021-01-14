class Solution:
    int_to_roman = (
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I'),
    )

    def intToRoman(self, num: int) -> str:
        as_roman = ''
        current_num = num
        for number, roman in self.int_to_roman:
            if current_num == 0:
                break

            digit, remaining = divmod(current_num, number)
            if digit > 0:
                current_num = remaining

            as_roman += roman * digit

        return as_roman

    def _get_roman_digit(self, roman_numeral, count):
        if roman_numeral == 'I' and count == 4:
            return 'IV'

        if roman_numeral == 'X' and count == 4:
            return ''


print(Solution().intToRoman(2020))