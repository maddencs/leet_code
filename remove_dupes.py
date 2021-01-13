import pytest


class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return nums

        replace_index = 1
        current = nums[0]

        i = 1
        while i < len(nums):
            if current != nums[i]:
                nums[replace_index] = nums[i]
                replace_index += 1
                current = nums[i]
            i += 1

        return nums[:replace_index]


tests = [
    ([1, 1, 2], [1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 3, 3], [1, 2, 3]),
    ([], []),
    ([1], [1])
]


@pytest.mark.parametrize('test_case,expected', tests)
def test_remove_dupes(test_case, expected):
    assert Solution().removeDuplicates(test_case) == expected
