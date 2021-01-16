class Solution:
    def longestPalindrome(self, s: str) -> str:
        substr_start = 0
        longest_length = 0
        longest_start = 0
        longest_end = 1
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s):
                if self._compare(s, i, j):
                    # if s[i:j] == s[i:j][::-1]:
                    if j - i > longest_length:
                        longest_length = j - i
                        longest_start = i
                        longest_end = j
                j += 1
            i += 1
        return s[longest_start:longest_end]

    def _compare(self, s, start, end):
        i = start
        while i < end:
            if s[end - i] != s[i]:
                return False
            i += 1
        return True
