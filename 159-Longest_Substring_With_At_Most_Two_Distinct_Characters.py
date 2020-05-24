class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 or len(s) == 2 or len(s) == 0: 
            return len(s)
        
        leftIndex = 0
        rightIndex = 1 
        maxLength = 2
        if s[0] == s[1]: 
            letterDict = {s[0] : 2}
        else:
            letterDict = {s[0] : 1, s[1] : 1}
        while rightIndex < len(s) - 1:
            
            rightIndex += 1
            if s[rightIndex] in letterDict: 
                letterDict[s[rightIndex]] += 1
            else: 
                letterDict[s[rightIndex]] = 1
            
            while len(letterDict.keys()) == 3:
                if letterDict[s[leftIndex]] == 1:
                    letterDict.pop(s[leftIndex])
                else: 
                    letterDict[s[leftIndex]] -= 1
                leftIndex += 1
                
            if sum(letterDict.values()) > maxLength: 
                maxLength = sum(letterDict.values())
        return maxLength
            