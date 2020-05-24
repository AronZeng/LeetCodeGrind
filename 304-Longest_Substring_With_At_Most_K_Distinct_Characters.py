class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= k: 
            return len(s)
        
        leftIndex = 0
        rightIndex = k
        maxLength = k
        done = False
        hashTable = {}
        while not done: 
            rightIndex += 1 
            if len(set(s[leftIndex : rightIndex])) > k: 
                #move first char out of the window 
                
            if maxLength < len(s[leftIndex : rightIndex]): 
                maxLength = len(s[leftIndex : rightIndex])
            hashTable[s[rightIndex]] = rightIndex
            if rightIndex == len(s):
                return maxLength
        