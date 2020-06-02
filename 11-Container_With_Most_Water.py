class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftPointer = 0 
        rightPointer = len(height) - 1
        maxArea = 0
        while leftPointer < rightPointer: 
            currArea = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            if currArea > maxArea: 
                maxArea = currArea
            if height[leftPointer] < height[rightPointer]: 
                leftPointer += 1 
            else: 
                rightPointer -= 1
        return maxArea