from typing import List
class solution:
    def MajorityElement(self,nums:List[int])->int:
        count={}
        n=len(nums)
        for num in nums:
            count[num]=count.get(num,0)+1
            if count[num]>n//2:
                return num
        return -1

nums=[2,2,1,1,1,2,2]
obj=solution()
print(obj.MajorityElement(nums))