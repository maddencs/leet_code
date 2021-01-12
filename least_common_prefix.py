import pytest


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        i = 0
        while i < min(len(s) for s in strs):
            current = strs[0][i]
            for s in strs[1:]:
                if s[i] != current:
                    return strs[0][0:i]

            i += 1
        return strs[0][:i]


test_cases = [
    (['a', 'ac'], 'a'),
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], ''),
    ([], ''),
]


@pytest.mark.parametrize('test_case,expected', test_cases)
def test_least_common_prefix(test_case, expected):
    assert Solution().longestCommonPrefix(test_case) == expected