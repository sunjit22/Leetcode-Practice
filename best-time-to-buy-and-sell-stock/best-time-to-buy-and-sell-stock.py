class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if prices == prices.sort(reverse = True):
        #     return 0
        
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         if (profit > maxProfit):
        #             maxProfit = profit 
        # return maxProfit        
        
        
        minimum = 10000000
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif (prices[i] - minimum > profit):
                profit = prices[i] - minimum
        return profit        
            
        