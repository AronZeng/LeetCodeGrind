class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        currClosest = None
        for i in range(len(nums) - 2): 
            leftPointer = i + 1
            rightPointer = len(nums) - 1
            currSum = 0
            while leftPointer < rightPointer: 
                currSum = nums[i] + nums[leftPointer] + nums[rightPointer]
                if currSum == target:
                    return target
                if currSum < target: 
                    leftPointer += 1
                else:
                    rightPointer -= 1
                if currClosest == None: 
                    currClosest = currSum
                elif abs(target - currSum) < abs(target - currClosest): 
                    currClosest = currSum
        return currClosest

        #try to implement this solution with a BST