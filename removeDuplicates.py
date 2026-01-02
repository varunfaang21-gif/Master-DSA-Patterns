from typing import List
class solution:
    def removeDuplicates(self,nums:List[int])->int:
        readpose=1
        writepose=1
        while writepose<len(nums):
            if nums[writepose]!=nums[writepose-1]:
                nums[readpose]=nums[writepose]
                readpose+=1
                writepose+=1
            else:
                writepose+=1
        return readpose
nums=[0,0,1,1,1,2,2,3,3,4]
obj=solution()
print(obj.removeDuplicates(nums))
