class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        restriction: cannot buy one day after selling (to buy on day i then we have sold on i - 2)

        goal: determine max profit on the last day (implies that we have no stocks in hand)

        states: 
          max profit on day i with 0 stock 
          max profit on day i with 1 stock 

        base case: 
          dp[0][0] -> 0 
          dp[0][1] -> -price[0]
          dp[1][1] -> max()
        """      

        