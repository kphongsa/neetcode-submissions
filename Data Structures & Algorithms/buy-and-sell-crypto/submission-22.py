class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0

        profit = 0

        buy = 0
        sell = 1

        for i in range(len(prices)-1): 
            pot = prices[sell]-prices[buy]
            profit = max(profit, pot)
           
            if (prices[i] < prices[buy] and buy < sell): 
                buy = i
                sell = buy + 1
            elif(sell < len(prices)-1): 
                sell += 1
            
        print(buy, sell)

        return max(profit, prices[sell]-prices[buy])

        