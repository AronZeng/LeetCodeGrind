class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes = sorted(boxTypes, key = lambda boxType: boxType[1])
        currentPosition = len(boxTypes) - 1
        res = 0
        while truckSize != 0 and currentPosition >= 0:
            if (boxTypes[currentPosition][0] > 0):
                truckSize -= 1
                res += boxTypes[currentPosition][1]
                boxTypes[currentPosition][0] -= 1
            else: 
                currentPosition -= 1
        return res
                
