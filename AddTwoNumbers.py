class ListNode(object): 
    def __init__(self , x):
        self.val = x 
        self.next = None

class Solution(object):
    def addTwoNumbers(self , l1 , l2 , carry = 0):
        sum = l1.val + l2.val + carry
        carry = sum // 10
        ret = ListNode(sum % 10)     
        if l1.next != None or l2.next != None:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None: 
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next , l2.next , carry)  
        else:
            if carry > 0:
                ret.next = ListNode(carry)       
        return ret