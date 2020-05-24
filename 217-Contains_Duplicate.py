class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicateCounter = {}
        for i in range(len(nums)):
            if nums[i] in duplicateCounter: 
                return True
            duplicateCounter[nums[i]] = True
        return False