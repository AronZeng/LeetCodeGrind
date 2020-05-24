# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        hashTable = {}
        def searchFunction(root):
            if root == None: 
                return
            hashTable[target - root.val] = 1
            if root.left: 
                searchFunction(root.left)
            if root.right:
                searchFunction(root.right)
        
        searchFunction(root1)
        
        def findComplement(root):            
            if root == None: 
                return False
            if root.val in hashTable:
                return True
            left = False
            right = False
            if root.left: 
                 left = findComplement(root.left)
            if root.right: 
                right = findComplement(root.right)
            if left or right:
                return True
        
        result = findComplement(root2)
        return result
            
        