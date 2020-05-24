class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        memo = {}
        if len(s) == 0: 
            return ""
        result = s[0]
        for i in range(n): 
            memo[(i,i)] = True
        for i in range(n):
            for j in range(i - 1, -1 , -1): 
                if s[j] == s[i] and (i-j<2 or (j+1,i-1) in memo):
                    memo[(j,i)] = True
                    if i - j + 1 > len(result):
                        result = s[j : i + 1]
        return result
        
        # Return if string is empty
#         if len(s) == 0: 
#             return ""
        
#         result = ""
#         def findLongestPalindrome(s, start, end):
#             while start >= 0 and end < len(s) and s[start] == s[end]: 
#                 start -= 1
#                 end += 1
#             end -= 1
#             start += 1
#             return end - start + 1
            
        
#         for i in range(len(s)):
#             oddCaseLength = findLongestPalindrome(s, i, i)
#             evenCaseLength = findLongestPalindrome(s, i, i+1)
#             maxLength = max(oddCaseLength, evenCaseLength)
#             print(oddCaseLength)
#             print(evenCaseLength)
#             print(maxLength)
#             print("======")
#             if (maxLength > len(result)): 
#                 start = i - int((maxLength - 1) / 2)
#                 end = i + int((maxLength /2))
#                 result = s[start : end + 1]
#         return result
        

            
        
        