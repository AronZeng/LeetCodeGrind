class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        memo={}
        def dp(d, target): 
            result = 0
            if (d == 0 and target > 0) or (dp > 0 and target == 0): 
                return 0 
            if d == 1 and target <= f:                
                return 1
            if (d ,target) in memo: 
                return memo[(d,target)]
            for i in range(1 , f + 1):
                result += dp(d - 1, max(0,target - i))
            memo[(d,target)] = result
            return result
        return dp(d, target) % (10**9 + 7)