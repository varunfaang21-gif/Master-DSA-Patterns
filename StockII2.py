class solution:
    def maxprofit(self,prices):
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxprofit=maxprofit+prices[i]-prices[i-1]
        return maxprofit
prices=[7,1,5,3,6,4]
obj=solution()
print(obj.maxprofit(prices))
   