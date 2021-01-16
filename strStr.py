class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1

        i = 0
        while i < len(haystack):
            char = haystack[i]
            if char == needle[0]:
                j = i
                if haystack[i:i + len(needle)] == needle:
                    return i
            i += 1
        return -1
