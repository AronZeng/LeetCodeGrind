class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ( -> call this open 
        # ) -> call this close 
        # at no given can there be more closed than open brackets 
        
        # NOTE: first bracket will always be open and last will always be closed 
        res = []
        def generateStrings(current, numClose, numOpen, maxItems):
            if numOpen == 0 and numClose == 0: 
                res.append(current)
            if numOpen < maxItems and numOpen > 0: 
                generateStrings(current + "(" , numClose, numOpen - 1, maxItems)
            if numClose > numOpen: 
                generateStrings(current + ")" , numClose - 1, numOpen, maxItems)
        generateStrings("(" , n, n-1, n)
        return res
              
              