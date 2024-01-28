class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices.pop(0)
        for num in prices:
            max_profit = max (max_profit, num-min_price)
            min_price = min (min_price,num)
        return max_profit

# create an instance for solution
solution_instance = Solution()
# Input
prices = [7,1,5,3,6,4]
# Call maxprofit function in the instance
result =solution_instance.maxProfit(prices)
# print result
print(result)