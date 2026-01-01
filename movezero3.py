from typing import List
class solution:
    def movezero(self,nums:List[int])->None:
        writepos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i!=writepos:
                    nums[i],nums[writepos]=nums[writepos],nums[i]
                writepos+=1
nums=[0,1,0,3,12]             
obj=solution()
obj.movezero(nums)
print(nums)