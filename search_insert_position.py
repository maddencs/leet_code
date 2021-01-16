from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        i = int(len(nums) / 2)
        while True:
            current = nums[i]
            prev = nums[i - 1]
            if i == 0:
                return 1 if nums[0] < target else 0

            if current == target:
                return i

            if i + 1 < len(nums):
                next = nums[i + 1]
                if next < target:
                    i = int((i + len(nums)) / 2)
                if next > target > prev:
                    return i
            else:
                return i

            if prev > target:
                i = int(i / 2)


print(Solution().searchInsert([1, 3], 0))