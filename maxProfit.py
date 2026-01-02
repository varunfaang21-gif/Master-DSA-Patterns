class solution:
    def maxProfit(self,prices):
        buy=0
        selling=1
        maxprofit=0
        while selling<len(prices):
            if prices[selling]>prices[buy]:
                profit=prices[selling]-prices[buy]
                if profit>maxprofit:
                    maxprofit=profit
            else:
                prices[buy]=prices[selling]
            selling+=1
        return maxprofit

prices=[7,1,5,3,6,4]
obj=solution()
print(obj.maxProfit(prices))