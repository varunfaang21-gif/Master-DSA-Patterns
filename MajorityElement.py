from typing import List
class solution:
    def MajorityElement(self,nums:List[int])->int:
        cand=None
        count=0
        for num in nums:
            if count==0:
                cand=num
            if cand==num:
                count+=1
            else:
                count-=1
        return cand
nums=[2,2,1,1,1,2,2]
obj=solution()
print(obj.MajorityElement(nums))
