from typing import List
class solution:
    def rotate(self,nums:List[int],k:int)->None:
        n=len(nums)
        k=k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    def reverse(self,nums:List[int],start:int,end:int)->None:
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
nums=[1,2,3,4,5,6,7]
k = 3
obj=solution()
obj.rotate(nums,k)
print(nums)