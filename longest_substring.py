class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        longest_length = 0

        start_pos = 0
        while start_pos < len(s):
            max_seg_length = self._get_max_seg_length(s, start_pos)
            if max_seg_length > longest_length:
                longest_length = max_seg_length

            start_pos += 1

        return longest_length

    def _get_max_seg_length(self, s, start_pos):
        seen = set()
        max_length = 0
        end_pos = start_pos + 1
        for char in s[start_pos:]:

            if char in seen:
                return max_length

            seen.add(char)
            max_length = max(end_pos - start_pos, max_length)
            end_pos += 1

        return max_length


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))