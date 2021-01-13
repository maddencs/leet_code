class Solution:
    number_to_letters = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits):
        if len(digits) > 0:
            return self._permutations(digits)
        else:
            return []

    def _permutations(self, digits):
        if len(digits) >= 1:
            suffixes = self._permutations(digits[1:])
        else:
            return ['']

        permutations = list()
        for char in self.number_to_letters[digits[0]]:
            for suffix in suffixes:
                permutations.append(char + suffix)

        return permutations