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


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        max_length = 1

        start_pos = 0
        end_pos = 1
        seen = set()
        seen.add(s[0])
        while end_pos < len(s):
            current = s[end_pos]

            if current in seen:
                max_length = max(end_pos - start_pos, max_length)
                if s[start_pos] == current:
                    start_pos += 1
                else:
                    start_pos = s.index(current, start_pos + 1)
                seen = set(s[start_pos:end_pos+1])
            else:
                max_length = max(end_pos - start_pos, max_length)

            seen.add(current)
            end_pos += 1

        return max_length


if __name__ == '__main__':
    s = "pwwkew"
    print(Solution2().lengthOfLongestSubstring(s))
