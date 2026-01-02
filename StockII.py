class solution:
    def maxprofit(self,prices):
        buy=0
        selling=1
        maxprofit=0
        while selling<len(prices):
            if prices[selling]>prices[buy]:
                maxprofit=maxprofit+prices[selling]-prices[buy]
            buy=selling
            selling+=1
        return maxprofit
prices=[7,1,5,3,6,4]
obj=solution()
print(obj.maxprofit(prices))
