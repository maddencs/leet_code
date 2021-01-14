from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_index = 0
        for num in nums:
            if num != val:
                nums[replace_index] = num
                replace_index += 1

        return replace_index
