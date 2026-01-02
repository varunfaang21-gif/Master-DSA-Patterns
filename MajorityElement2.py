from typing import List
class solution:
    def MajorityElement(self,nums:List[int])->int:
        nums.sort()
        return nums[len(nums)//2]
nums=[2,2,1,1,1,2,2]
obj=solution()
print(obj.MajorityElement(nums))