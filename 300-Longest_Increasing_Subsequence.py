class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: 
            return 0
        dp = [1]
        for i in range(1,len(nums)):
            dp.append(1)
            for j in range(0 , i): 
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)