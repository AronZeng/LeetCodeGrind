# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNode = ListNode(-1)
        currentNode = firstNode
        while l1 and l2: 
            if l1.val < l2.val: 
                currentNode.next = ListNode(l1.val)
                currentNode = currentNode.next
                l1 = l1.next
            else: 
                currentNode.next = ListNode(l2.val)
                currentNode = currentNode.next
                l2 = l2.next
        if l1:
            currentNode.next = l1
        else: 
            currentNode.next = l2
        return firstNode.next
        
        
                
                
                    
                    
                    
                    
        