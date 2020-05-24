class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        DP Problem
        MP(i) will represent the max profit for the array [i ... n ] where n is the length of the array minus 1
        
        Base Cases: 
        MP(n) = 0 -> there is only one price and best thing you can do is not buy 
        MP(n - 1) = max(price[n - 1] - price[n] , MP(n))
        
        We should continue to do this until we get MP(0) -> represents our entire array 
        
        Say we have MP(i)    
        To get MP(i - 1): 
            Case 1: We dont buy at MP(i-1) -> MP(i)
            Case 2: We do buy at MP(i-1) -> price[i-1] - price[sell] + MP(sell + 2) , sell -> [i,n] 
        """
        length = len(prices) + 2 #we want to add the 2 because we dont want out of range for last element
        MP = [0] * length #[0 , 0, 0, ... ] -> represent up to MP[len(prices) + 2]
        for i in range (length - 3 , -1 , -1): 
            case1 = MP[i + 1] #we dont buy at i
            case2 = 0 
            #what if we do buy at i
            for sell in range(i + 1 , len(prices)): 
                case2 = max(prices[sell] - prices[i] + MP[sell + 2] , case2)
            MP[i] = max(case1 , case2)
        return MP[0]
        