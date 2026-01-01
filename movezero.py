from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        result = [0] * n
        j = 0

        for i in range(n):
            if nums[i] != 0:
                result[j] = nums[i]
                j += 1

        for i in range(n):
            nums[i] = result[i]


nums = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(nums)
print(nums)
