import math 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        x = str(x)
        index = int(math.floor(len(x)/2))
        print(index)
        firstHalf = x[0:index]
        if (len(x) % 2 == 0): 
            return firstHalf[::-1] == x[index:]
        else: 
            return firstHalf[::-1] == x[index + 1 :]
        