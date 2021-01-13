class Solution:
    def threeSum(self, nums):
        triples = set()
        num_set = set(nums)

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                a = nums[i]
                b = nums[j]
                needed = 0 - (a + b)
                if needed not in [a, b]:
                    if needed in num_set:
                        ordered = sorted([a, b, needed])
                        triples.add(tuple(ordered))

                j += 1
            i += 1
        return triples

print(Solution().threeSum([-1,0,1,2,-1,-4]))